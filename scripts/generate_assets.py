"""Generates every SVG for the GitHub profile README. Run from the repo root: python scripts/generate_assets.py ."""
import sys, os
from xml.sax.saxutils import escape

ROOT = sys.argv[1]
A = os.path.join(ROOT, "assets")
for d in ["", "project-thumbnails", "architecture", "dividers", "links"]:
    os.makedirs(os.path.join(A, d), exist_ok=True)

BG, PANEL, LINE, TEXT, MUTED = "#050A14", "#0B1628", "#1E2D45", "#E6EDF7", "#8A9BB5"
BLUE, CYAN, RED = "#2F81F7", "#22D3EE", "#F43F5E"
FONT = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"


def write(rel, body):
    with open(os.path.join(A, rel), "w", encoding="utf-8", newline="\n") as f:
        f.write(body.strip() + "\n")


def svg(w, h, inner, title, extra_style=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">
<title id="t">{escape(title)}</title>
<style>text{{font-family:{FONT}}}{extra_style}</style>
{inner}
</svg>'''


def arrow_defs(idn="a"):
    return f'''<defs>
<marker id="{idn}b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{BLUE}"/></marker>
<marker id="{idn}c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{CYAN}"/></marker>
<marker id="{idn}r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{RED}"/></marker>
</defs>'''


def node(x, y, w, h, label, sub=None, kind="n"):
    stroke = {"n": LINE, "hi": BLUE, "guard": RED, "out": CYAN}[kind]
    sw = 1.5 if kind == "n" else 2
    fill = PANEL if kind != "out" else "#0A2230"
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    cy = y + h / 2 + (6 if not sub else -3)
    s += f'<text x="{x + w/2}" y="{cy}" text-anchor="middle" font-size="17" font-weight="600" fill="{TEXT}">{escape(label)}</text>'
    if sub:
        s += f'<text x="{x + w/2}" y="{y + h/2 + 17}" text-anchor="middle" font-size="13" fill="{MUTED}">{escape(sub)}</text>'
    return s


def edge(x1, y1, x2, y2, color="b", dash=False, idn="a"):
    c = {"b": BLUE, "c": CYAN, "r": RED}[color]
    d = ' stroke-dasharray="5 5"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="1.8"{d} marker-end="url(#{idn}{color})"/>'


def path(dstr, color="c", dash=True, idn="a"):
    c = {"b": BLUE, "c": CYAN, "r": RED}[color]
    d = ' stroke-dasharray="5 5"' if dash else ""
    return f'<path d="{dstr}" fill="none" stroke="{c}" stroke-width="1.8"{d} marker-end="url(#{idn}{color})"/>'


def caption(text, x=24, y=36):
    return f'<text x="{x}" y="{y}" font-size="15" fill="{MUTED}">{escape(text)}</text>'


def frame(w, h):
    return f'<rect width="{w}" height="{h}" rx="16" fill="{BG}"/><rect x="0.75" y="0.75" width="{w-1.5}" height="{h-1.5}" rx="15.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>'


TW, TH = 600, 300  # every project thumbnail

# ---------------------------------------------------------------- hero banner
hero_nodes = [  # (x, y, label, kind)
    (690, 150, "task", "n"),
    (810, 90, "plan", "hi"),
    (930, 60, "retrieve", "n"),
    (930, 170, "tools", "n"),
    (1050, 115, "verify", "guard"),
    (1050, 235, "act", "out"),
]
hero_edges = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
NW, NH = 96, 40
anim = ""
for i in range(len(hero_nodes)):
    anim += f".n{i}{{animation:glow 6s ease-in-out {i*0.7:.1f}s infinite}}"
style = ("@keyframes glow{0%,100%{opacity:.15}12%{opacity:1}30%{opacity:.15}}" + anim +
         "@media (prefers-reduced-motion:reduce){[class^=n]{animation:none;opacity:.35}}")
inner = frame(1200, 340) + arrow_defs("h")
inner += '<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#16243A"/></pattern></defs>'
inner += '<rect x="620" y="16" width="564" height="308" rx="12" fill="url(#dots)"/>'
inner += f'<text x="56" y="128" font-size="62" font-weight="700" letter-spacing="-1.5" fill="{TEXT}">Mokshit Sharma</text>'
inner += f'<text x="58" y="172" font-size="24" font-weight="600" fill="{CYAN}">AI/ML Engineer · Agentic AI Developer</text>'
inner += f'<text x="58" y="222" font-size="19" fill="{TEXT}">Intelligent systems that show their work.</text>'
inner += f'<text x="58" y="276" font-size="15" fill="{MUTED}">Indore, Madhya Pradesh, India</text>'
for a, b in hero_edges:
    x1, y1 = hero_nodes[a][0] + NW, hero_nodes[a][1] + NH / 2
    x2, y2 = hero_nodes[b][0], hero_nodes[b][1] + NH / 2
    col = "r" if hero_nodes[b][3] == "guard" else "b"
    if a == 4 and b == 5:  # vertical: verify down to act
        x1, y1, x2, y2 = hero_nodes[a][0] + NW / 2, hero_nodes[a][1] + NH, hero_nodes[b][0] + NW / 2, hero_nodes[b][1]
        col = "c"
    inner += edge(x1, y1, x2 - 2 if a != 4 else x2, y2 - 2 if a == 4 else y2, col, idn="h")
for i, (x, y, label, kind) in enumerate(hero_nodes):
    c = {"n": BLUE, "hi": BLUE, "guard": RED, "out": CYAN}[kind]
    inner += f'<rect class="n{i}" x="{x-5}" y="{y-5}" width="{NW+10}" height="{NH+10}" rx="14" fill="none" stroke="{c}" stroke-width="2"/>'
    inner += node(x, y, NW, NH, label, kind=kind)
inner += f'<text x="1098" y="300" text-anchor="middle" font-size="12" fill="{MUTED}">nothing acts unverified</text>'
write("hero-banner.svg", svg(1200, 340, inner,
      "Mokshit Sharma, AI/ML Engineer and Agentic AI Developer, Indore. An agent graph: task, plan, retrieve and tools, a verify step, then act.", style))

# ---------------------------------------------------------------- photo placeholder
inner = f'''<rect width="400" height="400" rx="40" fill="{PANEL}"/>
<rect x="2" y="2" width="396" height="396" rx="38" fill="none" stroke="{LINE}" stroke-width="4"/>
<circle cx="200" cy="200" r="138" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="4 10"/>
<circle cx="200" cy="62" r="7" fill="{CYAN}"/>
<text x="200" y="228" text-anchor="middle" font-size="96" font-weight="700" letter-spacing="-3" fill="{TEXT}">MS</text>
<text x="200" y="300" text-anchor="middle" font-size="18" fill="{MUTED}">Photo coming soon</text>'''
write("profile-photo-placeholder.svg", svg(400, 400, inner, "Profile photo placeholder for Mokshit Sharma"))

# ---------------------------------------------------------------- divider
inner = f'''<line x1="0" y1="12" x2="560" y2="12" stroke="{LINE}" stroke-width="1.5"/>
<line x1="640" y1="12" x2="1200" y2="12" stroke="{LINE}" stroke-width="1.5"/>
<circle cx="580" cy="12" r="4" fill="{BLUE}"/><circle cx="600" cy="12" r="4" fill="{RED}"/><circle cx="620" cy="12" r="4" fill="{CYAN}"/>'''
write("dividers/divider.svg", svg(1200, 24, inner, "Section divider"))

# ---------------------------------------------------------------- current focus
rows = [("Agents and LLMs", ["Agentic AI", "Multi-agent architectures", "LLM applications", "RAG pipelines"], BLUE),
        ("ML and systems", ["Machine learning", "Data science", "AI engineering", "System design"], CYAN)]
inner = frame(1200, 250)
for r, (label, items, col) in enumerate(rows):
    y = 40 + r * 100
    inner += f'<text x="40" y="{y+43}" font-size="16" font-weight="600" fill="{col}">{label}</text>'
    for i, it in enumerate(items):
        x = 240 + i * 232
        inner += f'<rect x="{x}" y="{y}" width="212" height="70" rx="12" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>'
        inner += f'<rect x="{x}" y="{y+18}" width="4" height="34" rx="2" fill="{col}"/>'
        inner += f'<text x="{x+24}" y="{y+42}" font-size="17" font-weight="600" fill="{TEXT}">{escape(it)}</text>'
write("current-focus.svg", svg(1200, 250, inner,
      "Current focus. Agents and LLMs: agentic AI, multi-agent architectures, LLM applications, RAG pipelines. ML and systems: machine learning, data science, AI engineering, system design."))


# ---------------------------------------------------------------- project thumbnails
def thumb(name, title, cap, body):
    write(f"project-thumbnails/{name}.svg", svg(TW, TH, frame(TW, TH) + arrow_defs() + caption(cap) + body, title))


W, H = 165, 58
# SettleAI: snake with guard and deny branch
b = node(20, 66, W, H, "Signed mandate", "human authorises agent")
b += node(217, 66, W, H, "Scoping agent", "milestones + proof")
b += node(414, 66, W, H, "Proof checks", "rules + vision AI")
b += node(414, 188, W, H, "Mandate Guard", "deterministic", "guard")
b += node(217, 188, W, H, "PayPal payout", "or refund")
b += node(20, 188, W, H, "Signed receipt", "verifies offline", "out")
b += edge(185, 95, 215, 95) + edge(382, 95, 412, 95) + edge(496, 124, 496, 186, "r")
b += edge(414, 217, 384, 217) + edge(217, 217, 187, 217, "c")
b += f'<text x="579" y="272" text-anchor="end" font-size="13" fill="{RED}">out of mandate: denied, no money moves</text>'
thumb("settleai", "SettleAI flow: signed mandate, scoping agent, proof checks, Mandate Guard, PayPal payout, signed receipt",
      "Escrow for work AI agents hire people to do", b)

# docIQ
b = node(20, 66, W, H, "Upload", "contracts, invoices")
b += node(217, 66, W, H, "Parse + chunk", "per-workspace config")
b += node(414, 66, W, H, "Embed", "Gemini or local")
b += node(414, 188, W, H, "Retrieve", "vector or hybrid", "hi")
b += node(217, 188, W, H, "Grounded answer", "refuses out of scope")
b += node(20, 188, W, H, "Citations", "+ risk clauses", "out")
b += edge(185, 95, 215, 95) + edge(382, 95, 412, 95) + edge(496, 124, 496, 186)
b += edge(414, 217, 384, 217) + edge(217, 217, 187, 217, "c")
thumb("dociq", "docIQ RAG pipeline: upload, parse and chunk, embed, retrieve, grounded answer, citations",
      "RAG over your documents, answers cited to source", b)

# ToolForge: two rows of 4 with feedback loops
W2 = 128
xs = [16, 164, 312, 460]
r1 = [("OpenAPI spec", None, "n"), ("Design", "LLM picks tools", "hi"), ("Check plan", None, "n"), ("Human review", None, "guard")]
r2 = [("Scorecard", None, "out"), ("Security audit", None, "n"), ("Live test", "agent vs real API", "hi"), ("Generate", "+ validate", "n")]
b = ""
for x, (l, s, k) in zip(xs, r1):
    b += node(x, 66, W2, 50, l, s, k)
for x, (l, s, k) in zip(xs, r2):
    b += node(x, 196, W2, 50, l, s, k)
b += edge(144, 91, 162, 91) + edge(292, 91, 310, 91) + edge(440, 91, 458, 91)
b += edge(524, 116, 524, 194) + edge(460, 221, 442, 221) + edge(312, 221, 294, 221) + edge(164, 221, 146, 221, "c")
b += path("M 376 196 C 376 156, 228 160, 228 120")  # test -> design loop
b += path("M 376 66 C 376 40, 234 40, 230 63")      # check -> design loop
b += f'<text x="300" y="285" text-anchor="middle" font-size="12" fill="{CYAN}">dashed: design problems go back to the designer</text>'
thumb("toolforge", "ToolForge LangGraph flow: OpenAPI spec, design, check plan, human review, generate and validate, live test, security audit, scorecard, with feedback loops to design",
      "OpenAPI spec in, tested and audited MCP server out", b)

# Naman
b = node(20, 66, W, H, "“Jarvis”", "offline wake word")
b += node(217, 66, W, H, "Speech to text", "Groq")
b += node(414, 66, W, H, "Router", "skill packs")
b += node(414, 188, W, H, "LangGraph agent", "memory, tasks", "hi")
b += node(217, 188, W, H, "Approval step", "asks before risk", "guard")
b += node(20, 188, W, H, "Tools", "laptop, jobs, MCP", "out")
b += edge(185, 95, 215, 95) + edge(382, 95, 412, 95) + edge(496, 124, 496, 186)
b += edge(414, 217, 384, 217, "r") + edge(217, 217, 187, 217, "c")
thumb("naman", "Naman voice assistant: wake word, speech to text, router, LangGraph agent, approval step, tools",
      "Voice agent for Windows and Telegram", b)

# System Design Atlas: request path with animated pulse (the site's own core feature)
pts = [(16, "Rider app"), (164, "API gateway"), (312, "Ride service"), (460, "Driver match")]
b = ""
for x, l in pts:
    b += node(x, 100, 128, 50, l)
b += node(312, 200, 128, 50, "Surge pricing", "per map cell", "hi") + node(460, 200, 128, 50, "Location store", None, "out")
b += edge(144, 125, 162, 125) + edge(292, 125, 310, 125) + edge(440, 125, 458, 125)
b += edge(376, 150, 376, 198) + edge(524, 150, 524, 198, "c")
b += f'''<circle r="6" fill="{CYAN}"><animateMotion dur="4s" repeatCount="indefinite" path="M 80 125 L 524 125 L 524 225"/></circle>
<text x="30" y="235" font-size="13" fill="{MUTED}">Send request:</text><text x="30" y="255" font-size="13" fill="{MUTED}">watch it travel</text>'''
thumb("system-design-atlas", "System Design Atlas: an interactive diagram where a request travels from rider app through gateway and services",
      "Interactive system design tutorials", b)

# Customer churn XAI
b = node(20, 66, W, H, "Telco data", "~7K customers")
b += node(217, 66, W, H, "XGBoost", "churn risk")
b += node(414, 66, W, H, "SHAP", "TreeExplainer", "hi")
b += node(414, 188, W, H, "Reasons", "plain language")
b += node(217, 188, W, H, "Actions", "retention offers", "out")
b += node(20, 188, W, H, "Streamlit", "live dashboard")
b += edge(185, 95, 215, 95) + edge(382, 95, 412, 95) + edge(496, 124, 496, 186)
b += edge(414, 217, 384, 217, "c") + edge(217, 217, 187, 217)
thumb("churn-xai", "Customer churn with explainable AI: telco data, XGBoost, SHAP, plain-language reasons, retention actions, Streamlit dashboard",
      "Predicts churn and explains why", b)

# ---------------------------------------------------------------- Movigo architecture (high level, no internals)
inner = frame(1200, 400) + arrow_defs("m")
inner += caption("Movigo: live B2B intra-city logistics marketplace, Indore. High-level view; the codebase is private.", 32, 40)
inner += node(40, 90, 200, 60, "Retailer apps", "book deliveries")
inner += node(40, 170, 200, 60, "Driver app", "accept and deliver")
inner += node(40, 280, 200, 60, "Inbound support calls")
inner += f'<rect x="330" y="72" width="560" height="176" rx="14" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="6 6"/>'
inner += f'<text x="350" y="98" font-size="14" font-weight="600" fill="{BLUE}">Core platform, built from zero</text>'
inner += node(350, 120, 160, 60, "Bookings")
inner += node(530, 120, 160, 60, "Dispatch", "driver availability", "hi")
inner += node(710, 120, 160, 60, "Surge pricing", "ML model", "hi")
inner += f'<text x="610" y="222" text-anchor="middle" font-size="13" fill="{MUTED}">code review: work from 2 full-stack engineers and AI coding tools</text>'
inner += node(530, 280, 180, 60, "AI voice agent", "~81% resolved", "out")
inner += node(960, 280, 200, 60, "Human support", "the rest")
inner += node(960, 120, 200, 60, "Deliveries", "across Indore", "out")
inner += edge(240, 120, 348, 145, idn="m") + path("M 240 200 H 610 V 184", "b", dash=False, idn="m")
inner += edge(510, 150, 528, 150, idn="m") + edge(690, 150, 708, 150, idn="m") + edge(870, 150, 958, 150, "c", idn="m")
inner += edge(240, 310, 528, 310, idn="m") + edge(710, 310, 958, 310, "r", dash=True, idn="m")
inner += f'<text x="834" y="300" text-anchor="middle" font-size="12" fill="{RED}">escalate</text>'
write("architecture/movigo.svg", svg(1200, 400, inner,
      "Movigo high-level architecture: retailer and driver apps feed a core platform of bookings, dispatch and an ML surge-pricing model; an AI voice agent resolves about 81% of support calls and escalates the rest."))

# ---------------------------------------------------------------- link chips
chips = {
    "portfolio": ("Portfolio", f'<circle cx="26" cy="22" r="9" fill="none" stroke="{CYAN}" stroke-width="2"/><ellipse cx="26" cy="22" rx="4" ry="9" fill="none" stroke="{CYAN}" stroke-width="1.6"/><line x1="17" y1="22" x2="35" y2="22" stroke="{CYAN}" stroke-width="1.6"/>'),
    "linkedin": ("LinkedIn", f'<rect x="17" y="13" width="18" height="18" rx="4" fill="{CYAN}"/><text x="26" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="{BG}">in</text>'),
    "github": ("GitHub", f'<circle cx="21" cy="14" r="3" fill="none" stroke="{CYAN}" stroke-width="2"/><circle cx="21" cy="30" r="3" fill="none" stroke="{CYAN}" stroke-width="2"/><circle cx="32" cy="18" r="3" fill="none" stroke="{CYAN}" stroke-width="2"/><path d="M21 17v10M32 21c0 5-11 3-11 6" fill="none" stroke="{CYAN}" stroke-width="2"/>'),
    "email": ("Email", f'<rect x="16" y="15" width="20" height="14" rx="2" fill="none" stroke="{CYAN}" stroke-width="2"/><path d="M17 16l9 7 9-7" fill="none" stroke="{CYAN}" stroke-width="1.8"/>'),
}
for key, (label, icon) in chips.items():
    inner = f'<rect x="1" y="1" width="150" height="42" rx="21" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>{icon}<text x="46" y="27" font-size="15" font-weight="600" fill="{TEXT}">{label}</text>'
    write(f"links/{key}.svg", svg(152, 44, inner, label))
print("ok")
