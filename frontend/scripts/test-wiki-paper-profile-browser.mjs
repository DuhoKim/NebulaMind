import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import net from "node:net";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const nextPort = Number(process.env.WIKI_PAPER_PROFILE_NEXT_PORT || 3034);
const chromePort = Number(process.env.WIKI_PAPER_PROFILE_CHROME_PORT || 9244);
const baseUrl = process.env.WIKI_PAPER_PROFILE_BASE_URL || `http://127.0.0.1:${nextPort}`;
const chromeBinary = process.env.CHROME_BIN || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const STARTUP_TIMEOUT_MS = 45_000;
const SELECTOR_TIMEOUT_MS = 35_000;
const CDP_COMMAND_TIMEOUT_MS = 45_000;
const SCHEMA_VERSION = "paper_profile_browser.v1";
const scenarioFilter = (process.env.WIKI_PAPER_PROFILE_ONLY || "paper-profile-journey")
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean);
assert.ok(scenarioFilter.includes("paper-profile-journey"), `No paper-profile browser scenario selected by WIKI_PAPER_PROFILE_ONLY=${process.env.WIKI_PAPER_PROFILE_ONLY || ""}`);

function readFixtureOutput() {
  const fixturePath = process.env.WIKI_PAPER_PROFILE_BROWSER_FIXTURE_OUTPUT;
  if (!fixturePath) return false;
  const output = fs.readFileSync(fixturePath, "utf8");
  if (output.trim()) console.log(output.trim());
  const jsonLine = output.split(/\r?\n/).find((line) => line.startsWith("PAPER_PROFILE_BROWSER_JSON "));
  if (!jsonLine) process.exit(1);
  const parsed = JSON.parse(jsonLine.slice("PAPER_PROFILE_BROWSER_JSON ".length));
  process.exit(parsed?.ok === true ? 0 : 1);
}
readFixtureOutput();

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
  child.outputTail = () => output.join("").split(/\r?\n/).slice(-30).join("\n");
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
      if (masked) payload = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
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
    const header = [0x81];
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
    if (result.exceptionDetails) throw new Error(`Runtime.evaluate exception: ${JSON.stringify(result.exceptionDetails)}`);
    return result.result?.value;
  }

  close() {
    this.socket?.end();
  }
}

const paperProfileJourneyScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const text = (el) => el?.textContent?.replace(/\s+/g, ' ').trim() || '';
  const state = () => ({
    path: location.pathname,
    directoryCards: document.querySelectorAll('[data-testid="global-paper-card"]').length,
    profileLinks: document.querySelectorAll('[data-testid="global-paper-profile-link"]').length,
    profileDetail: Boolean(document.querySelector('[data-testid="paper-profile-detail"]')),
    pageCards: document.querySelectorAll('[data-testid="paper-profile-page-card"]').length,
    claimRows: document.querySelectorAll('[data-testid="paper-profile-claim-row"]').length,
    loading: document.body.textContent?.includes('Loading paper profile') || false,
    errorText: text(document.querySelector('[data-testid="paper-profile-error"]')),
    caveatText: text(document.querySelector('[data-testid="paper-profile-scope-caveat"]')),
    statusText: text(document.querySelector('[data-testid="paper-profile-status-chip"]')),
    headingText: text(document.querySelector('h1')),
  });
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelector('[data-testid="global-paper-directory"]'), 'global paper directory shell');
  await waitFor(() => document.querySelectorAll('[data-testid="global-paper-card"]').length > 0, 'global paper cards');
  await waitFor(() => document.querySelectorAll('[data-testid="global-paper-profile-link"]').length > 0, 'global paper profile links');
  const link = document.querySelector('[data-testid="global-paper-profile-link"]');
  const profileHref = link.getAttribute('href') || '';
  const profileAriaLabel = link.getAttribute('aria-label') || '';
  const directoryCardsBeforeNavigation = document.querySelectorAll('[data-testid="global-paper-card"]').length;
  link.scrollIntoView({ block: 'center', inline: 'center' });
  link.focus();
  link.click();

  await waitFor(() => location.pathname.startsWith('/wiki/papers/') && location.pathname !== '/wiki/papers', 'client navigation to dynamic profile route');
  await waitFor(() => document.querySelector('[data-testid="paper-profile-detail"]'), 'paper profile detail shell');
  await waitFor(() => !state().loading && !state().errorText && state().pageCards > 0 && state().claimRows > 0, 'API-backed paper profile rows');
  await waitFor(() => /not a final verdict/i.test(state().caveatText) && /No labels are written/i.test(state().caveatText), 'truth/read-only framing copy');

  const final = state();
  return {
    ...final,
    profileHref,
    profileAriaLabel,
    profileId: decodeURIComponent(profileHref.replace(/^\/wiki\/papers\//, '')),
    directoryCardsBeforeNavigation,
    truthFraming: /not a final verdict/i.test(final.caveatText),
    readOnlyFraming: /No labels are written/i.test(final.caveatText),
    directoryLinkVisible: Boolean(document.querySelector('[data-testid="paper-profile-directory-link"]')),
    backlinkVisible: Boolean(document.querySelector('[data-testid="paper-profile-backlink"]')),
  };
})()`;

async function waitForPageReady(cdp, routePath) {
  await waitFor(async () => {
    try {
      const ready = await cdp.evaluate(`(() => ({ href: location.href, readyState: document.readyState }))()`);
      return ready && ready.href.includes(routePath) && ready.readyState !== "loading";
    } catch {
      return false;
    }
  }, STARTUP_TIMEOUT_MS, `Chrome page navigation to stabilize for ${routePath}`);
}

function assertPaperProfileJourney(result) {
  assert.ok(result.directoryCardsBeforeNavigation > 0, "Directory should render at least one paper card before profile navigation.");
  assert.ok(result.profileHref.startsWith("/wiki/papers/"), "Directory profile link should point at the dynamic paper profile route.");
  assert.notEqual(result.profileHref, "/wiki/papers/profile-fixture", "Browser journey should use an API-backed dynamic profile, not the static fixture route.");
  assert.ok(result.profileId && result.profileId !== "profile-fixture", "Profile id should be derived from the clicked directory link.");
  assert.ok(result.path.startsWith("/wiki/papers/"), "Browser should navigate to a dynamic paper profile route.");
  assert.ok(result.profileDetail, "Profile detail wrapper should render after navigation.");
  assert.ok(result.pageCards > 0, "Dynamic profile should render at least one page footprint card.");
  assert.ok(result.claimRows > 0, "Dynamic profile should render at least one claim footprint row.");
  assert.ok(result.statusText, "Dynamic profile should render a status chip.");
  assert.equal(result.truthFraming, true, "Dynamic profile should visibly say it is not a final verdict.");
  assert.equal(result.readOnlyFraming, true, "Dynamic profile should visibly say no labels are written.");
  assert.equal(result.errorText, "", "Dynamic profile should not show the retry/error state.");
  assert.equal(result.directoryLinkVisible, true, "Profile should expose a return link to the paper directory.");
  assert.equal(result.backlinkVisible, true, "Profile should expose a wiki index backlink.");
}

async function runPaperProfileJourney() {
  const routePath = "/wiki/papers";
  const pageUrl = new URL(routePath, baseUrl).toString();
  const chromeProfile = path.join(os.tmpdir(), `nebulamind-paper-profile-chrome-${process.pid}`);
  let chrome;
  let cdp;
  fs.rmSync(chromeProfile, { recursive: true, force: true });
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
    const target = await waitFor(async () => {
      const pages = await requestJson(`http://127.0.0.1:${chromePort}/json/list`);
      return pages.find((page) => page.type === "page" && page.webSocketDebuggerUrl);
    }, STARTUP_TIMEOUT_MS, "Chrome DevTools target for paper-profile journey");
    cdp = new CdpClient(target.webSocketDebuggerUrl);
    await cdp.connect();
    await cdp.command("Runtime.enable");
    await cdp.command("Page.enable");
    await waitForPageReady(cdp, routePath);
    const result = await cdp.evaluate(paperProfileJourneyScript);
    assertPaperProfileJourney(result);
    const route = result.path;
    const summary = {
      schemaVersion: SCHEMA_VERSION,
      generatedAt: new Date().toISOString(),
      ok: true,
      case: {
        name: "paper-profile-journey",
        ok: true,
        route,
        url: new URL(route, baseUrl).toString(),
        profileId: result.profileId,
        profileHref: result.profileHref,
        profileAriaLabel: result.profileAriaLabel,
        directoryCards: result.directoryCardsBeforeNavigation,
        pageCards: result.pageCards,
        claimRows: result.claimRows,
        statusText: result.statusText,
        headingText: result.headingText,
        truthFraming: result.truthFraming,
        readOnlyFraming: result.readOnlyFraming,
      },
    };
    console.log(`PAPER_PROFILE_BROWSER_OK profile_id=${summary.case.profileId} route=${summary.case.route} page_cards=${summary.case.pageCards} claim_rows=${summary.case.claimRows}`);
    console.log(`PAPER_PROFILE_BROWSER_JSON ${JSON.stringify(summary)}`);
    return summary;
  } catch (error) {
    console.error(`PAPER_PROFILE_BROWSER_FAIL ${error.message}`);
    if (chrome) console.error(`chrome_tail_paper_profile:\n${chrome.outputTail()}`);
    throw error;
  } finally {
    cdp?.close();
    await stopChild(chrome, "chrome paper-profile");
    for (let i = 0; i < 8; i += 1) {
      try {
        fs.rmSync(chromeProfile, { recursive: true, force: true });
        break;
      } catch (cleanupError) {
        if (i === 7) console.warn(`chrome_profile_cleanup_warning paper-profile ${cleanupError.message}`);
        await sleep(250);
      }
    }
  }
}

async function main() {
  assert.ok(fs.existsSync(path.join(frontendRoot, ".next", "BUILD_ID")), "Run npm run build before smoke:wiki-paper-profile-browser so next start can serve a production build.");
  assert.ok(fs.existsSync(chromeBinary), `Chrome binary not found at ${chromeBinary}; set CHROME_BIN to override.`);
  const next = process.env.WIKI_PAPER_PROFILE_BASE_URL
    ? null
    : spawnLogged("npm", ["run", "start", "--", "-p", String(nextPort)], { cwd: frontendRoot });
  try {
    await runPaperProfileJourney();
  } catch (error) {
    if (next) console.error(`next_tail:\n${next.outputTail()}`);
    process.exitCode = 1;
  } finally {
    await stopChild(next, "next");
  }
}

await main();
