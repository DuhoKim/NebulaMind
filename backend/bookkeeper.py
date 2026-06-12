import os
import re
import json
from collections import defaultdict
from datetime import datetime

AGENTS_DIR = "/Users/duhokim/.openclaw/agents"
agents = ["hwao", "koon", "kun", "main", "tori"]

# Unified price matrix in USD per 1 Million tokens
# Rates sourced from official GCP & OpenAI 2026 API charts
PRICES_PER_M = {
    "claude-opus-4-7": {"input": 15.0, "output": 75.0, "name": "Claude 3.7 Opus"},
    "claude-opus-4-8": {"input": 15.0, "output": 75.0, "name": "Claude 3.8 Opus"},
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0, "name": "Claude 3.6 Sonnet"},
    "gemini-3.5-flash": {"input": 1.50, "output": 9.00, "name": "Gemini 3.5 Flash"},
    "gemini-3.1-pro-preview": {"input": 2.00, "output": 12.00, "name": "Gemini 3.1 Pro"},
    "gemini-2.5-pro": {"input": 1.25, "output": 10.00, "name": "Gemini 2.5 Pro"},
    "gemini-2.5-flash": {"input": 0.30, "output": 2.50, "name": "Gemini 2.5 Flash"},
    "gpt-5.5": {"input": 5.00, "output": 30.00, "name": "OpenAI GPT-5.5"},
    "gpt-5.4": {"input": 5.00, "output": 30.00, "name": "OpenAI GPT-5.4"},
}

# Structure to store aggregated data:
agent_data = defaultdict(lambda: {
    "models": defaultdict(lambda: {"input": 0, "output": 0, "total_tokens": 0, "cost": 0.0}),
    "detailed_rows": defaultdict(lambda: {"tokens": 0, "cost": 0.0}),
    "earliest_date": None,
    "latest_date": None
})

# Out-of-band GCP Backend Infrastructure cost from June 2, 2026
GCP_COSTS = {
    "agent": "GCP_BACKEND",
    "model": "gemini-3.1-pro-preview",
    "thinking_level": "high",
    "total_tokens": 114000000,
    "cost": 495.00,  # ₩682,000 KRW
    "earliest_date": datetime(2026, 6, 2),
    "latest_date": datetime(2026, 6, 2),
    "description": "NebulaMind automated paper evaluation pipeline (evaluate_entailment_gate_gemini)"
}

# We want to match files that are exactly <uuid>.jsonl or <custom-label>.jsonl but not trajectories, checkpoints, etc.
def is_valid_session_file(filename):
    if not filename.endswith(".jsonl"):
        return False
    for blacklist in [".trajectory", ".codex", ".checkpoint", ".deleted", ".reset", ".bak"]:
        if blacklist in filename:
            return False
    return True

print("Scanning OpenClaw sessions for deep grouped bookkeeping...")
for agent in agents:
    sessions_path = os.path.join(AGENTS_DIR, agent, "sessions")
    if not os.path.exists(sessions_path):
        continue
    
    # Map 'main' directly to 'HWAO' to match our core identity.
    # Obsolete agents 'koon' and 'hwao' are ignored or merged.
    mapped_agent_id = "HWAO" if agent in ["main", "hwao"] else agent.upper()
    if agent == "koon":
        continue # Prune completely obsolete koon agent
    
    files = [f for f in os.listdir(sessions_path) if is_valid_session_file(f)]
    for f in files:
        filepath = os.path.join(sessions_path, f)
        try:
            # Sourced directly from openclaw.json defaults:
            # HWAO/MAIN default is 'max', KUN is 'max', TORI is 'xhigh'
            if agent == "main":
                current_thinking_level = "max"
            elif agent == "kun":
                current_thinking_level = "max"
            elif agent == "tori":
                current_thinking_level = "xhigh"
            else:
                current_thinking_level = "off"
                
            session_start_date = None
            
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        line_type = data.get("type")
                        
                        if line_type == "session":
                            ts_str = data.get("timestamp")
                            if ts_str:
                                ts_str_clean = re.sub(r"\.\d+Z$", "Z", ts_str)
                                try:
                                    session_start_date = datetime.strptime(ts_str_clean, "%Y-%m-%dT%H:%M:%SZ")
                                except ValueError:
                                    try:
                                        session_start_date = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                                    except Exception:
                                        pass
                                        
                        elif line_type == "thinking_level_change":
                            current_thinking_level = data.get("thinkingLevel", "off")
                            if not current_thinking_level:
                                current_thinking_level = "off"
                                
                        elif line_type == "message":
                            msg = data.get("message", {})
                            model = msg.get("model")
                            usage = msg.get("usage", {})
                            if model and usage:
                                inp = usage.get("input", 0)
                                out = usage.get("output", 0)
                                tot = usage.get("totalTokens", 0)
                                cost_obj = usage.get("cost", {})
                                cost = cost_obj.get("total", 0.0)
                                
                                t_level = current_thinking_level
                                
                                if cost == 0.0 and model in PRICES_PER_M:
                                    rates = PRICES_PER_M[model]
                                    cost = (inp * (rates["input"] / 1e6)) + (out * (rates["output"] / 1e6))
                                
                                # Accumulate Agent-specific stats
                                agent_id = mapped_agent_id
                                agent_data[agent_id]["models"][model]["input"] += inp
                                agent_data[agent_id]["models"][model]["output"] += out
                                agent_data[agent_id]["models"][model]["total_tokens"] += tot
                                agent_data[agent_id]["models"][model]["cost"] += cost
                                
                                key = (model, t_level)
                                agent_data[agent_id]["detailed_rows"][key]["tokens"] += tot
                                agent_data[agent_id]["detailed_rows"][key]["cost"] += cost
                                
                                # Update agent date range
                                if session_start_date:
                                    cur_min = agent_data[agent_id]["earliest_date"]
                                    cur_max = agent_data[agent_id]["latest_date"]
                                    if cur_min is None or session_start_date < cur_min:
                                        agent_data[agent_id]["earliest_date"] = session_start_date
                                    if cur_max is None or session_start_date > cur_max:
                                        agent_data[agent_id]["latest_date"] = session_start_date
                    except Exception:
                        pass
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

# Add manual GCP Direct Billing Agent
gcp_id = GCP_COSTS["agent"]
agent_data[gcp_id]["models"][GCP_COSTS["model"]]["input"] += GCP_COSTS["total_tokens"]
agent_data[gcp_id]["models"][GCP_COSTS["model"]]["total_tokens"] += GCP_COSTS["total_tokens"]
agent_data[gcp_id]["models"][GCP_COSTS["model"]]["cost"] += GCP_COSTS["cost"]
key = (GCP_COSTS["model"], GCP_COSTS["thinking_level"])
agent_data[gcp_id]["detailed_rows"][key]["tokens"] += GCP_COSTS["total_tokens"]
agent_data[gcp_id]["detailed_rows"][key]["cost"] += GCP_COSTS["cost"]
agent_data[gcp_id]["earliest_date"] = GCP_COSTS["earliest_date"]
agent_data[gcp_id]["latest_date"] = GCP_COSTS["latest_date"]

# Read Active & Fallback Model configurations from openclaw.json
primary_configs = {}
fallback_configs = {}
try:
    with open("/Users/duhokim/.openclaw/openclaw.json", "r") as config_f:
        config_data = json.load(config_f)
        
        # Default global config
        defaults = config_data.get("agents", {}).get("defaults", {}).get("model", {})
        def_primary = defaults.get("primary", "N/A")
        def_fallbacks = defaults.get("fallbacks", [])
        
        # Populate defaults
        for agent_id in ["KUN", "TORI", "HWAO"]:
            primary_configs[agent_id] = def_primary
            fallback_configs[agent_id] = def_fallbacks
            
        # Parse individual list overrides
        agents_list = config_data.get("agents", {}).get("list", [])
        for a in agents_list:
            a_id = a.get("id", "").upper()
            if a_id == "MAIN":
                a_id = "HWAO" # Map 'main' agent directly to 'HWAO'
            if a_id == "KOON":
                continue # Skip obsolete koon config
            if a_id:
                m_cfg = a.get("model", {})
                primary_configs[a_id] = m_cfg.get("primary", def_primary)
                fallback_configs[a_id] = m_cfg.get("fallbacks", def_fallbacks)
except Exception as e:
    print(f"Error reading openclaw.json config: {e}")

# Helper to format token counts into Millions (M)
def format_m(tokens):
    return f"{tokens / 1e6:.2f}M" if tokens >= 10000 else f"{tokens:,}"

# Helper to format Date range nicely
def format_date_range(min_d, max_d):
    if min_d is None or max_d is None:
        return "N/A"
    if min_d.date() == max_d.date():
        return min_d.strftime("%Y-%m-%d")
    return f"{min_d.strftime('%Y-%m-%d')} ~ {max_d.strftime('%Y-%m-%d')}"

# Calculate Grand Totals
grand_total_tokens = 0
grand_total_cost = 0.0
for agent_id, data in agent_data.items():
    for model, stats in data["models"].items():
        grand_total_tokens += stats["total_tokens"]
        grand_total_cost += stats["cost"]

# Build report
markdown_lines = []
markdown_lines.append("# Unified Ecosystem Financial Bookkeeping Report")
markdown_lines.append("This report combines both local **OpenClaw Agent Platform** costs and external **NebulaMind Backend Infrastructure (GCP Direct Billing)** costs.")
markdown_lines.append("All statistics are grouped primarily by **Agent** and display the **Active Time Period** for each group. Token counts are compacted into millions (M) for clean readability.\n")
markdown_lines.append(f"Report generated dynamically on KST 2026-06-03.\n")

# Section 1: Executive Summary Table (Grouped by Agent)
markdown_lines.append("## 📊 Executive Summary Table (Grouped by Agent)")
markdown_lines.append("| Agent | Active Time Period | Primary Models | Compacted Tokens | Cost (USD) | Share (%) |")
markdown_lines.append("|---|---|---|---|---|---|")

agent_summary_rows = []
for agent_id, data in agent_data.items():
    tot_tokens = sum(stats["total_tokens"] for stats in data["models"].values())
    tot_cost = sum(stats["cost"] for stats in data["models"].values())
    
    if tot_tokens == 0 and tot_cost == 0:
        continue
        
    date_range_str = format_date_range(data["earliest_date"], data["latest_date"])
    
    # Identify top models
    top_models = sorted(data["models"].keys(), key=lambda m: data["models"][m]["cost"], reverse=True)
    primary_models_str = ", ".join([f"`{m}`" for m in top_models[:2]])
    
    agent_summary_rows.append({
        "agent": agent_id,
        "period": date_range_str,
        "primary_models": primary_models_str,
        "tokens": tot_tokens,
        "cost": tot_cost,
    })

# Sort agent rows by cost descending
agent_summary_rows.sort(key=lambda x: x["cost"], reverse=True)

for r in agent_summary_rows:
    share = (r["cost"] / grand_total_cost * 100) if grand_total_cost > 0 else 0.0
    markdown_lines.append(f"| **{r['agent']}** | {r['period']} | {r['primary_models']} | {format_m(r['tokens'])} | ${r['cost']:.2f} | {share:.1f}% |")

markdown_lines.append(f"| **GRAND TOTAL** | | | **{format_m(grand_total_tokens)}** | **${grand_total_cost:.2f}** | **100.0%** |")
markdown_lines.append("")

# Section 2: Agent Routing and Fallback Policies
markdown_lines.append("## 🛠️ Active Agent Routing & Fallback Policies")
markdown_lines.append("The active and fallback model configurations currently set inside `openclaw.json`:")
markdown_lines.append("")
markdown_lines.append("| Agent | Current Primary Model | Fallback Chain |")
markdown_lines.append("|---|---|---|")

for r in agent_summary_rows:
    a_id = r["agent"]
    primary = primary_configs.get(a_id, "N/A")
    fallbacks = fallback_configs.get(a_id, [])
    fb_str = " $\\rightarrow$ ".join([f"`{fb}`" for fb in fallbacks]) if fallbacks else "`None`"
    markdown_lines.append(f"| **{a_id}** | `{primary}` | {fb_str} |")
markdown_lines.append("")

# Section 3: Model Price List
markdown_lines.append("## 🏷️ Investigated Model Price List")
markdown_lines.append("The commercial rates (per 1 Million tokens) used to evaluate all token usage:")
markdown_lines.append("")
markdown_lines.append("| Model Identifier | Model Name | Input Price / 1M | Output Price / 1M |")
markdown_lines.append("|---|---|---|---|")

for m_id, r in sorted(PRICES_PER_M.items(), key=lambda x: x[1]["input"], reverse=True):
    markdown_lines.append(f"| `{m_id}` | {r['name']} | ${r['input']:.2f} | ${r['output']:.2f} |")
markdown_lines.append("")

# Section 4: Detailed Sub-Breakdown for Each Agent
markdown_lines.append("## 🔍 Detailed Sub-Breakdown by Agent")
markdown_lines.append("This section lists all models and thinking levels deployed under each agent during their active time periods:")
markdown_lines.append("")

for r in agent_summary_rows:
    agent_id = r["agent"]
    data = agent_data[agent_id]
    
    markdown_lines.append(f"### Agent Sector: {agent_id}")
    markdown_lines.append(f"* **Operational Period:** {r['period']}")
    markdown_lines.append(f"* **Sector Expenditure:** **${r['cost']:.2f}** ({r['cost']/grand_total_cost*100:.1f}% Share)")
    markdown_lines.append(f"* **Sector Volume:** **{format_m(r['tokens'])}** processed")
    markdown_lines.append("")
    markdown_lines.append("| Model | Thinking Level | Compacted Tokens | Cost (USD) | Note / Context |")
    markdown_lines.append("|---|---|---|---|---|")
    
    detailed = sorted(data["detailed_rows"].items(), key=lambda x: x[1]["cost"], reverse=True)
    for (model, t_level), stats in detailed:
        note = "GCP Direct Bill Event" if agent_id == "GCP_BACKEND" else "Agent Session Run"
        markdown_lines.append(f"| `{model}` | `{t_level}` | {format_m(stats['tokens'])} | ${stats['cost']:.2f} | {note} |")
    markdown_lines.append("")

# Section 5: Global Model Summary
markdown_lines.append("## Global Unified Expenditure by Model (Agents + GCP)")
markdown_lines.append("| Model | Total Tokens | Cost (USD) | Share (%) |")
markdown_lines.append("|---|---|---|---|")

model_totals = defaultdict(lambda: {"tokens": 0, "cost": 0.0})
for agent_id, data in agent_data.items():
    for model, stats in data["models"].items():
        model_totals[model]["tokens"] += stats["total_tokens"]
        model_totals[model]["cost"] += stats["cost"]

for model in sorted(model_totals.keys(), key=lambda m: model_totals[m]["cost"], reverse=True):
    tot = model_totals[model]["tokens"]
    cost = model_totals[model]["cost"]
    share = (cost / grand_total_cost * 100) if grand_total_cost > 0 else 0.0
    markdown_lines.append(f"| `{model}` | {format_m(tot)} | ${cost:.2f} | {share:.1f}% |")

markdown_lines.append(f"| **GRAND TOTAL** | **{format_m(grand_total_tokens)}** | **${grand_total_cost:.2f}** | **100.0%** |")

# Save file
report_path = "/Users/duhokim/.openclaw/workspace/memory/openclaw-expenditure-report.md"
os.makedirs(os.path.dirname(report_path), exist_ok=True)
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(markdown_lines))

print("Bookkeeping Report V4 (Fully Loaded) Compiled successfully!")
print(f"Saved to: {report_path}")
