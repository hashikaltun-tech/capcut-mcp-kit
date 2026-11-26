"""Nurturing carousel: 'Slow is still moving'. Writes build/slide-0N.html; render with render.js."""
import os, re, json

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(OUT, "build"), exist_ok=True)
TOTAL = 3

def hl(s):
    return re.sub(r"\[(.+?)\]", r"<mark>\1</mark>", s)

CHECK = '<svg class="ck" viewBox="0 0 60 44"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#f2e600" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg class="arr" viewBox="0 0 90 30"><path d="M3 17 C25 13 52 13 84 15 M66 4 C72 9 78 12 85 15 C78 18 71 22 64 27" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CSS = """
:root{--bg:#2b1a10;--card:#36261c;--cream:#f7f5f2;--tan:#d6c6b2;--hl:#f2e600;--ink:#2b1a10}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:var(--bg);overflow:hidden}
body{position:relative;color:var(--cream);font-family:'Jost',sans-serif;-webkit-font-smoothing:antialiased}
.frame{position:absolute;inset:24px;border:2px solid rgba(247,245,242,.16);border-radius:14px}
.logo{position:absolute;left:94px;top:92px;width:112px}
.count{position:absolute;right:90px;top:94px;font-size:30px;font-weight:500;color:rgba(247,245,242,.7)}
.content{position:absolute;left:90px;right:90px;top:205px;bottom:175px;display:flex;flex-direction:column}
.content>*{flex:none}
.label{font-size:34px;font-weight:500;color:var(--tan);margin-bottom:18px}
h1{font-family:'Playfair Display',serif;font-weight:800;font-size:64px;line-height:1.2;letter-spacing:-.01em}
mark{background:var(--hl);color:var(--ink);border-radius:8px;padding:0 .14em;-webkit-box-decoration-break:clone;box-decoration-break:clone;white-space:nowrap}
.sub{text-wrap:balance;font-size:40px;font-weight:500;line-height:1.3;margin-top:22px}
.vis{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0}
.tease{position:absolute;left:90px;bottom:110px;display:flex;align-items:center;gap:22px;font-size:36px;font-weight:500;color:rgba(247,245,242,.72)}
.arr{width:86px;height:30px}
.ck{width:58px;height:42px}
.card{background:var(--card);border:2px solid rgba(247,245,242,.85);border-radius:22px}
.dash{border:3px dashed rgba(247,245,242,.35);border-radius:22px}
.big{font-family:'Playfair Display',serif;font-weight:900;color:#f3e9dc;line-height:1;font-variant-numeric:lining-nums}
/* slide 1 bars */
.bars{padding:44px 46px;display:flex;flex-direction:column;gap:40px}
.row .top{display:flex;justify-content:space-between;font-size:34px;font-weight:500;margin-bottom:14px}
.row .top span:last-child{color:var(--tan)}
.track{height:34px;border-radius:17px;background:rgba(247,245,242,.12);overflow:hidden}
.fill{height:100%;border-radius:17px}
/* two cards */
.two{display:flex;gap:40px;height:500px}
.two>div{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:18px}
.two .k{font-size:38px;font-weight:500;line-height:1.25}
/* timeline pills */
.pills{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.pill{display:flex;align-items:center;justify-content:space-between;padding:30px 36px;font-size:44px;font-weight:500}
.cap{text-align:center;font-family:'Playfair Display',serif;font-weight:700;font-size:48px;margin-top:40px}
/* stats */
.stats{display:flex;flex-direction:column;gap:22px}
.stat{display:flex;align-items:center;gap:34px;padding:22px 40px}
.stat .big{font-size:96px;width:190px;text-align:center}
.stat .t{font-size:40px;font-weight:500;line-height:1.2}
.foot{font-size:28px;color:rgba(247,245,242,.6);margin-top:18px}
/* equation */
.eq{display:flex;flex-direction:column;align-items:stretch;gap:12px}
.eq .card,.eq .res{padding:30px 40px;font-size:42px;font-weight:500;text-align:center}
.eq .op{text-align:center;font-family:'Playfair Display',serif;font-weight:800;font-size:60px;color:var(--hl);line-height:1}
.res{background:var(--hl);color:var(--ink);border-radius:22px;font-weight:600!important}
/* week */
.week{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.day{display:flex;flex-direction:column;align-items:center;gap:16px;padding:26px 0 24px}
.day .d{font-size:40px;font-weight:600}
.day .p{font-size:36px;color:var(--tan)}
.day .ck{width:54px;height:40px}
/* missed */
.miss{display:flex;gap:26px;height:420px}
.miss>div{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;text-align:center}
.miss .d{font-size:38px;font-weight:600}
.miss .p{font-size:36px}
.strike{font-size:34px;color:rgba(247,245,242,.45);text-decoration:line-through;text-decoration-thickness:3px}
/* cta */
.cta{background:var(--cream);color:var(--ink);border-radius:22px;padding:44px 48px;display:flex;flex-direction:column;gap:22px}
.cta p{font-size:40px;font-weight:500;line-height:1.3}
.cta .c{font-family:'Playfair Display',serif;font-weight:800;font-size:60px;line-height:1.15}
.cta mark{background:var(--hl)}
.media{border-radius:18px;overflow:hidden;border:2px solid rgba(247,245,242,.3);flex:1;min-height:0}
.media img{width:100%;height:100%;object-fit:cover;display:block}
.hole{flex:1;border-radius:18px;box-shadow:0 0 0 3000px var(--bg);outline:2px solid rgba(247,245,242,.3);outline-offset:-1px}
html.tr,html.tr body{background:transparent}
.frame,.logo,.count,.tease,h1,.label,.sub,.cap,.foot{position:relative;z-index:2}
.frame,.logo,.count,.tease{position:absolute}
.plan{background:var(--cream);color:var(--ink);border-radius:22px;padding:36px 44px;display:flex;flex-direction:column;gap:14px}
.plan h3{font-family:"Playfair Display",serif;font-weight:800;font-size:44px}
.plan .it{display:flex;align-items:center;gap:20px;font-size:36px;font-weight:500}
.box{width:44px;height:44px;border-radius:8px;background:#2f6fd6;display:flex;align-items:center;justify-content:center;flex:none}
.lbl{font-size:30px;color:#7a6656;font-weight:500;margin-top:6px}
.ig{display:flex;flex-direction:column;gap:34px}
.igr{display:grid;grid-template-columns:230px 1fr;align-items:center;gap:24px}
.igr .pace{font-family:"Playfair Display",serif;font-weight:800;font-size:52px;line-height:1.05}
.igr .pace small{display:block;font-family:Jost;font-weight:500;font-size:30px;color:var(--tan)}
.igb{height:92px;border-radius:16px;background:rgba(247,245,242,.12);position:relative}
.igf{height:100%;border-radius:14px;background:var(--cream);display:flex;align-items:center;justify-content:flex-end;padding-right:16px;gap:10px;font-size:38px;font-weight:600;color:var(--ink);white-space:nowrap;padding-right:22px}
.igf .ck{width:40px;height:30px}
"""

def row(name, val, frac, color):
    return (f'<div class="row"><div class="top"><span>{name}</span><span>{val}</span></div>'
            f'<div class="track"><div class="fill" style="width:{frac*100:.1f}%;background:{color}"></div></div></div>')



WCK = '<svg viewBox="0 0 60 44" style="width:28px;height:22px"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
X = '<svg class="ck" viewBox="0 0 60 44"><path d="M14 6 L46 38 M46 6 L14 38" fill="none" stroke="rgba(247,245,242,.45)" stroke-width="6" stroke-linecap="round"/></svg>'

S = {}
S[1] = dict(tease="Save this", body=f"""
<h1 style="font-size:80px">There's <span style="color:var(--hl)">NO</span> time limit to becoming a {hl('[Hafidh.]')}</h1>
<div class="sub">How long it takes at your pace:</div>
<div class="vis"><div class="ig"><div class="igr"><div class="pace">2 pages<small>a day</small></div><div class="igb"><div class="igf" style="width:44%">~10 months <svg class="ck" viewBox="0 0 60 44"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#2b1a10" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div></div><div class="igr"><div class="pace">1 page<small>a day</small></div><div class="igb"><div class="igf" style="width:55%">~20 months <svg class="ck" viewBox="0 0 60 44"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#2b1a10" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div></div><div class="igr"><div class="pace">½ page<small>a day</small></div><div class="igb"><div class="igf" style="width:76%">~3 years <svg class="ck" viewBox="0 0 60 44"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#2b1a10" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div></div><div class="igr"><div class="pace">5 lines<small>a day</small></div><div class="igb"><div class="igf" style="width:100%">~5 years <svg class="ck" viewBox="0 0 60 44"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#2b1a10" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div></div></div>
<div class="foot" style="margin-top:30px">604-page Mushaf, 15 lines a page, every day. Every pace gets there.</div></div>""")
S[2] = dict(tease="How to stay consistent", body=f"""
<h1 style="font-size:70px">1 year or 5 years, what matters is that you {hl('[stay consistent.]')}</h1>
<div class="sub">Pick the pace you can keep, even on your busiest day, and keep going inshallah.</div>
<div style="height:34px;flex:none"></div>
<div class="media" style="margin-bottom:24px"><img src="../desk.jpg"></div>""")
S[3] = dict(cls="tr", tease=None, body=f"""
<h1 style="font-size:66px">That's why I made the {hl('[Hifdh Planner,]')}</h1>
<div class="sub" style="margin-top:14px">so you can see what to memorize and revise every day, at your own pace.</div>
<div style="height:30px;flex:none"></div>
<div class="hole" id="vid" style="flex:1"></div>
<div class="cap" style="text-align:left;font-family:Jost;font-weight:500;font-size:42px;margin-top:28px">Comment <mark style="font-family:'Playfair Display';font-weight:800">PLANNER</mark> and I'll send you the link</div>
<div class="foot" style="font-size:30px;margin-top:10px">$16.99 one-time</div>""")
jobs = []
for n, s in S.items():
    tease = f'<div class="tease">{s["tease"]} {ARROW}</div>' if s["tease"] else ""
    html = f"""<!doctype html><html class="{s.get('cls','')}"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fonts/fonts.css"><style>{CSS}</style></head>
<body><div class="frame"></div><img class="logo" src="../logo.png"><div class="count">{n}/{TOTAL}</div>
<div class="content">{s['body']}</div>{tease}</body></html>"""
    f = f"build/nt-{n:02d}.html"
    open(os.path.join(OUT, f), "w").write(html)
    jobs.append(f)
json.dump(jobs, open(os.path.join(OUT, "build/nt.json"), "w"))
