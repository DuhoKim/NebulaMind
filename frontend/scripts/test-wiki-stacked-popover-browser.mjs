import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import net from "node:net";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";

const frontendRoot = path.resolve(import.meta.dirname, "..");
// Browser stack fixture contract: galaxy-evolution-v2 is public, requires no auth,
// and currently renders multiple claim trust badges with mini-map hover cards. The
// route has no source-trace triggers today, so this smoke locks the real available
// evidence-panel + claim-mini-map stack; source-trace browser coverage is a follow-up
// when a deterministic route/fixture with source-trace triggers exists.
const routePath = process.env.WIKI_STACKED_POPOVER_PATH || "/wiki/galaxy-evolution-v2";
const nextPort = Number(process.env.WIKI_STACKED_POPOVER_NEXT_PORT || 3033);
const chromePort = Number(process.env.WIKI_STACKED_POPOVER_CHROME_PORT || 9234);
const baseUrl = process.env.WIKI_STACKED_POPOVER_BASE_URL || `http://127.0.0.1:${nextPort}`;
const pageUrl = new URL(routePath, baseUrl).toString();
const chromeBinary = process.env.CHROME_BIN || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const chromeProfile = path.join(os.tmpdir(), `nebulamind-stacked-popover-chrome-${process.pid}`);
const STARTUP_TIMEOUT_MS = 45_000;
const SELECTOR_TIMEOUT_MS = 30_000;
const CDP_COMMAND_TIMEOUT_MS = 45_000;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitFor(predicate, timeoutMs, description) {
  const start = Date.now();
  let lastError;
  while (Date.now() - start < timeoutMs) {
    try {
      const value = await predicate();
      if (value) return value;
    } catch (error) {
      lastError = error;
    }
    await sleep(250);
  }
  throw new Error(`Timed out waiting for ${description}${lastError ? `: ${lastError.message}` : ""}`);
}

function requestJson(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let body = "";
      res.setEncoding("utf8");
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => {
        if ((res.statusCode || 0) >= 400) {
          reject(new Error(`${url} returned ${res.statusCode}: ${body.slice(0, 240)}`));
          return;
        }
        try {
          resolve(JSON.parse(body));
        } catch (error) {
          reject(error);
        }
      });
    });
    req.on("error", reject);
    req.setTimeout(8_000, () => req.destroy(new Error(`${url} timed out`)));
  });
}

async function waitForHttpOk(url, timeoutMs) {
  await waitFor(async () => {
    try {
      const res = await fetch(url, { redirect: "manual" });
      return res.status >= 200 && res.status < 500;
    } catch {
      return false;
    }
  }, timeoutMs, `${url} to respond`);
}

function spawnLogged(command, args, options = {}) {
  const output = [];
  const child = spawn(command, args, { ...options, stdio: ["ignore", "pipe", "pipe"] });
  child.stdout.on("data", (chunk) => output.push(String(chunk)));
  child.stderr.on("data", (chunk) => output.push(String(chunk)));
  child.outputTail = () => output.join("").split(/\r?\n/).slice(-20).join("\n");
  return child;
}

async function stopChild(child, name) {
  if (!child || child.exitCode !== null) return;
  child.kill("SIGTERM");
  for (let i = 0; i < 30; i += 1) {
    if (child.exitCode !== null) return;
    await sleep(100);
  }
  child.kill("SIGKILL");
  for (let i = 0; i < 20; i += 1) {
    if (child.exitCode !== null) return;
    await sleep(100);
  }
  console.warn(`${name} required SIGKILL during cleanup`);
}

class CdpClient {
  constructor(wsUrl) {
    const parsed = new URL(wsUrl);
    this.host = parsed.hostname;
    this.port = Number(parsed.port);
    this.path = `${parsed.pathname}${parsed.search}`;
    this.socket = null;
    this.buffer = Buffer.alloc(0);
    this.nextId = 1;
    this.pending = new Map();
  }

  async connect() {
    this.socket = net.createConnection({ host: this.host, port: this.port });
    await new Promise((resolve, reject) => {
      this.socket.once("connect", resolve);
      this.socket.once("error", reject);
    });
    const key = crypto.randomBytes(16).toString("base64");
    this.socket.write(
      `GET ${this.path} HTTP/1.1\r\n` +
      `Host: ${this.host}:${this.port}\r\n` +
      `Upgrade: websocket\r\n` +
      `Connection: Upgrade\r\n` +
      `Sec-WebSocket-Key: ${key}\r\n` +
      `Sec-WebSocket-Version: 13\r\n\r\n`,
    );
    let handshake = Buffer.alloc(0);
    await new Promise((resolve, reject) => {
      const onData = (chunk) => {
        handshake = Buffer.concat([handshake, chunk]);
        const marker = handshake.indexOf("\r\n\r\n");
        if (marker !== -1) {
          this.socket.off("data", onData);
          const header = handshake.slice(0, marker).toString("utf8");
          if (!header.includes("101")) {
            reject(new Error(`WebSocket handshake failed: ${header}`));
            return;
          }
          this.buffer = handshake.slice(marker + 4);
          this.socket.on("data", (data) => this.handleData(data));
          if (this.buffer.length) this.handleData(Buffer.alloc(0));
          resolve();
        }
      };
      this.socket.on("data", onData);
      this.socket.once("error", reject);
    });
  }

  handleData(data) {
    this.buffer = Buffer.concat([this.buffer, data]);
    while (this.buffer.length >= 2) {
      const first = this.buffer[0];
      const second = this.buffer[1];
      const opcode = first & 0x0f;
      let offset = 2;
      let length = second & 0x7f;
      if (length === 126) {
        if (this.buffer.length < offset + 2) return;
        length = this.buffer.readUInt16BE(offset);
        offset += 2;
      } else if (length === 127) {
        if (this.buffer.length < offset + 8) return;
        const high = this.buffer.readUInt32BE(offset);
        const low = this.buffer.readUInt32BE(offset + 4);
        length = high * 2 ** 32 + low;
        offset += 8;
      }
      const masked = Boolean(second & 0x80);
      let mask;
      if (masked) {
        if (this.buffer.length < offset + 4) return;
        mask = this.buffer.slice(offset, offset + 4);
        offset += 4;
      }
      if (this.buffer.length < offset + length) return;
      let payload = this.buffer.slice(offset, offset + length);
      this.buffer = this.buffer.slice(offset + length);
      if (masked) {
        payload = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
      }
      if (opcode === 8) return;
      if (opcode !== 1) continue;
      const message = JSON.parse(payload.toString("utf8"));
      if (message.id && this.pending.has(message.id)) {
        const { resolve, reject } = this.pending.get(message.id);
        this.pending.delete(message.id);
        if (message.error) reject(new Error(JSON.stringify(message.error)));
        else resolve(message.result);
      }
    }
  }

  sendFrame(text) {
    const payload = Buffer.from(text, "utf8");
    const mask = crypto.randomBytes(4);
    const header = [];
    header.push(0x81);
    if (payload.length < 126) {
      header.push(0x80 | payload.length);
    } else if (payload.length < 65536) {
      header.push(0x80 | 126, (payload.length >> 8) & 0xff, payload.length & 0xff);
    } else {
      header.push(0x80 | 127, 0, 0, 0, 0, (payload.length >>> 24) & 0xff, (payload.length >>> 16) & 0xff, (payload.length >>> 8) & 0xff, payload.length & 0xff);
    }
    const masked = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
    this.socket.write(Buffer.concat([Buffer.from(header), mask, masked]));
  }

  command(method, params = {}) {
    const id = this.nextId++;
    this.sendFrame(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`${method} timed out`));
      }, CDP_COMMAND_TIMEOUT_MS);
      this.pending.set(id, {
        resolve: (value) => {
          clearTimeout(timeout);
          resolve(value);
        },
        reject: (error) => {
          clearTimeout(timeout);
          reject(error);
        },
      });
    });
  }

  async evaluate(expression, awaitPromise = true) {
    const result = await this.command("Runtime.evaluate", {
      expression,
      awaitPromise,
      returnByValue: true,
      userGesture: true,
    });
    if (result.exceptionDetails) {
      throw new Error(`Runtime.evaluate exception: ${JSON.stringify(result.exceptionDetails)}`);
    }
    return result.result?.value;
  }

  async pressEscape() {
    await this.command("Input.dispatchKeyEvent", {
      type: "keyDown",
      windowsVirtualKeyCode: 27,
      nativeVirtualKeyCode: 27,
      macCharCode: 27,
      key: "Escape",
      code: "Escape",
    });
    await this.command("Input.dispatchKeyEvent", {
      type: "keyUp",
      windowsVirtualKeyCode: 27,
      nativeVirtualKeyCode: 27,
      macCharCode: 27,
      key: "Escape",
      code: "Escape",
    });
  }

  close() {
    this.socket?.end();
  }
}

const interactionScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => ({
    claimBadges: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
    miniMapTriggers: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
    panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
    miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
    activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  });
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelectorAll('[data-testid="claim-trust-badge"]').length > 0, 'claim badges');
  await waitFor(() => document.querySelectorAll('[data-testid="claim-trust-badge"]').length > 0, 'claim mini-map triggers');

  const claimBadge = document.querySelector('[data-testid="claim-trust-badge"]');
  claimBadge.scrollIntoView({ block: 'center', inline: 'center' });
  claimBadge.click();
  await waitFor(() => document.querySelector('[data-testid="evidence-panel-dialog"]'), 'evidence panel open');

  const miniMapTrigger = document.querySelectorAll('[data-testid="claim-trust-badge"]')[1] || document.querySelector('[data-testid="claim-trust-badge"]');
  miniMapTrigger.scrollIntoView({ block: 'center', inline: 'center' });
  miniMapTrigger.focus();
  miniMapTrigger.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
  miniMapTrigger.parentElement?.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
  await waitFor(() => document.querySelector('[data-testid="claim-mini-map-hover-card"]'), 'claim mini-map hover card open with panel');

  return state();
})()`;

const firstEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  dialogRole: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('role') || '',
  ariaModal: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-modal') || '',
  panelLabelledBy: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-labelledby')),
}))()`;

const secondEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
}))()`;

async function main() {
  assert.ok(fs.existsSync(path.join(frontendRoot, ".next", "BUILD_ID")), "Run npm run build before smoke:wiki-stacked-popover-browser so next start can serve a production build.");
  assert.ok(fs.existsSync(chromeBinary), `Chrome binary not found at ${chromeBinary}; set CHROME_BIN to override.`);

  fs.rmSync(chromeProfile, { recursive: true, force: true });
  const next = process.env.WIKI_STACKED_POPOVER_BASE_URL
    ? null
    : spawnLogged("npm", ["run", "start", "--", "-p", String(nextPort)], { cwd: frontendRoot });
  let chrome;
  let cdp;
  try {
    await waitForHttpOk(pageUrl, STARTUP_TIMEOUT_MS);
    chrome = spawnLogged(chromeBinary, [
      "--headless=new",
      "--disable-gpu",
      "--no-first-run",
      "--no-default-browser-check",
      "--disable-background-networking",
      `--remote-debugging-port=${chromePort}`,
      `--user-data-dir=${chromeProfile}`,
      pageUrl,
    ]);
    const targets = await waitFor(async () => {
      const pages = await requestJson(`http://127.0.0.1:${chromePort}/json/list`);
      return pages.find((page) => page.type === "page" && page.webSocketDebuggerUrl);
    }, STARTUP_TIMEOUT_MS, "Chrome DevTools target");
    cdp = new CdpClient(targets.webSocketDebuggerUrl);
    await cdp.connect();
    await cdp.command("Runtime.enable");
    await cdp.command("Page.enable");
    await waitFor(async () => {
      try {
        const ready = await cdp.evaluate(`(() => ({ href: location.href, readyState: document.readyState }))()`);
        return ready && ready.href.includes(routePath) && ready.readyState !== "loading";
      } catch {
        return false;
      }
    }, STARTUP_TIMEOUT_MS, "Chrome page navigation to stabilize");

    const initial = await cdp.evaluate(interactionScript);
    assert.equal(initial.panelOpen, true, "Evidence panel should be open before stacked Escape smoke.");
    assert.equal(initial.miniMapOpen, true, "Claim mini-map hover card should be open above/with the evidence panel before first Escape.");
    assert.equal(initial.activeTestId, "claim-trust-badge", "Claim badge should own keyboard focus before first Escape.");

    await cdp.pressEscape();
    await sleep(300);
    const afterFirstEscape = await cdp.evaluate(firstEscapeStateScript);
    assert.equal(afterFirstEscape.miniMapOpen, false, "First Escape should close only the claim mini-map hover card.");
    assert.equal(afterFirstEscape.panelOpen, true, "First Escape should leave the evidence panel dialog open.");
    assert.equal(afterFirstEscape.activeTestId, "claim-trust-badge", "First Escape should return focus to the claim badge mini-map trigger.");
    assert.equal(afterFirstEscape.dialogRole, "dialog", "Evidence panel should keep dialog role after top-popover Escape.");
    assert.equal(afterFirstEscape.ariaModal, "true", "Evidence panel should keep aria-modal after top-popover Escape.");
    assert.equal(afterFirstEscape.panelLabelledBy, true, "Evidence panel should keep aria-labelledby after top-popover Escape.");

    await cdp.pressEscape();
    await sleep(350);
    const afterSecondEscape = await cdp.evaluate(secondEscapeStateScript);
    assert.equal(afterSecondEscape.panelOpen, false, "Second Escape should close the evidence panel after the top hover card is gone.");

    console.log(`STACKED_POPOVER_BROWSER_OK first_escape=mini_map_only second_escape=panel_closed url=${pageUrl}`);
    console.log(`STACKED_POPOVER_BROWSER_JSON ${JSON.stringify({ ok: true, route: routePath, firstEscape: afterFirstEscape, secondEscape: afterSecondEscape })}`);
  } catch (error) {
    console.error(`STACKED_POPOVER_BROWSER_FAIL ${error.message}`);
    if (next) console.error(`next_tail:\n${next.outputTail()}`);
    if (chrome) console.error(`chrome_tail:\n${chrome.outputTail()}`);
    process.exitCode = 1;
  } finally {
    cdp?.close();
    await stopChild(chrome, "chrome");
    await stopChild(next, "next");
    for (let i = 0; i < 8; i += 1) {
      try {
        fs.rmSync(chromeProfile, { recursive: true, force: true });
        break;
      } catch (cleanupError) {
        if (i === 7) console.warn(`chrome_profile_cleanup_warning ${cleanupError.message}`);
        await sleep(250);
      }
    }
  }
}

await main();
