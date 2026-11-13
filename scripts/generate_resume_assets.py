"""Résumé-style README assets: an at-a-glance strip, a projects-by-area chart (counted from README.md)
and one explainer card per featured project (what it is, how it works in three steps, the key result).

Run from the repo root:  python scripts/generate_resume_assets.py
Colours follow the hero banner: navy #050A14, cyan #22D3EE, blue #2F81F7, rose #F43F5E.
"""
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "assets"
BG, CARD, LINE, TEXT, DIM, CYAN, BLUE, ROSE = "#050A14", "#0B1628", "#1E2D45", "#E6EDF7", "#8A9BB5", "#22D3EE", "#2F81F7", "#F43F5E"
FONT = "font-family=\"'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif\""


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title, {chr(34): "&quot;"})}">'
            f'<title>{escape(title)}</title><g {FONT}>'
            f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/><rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="13.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>'
            f'{body}</g></svg>\n')


def t(x, y, s, size=16, fill=TEXT, weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + ([cur] if cur else [])


# ---------------------------------------------------------------- at a glance
def glance():
    tiles = [("Founding Engineer", "AI/ML at Movigo", "since Apr 2026, live B2B logistics", CYAN),
             ("3 internships", "data science and AI", "Kangaroo, Evoastra, Cognifyz", BLUE),
             (f"{count_projects()} public projects", "across 7 areas", "agents, ML, data, full-stack and more", CYAN),
             ("B.Tech + M.Tech", "AI and Data Science", "DAVV Indore, CGPA 8.2, 2028", BLUE)]
    w, h, pad, gap = 1200, 170, 24, 16
    tw = (w - 2 * pad - 3 * gap) / 4
    body = ""
    for i, (big, mid, small, col) in enumerate(tiles):
        x = pad + i * (tw + gap)
        body += f'<rect x="{x}" y="{pad}" width="{tw}" height="{h - 2 * pad}" rx="10" fill="{CARD}" stroke="{LINE}"/>'
        body += f'<rect x="{x}" y="{pad}" width="4" height="{h - 2 * pad}" rx="2" fill="{col}"/>'
        body += t(x + 22, pad + 44, big, 24, TEXT, 700) + t(x + 22, pad + 72, mid, 16, col, 600) + t(x + 22, pad + 100, small, 13, DIM)
    (A / "at-a-glance.svg").write_text(svg(w, h, body, "At a glance: Founding Engineer (AI/ML) at Movigo; 3 internships; "
                                           f"{count_projects()} public projects across 7 areas; B.Tech + M.Tech in AI and Data Science, DAVV Indore"), encoding="utf-8")


# ---------------------------------------------------------------- projects by area (counted from README.md)
AREAS = [("Agent systems", "agent-systems"), ("Production platforms", "production-platforms"), ("Full-stack and systems", "full-stack-and-systems"),
         ("Machine learning and XAI", "machine-learning-and-explainable-ai"), ("Data analysis and BI", "data-analysis-and-bi"),
         ("Computer vision", "computer-vision"), ("Automation tools", "automation-tools")]


def area_counts():
    """Distinct public repo links under each area heading of README.md (private projects have no link)."""
    md = (ROOT / "README.md").read_text(encoding="utf-8")
    parts = re.split(r"^#{2,3} ", md, flags=re.M)
    out = []
    for label, slug in AREAS:
        head = {"Machine learning and XAI": "Machine learning and explainable AI"}.get(label, label)
        block = next((x for x in parts if x.split("\n")[0].strip().endswith(head)), "")
        out.append((label, len(set(re.findall(r"(?:\]\(|href=\")(https://github\.com/Mokshitsharma/[^)#/\"]+)", block)))))
    return out


def count_projects():
    return sum(n for _, n in area_counts())


def by_area():
    rows = area_counts()
    w, top, rh = 1200, 64, 40
    h = top + rh * len(rows) + 30
    mx = max(n for _, n in rows)
    x0, x1 = 300, w - 90
    body = t(32, 40, "Public projects by area", 20, TEXT, 700) + t(w - 32, 40, f"{sum(n for _, n in rows)} in total", 15, DIM, 400, "end")
    for i, (label, n) in enumerate(rows):
        y = top + i * rh
        bw = (x1 - x0) * n / mx
        col = CYAN if i % 2 == 0 else BLUE
        body += t(32, y + 24, label, 16, TEXT, 600)
        body += f'<rect x="{x0}" y="{y + 8}" width="{x1 - x0}" height="22" rx="6" fill="{CARD}"/>'
        body += f'<rect x="{x0}" y="{y + 8}" width="{bw:.1f}" height="22" rx="6" fill="{col}"/>'
        body += t(x0 + bw + 12, y + 25, str(n), 16, TEXT, 700)
    (A / "projects-by-area.svg").write_text(svg(w, h, body, "Public projects by area: " + ", ".join(f"{l} {n}" for l, n in rows)), encoding="utf-8")


# ---------------------------------------------------------------- project explainer cards
CARDS = {
    "settleai": ("SettleAI", "Escrow for work that AI agents hire people to do",
                 ["An AI agent posts a job with a signed spending limit",
                  "AI checks the worker's photo proof against the job",
                  "A rule-based guard approves the PayPal payout, or blocks it"],
                 ["0 of 8", "bad proofs paid"], ["49 / 49", "tampering attempts caught"], ROSE),
    "toolforge": ("ToolForge", "Turns any OpenAPI spec into a tested MCP server",
                  ["An LLM designs the tools; you approve the plan",
                   "A tester agent calls the live API with every tool",
                   "A security audit and scorecard close every build"],
                  ["8 / 8", "live tests on PokéAPI"], ["100 / 100", "security score"], BLUE),
    "dociq": ("docIQ", "Ask your contracts and invoices, get cited answers",
              ["Upload contracts and invoices",
               "It finds the passages that answer your question",
               "Answers cite the source and flag risky clauses"],
              ["16 / 16", "end-to-end checks pass"], ["0 keys", "needed: runs offline"], CYAN),
    "naman": ("Naman", "Voice assistant plus a job-search agent team",
              ["Say \"Jarvis\": it opens apps, sets reminders, tracks tasks",
               "Agents find jobs, match them and draft applications",
               "Anything risky waits for your OK first"],
              ["8 agents", "running in parallel"], ["Free tiers", "only, no paid APIs"], BLUE),
    "system-design-atlas": ("System Design Atlas", "How apps like Uber, Netflix and IRCTC could be built",
                            ["Pick an app and read its design step by step",
                             "Watch a request travel through the system",
                             "Size it yourself with capacity calculators"],
                            ["6", "tutorials"], ["121", "platforms, 25 patterns"], CYAN),
    "churn-xai": ("Churn with explainable AI", "Who will leave, why, and what to do about it",
                  ["XGBoost scores each customer's churn risk",
                   "SHAP finds the reasons behind each score",
                   "Reasons become plain-language retention actions"],
                  ["~7K", "customers analysed"], ["Live", "Streamlit demo"], ROSE),
}


def card(key):
    name, line, steps, m1, m2, col = CARDS[key]
    w = 600
    wrapped = [wrap(x, 50) for x in steps]
    h = 132 + sum(26 + 22 * (len(ls) - 1) + 18 for ls in wrapped) + 92
    body = f'<rect x="0" y="0" width="{w}" height="6" rx="3" fill="{col}"/>'
    body += t(28, 52, name, 30, TEXT, 700) + t(28, 84, line, 17, DIM)
    y = 116
    for i, lines in enumerate(wrapped, 1):
        body += f'<circle cx="46" cy="{y + 14}" r="15" fill="{CARD}" stroke="{col}" stroke-width="2"/>' + t(46, y + 20, str(i), 15, col, 700, "middle")
        for j, ln in enumerate(lines):
            body += t(76, y + 20 + j * 22, ln, 17, TEXT)
        step_h = 26 + 22 * (len(lines) - 1) + 18
        if i < len(wrapped):
            body += f'<line x1="46" y1="{y + 30}" x2="46" y2="{y + step_h - 2}" stroke="{LINE}" stroke-width="2"/>'
        y += step_h
    for k, (big, small) in enumerate((m1, m2)):
        x = 28 + k * 280
        body += f'<rect x="{x}" y="{h - 92}" width="264" height="70" rx="10" fill="{CARD}" stroke="{LINE}"/>'
        body += t(x + 18, h - 58, big, 24, col if k == 0 else TEXT, 700) + t(x + 18, h - 35, small, 14, DIM)
    title = f"{name}: {line}. How it works: " + "; ".join(steps) + f". Result: {m1[0]} {m1[1]}, {m2[0]} {m2[1]}."
    (A / "project-cards").mkdir(exist_ok=True)
    (A / "project-cards" / f"{key}.svg").write_text(svg(w, h, body, title), encoding="utf-8")


if __name__ == "__main__":
    glance()
    by_area()
    for k in CARDS:
        card(k)
    print("projects by area:", area_counts())
