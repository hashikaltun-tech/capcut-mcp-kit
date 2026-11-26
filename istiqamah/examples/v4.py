"""Nurturing carousel: 'Slow is still moving'. Writes build/slide-0N.html; render with render.js."""
import os, re, json

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(OUT, "build"), exist_ok=True)
TOTAL = 6

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
.frame,.logo,.count,.tease,h1,.label{position:relative;z-index:2}
.frame,.logo,.count,.tease{position:absolute}
.plan{background:var(--cream);color:var(--ink);border-radius:22px;padding:36px 44px;display:flex;flex-direction:column;gap:14px}
.plan h3{font-family:"Playfair Display",serif;font-weight:800;font-size:44px}
.plan .it{display:flex;align-items:center;gap:20px;font-size:36px;font-weight:500}
.box{width:44px;height:44px;border-radius:8px;background:#2f6fd6;display:flex;align-items:center;justify-content:center;flex:none}
.lbl{font-size:30px;color:#7a6656;font-weight:500;margin-top:6px}
"""

def row(name, val, frac, color):
    return (f'<div class="row"><div class="top"><span>{name}</span><span>{val}</span></div>'
            f'<div class="track"><div class="fill" style="width:{frac*100:.1f}%;background:{color}"></div></div></div>')



WCK = '<svg viewBox="0 0 60 44" style="width:28px;height:22px"><path d="M6 24 L22 38 L54 6" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
X = '<svg class="ck" viewBox="0 0 60 44"><path d="M14 6 L46 38 M46 6 L14 38" fill="none" stroke="rgba(247,245,242,.45)" stroke-width="6" stroke-linecap="round"/></svg>'
S = {}
S[1] = dict(cls="tr", tease="Let me explain", body=f"""
<div class="label" style="font-size:40px;color:var(--hl)">Unpopular opinion</div>
<h1 style="font-size:92px">Stop memorizing {hl('[2 pages a day.]')}</h1>
<div style="height:40px;flex:none"></div>
<div class="hole" id="vid" style="flex:none;height:560px;margin:auto 0"></div>""")
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
ok = [1,1,0,0,0,0,0]
S[2] = dict(tease="So what do you do?", body=f"""
<h1 style="font-size:70px">It works for one good week, then a busy week comes and you {hl('[drop all of it.]')}</h1>
<div class="vis"><div class="week">
{''.join(f'<div class="{"card" if o else "dash"} day"><div class="d">{d}</div><div class="p">2 pages</div>{CHECK if o else X}</div>' for d,o in zip(DAYS,ok))}
<div class="day" style="justify-content:center;text-align:center"><div class="p" style="font-size:34px;color:var(--cream)">It's not<br>you.</div></div>
</div></div>""")
S[3] = dict(tease="And stop waiting", body=f"""
<h1 style="font-size:92px">Do less. {hl('[Seriously.]')}</h1>
<div class="sub">Half a page every day, and you're still consistent.</div>
<div class="vis"><div class="stats">
<div class="card stat"><div class="big">½</div><div class="t">page a day</div></div>
<div class="card stat"><div class="big">15</div><div class="t">pages a month</div></div>
<div class="card stat"><div class="big">~6</div><div class="t">weeks for a whole Juz</div></div>
</div></div>""")
S[4] = dict(tease="One more thing", body=f"""
<h1 style="font-size:74px">Stop waiting for free time. Give your Hifdh {hl('[a set time.]')}</h1>
<div class="sub">Memorize after work and revise in your salah, so it's already part of your day.</div>
<div class="vis"><div class="stats">
<div class="card stat"><div class="big" style="font-size:72px;width:230px">5pm</div><div class="t">New memorization,<br>after work</div></div>
<div class="card stat"><div class="big" style="font-size:72px;width:230px">Salah</div><div class="t">Revision, in your prayers<br>and while you wait</div></div>
</div></div>""")
S[5] = dict(tease="Where to keep it", body=f"""
<h1 style="font-size:80px">If it's only in your head, {hl('[you’ll skip it.]')}</h1>
<div style="height:36px;flex:none"></div>
<div class="media" style="margin-bottom:24px"><img src="../desk.jpg"></div>""")
S[6] = dict(tease=None, body=f"""
<h1 style="font-size:66px">That's why I made the {hl('[Hifdh Planner,]')}</h1>
<div class="sub" style="margin-top:14px">so you can see what to memorize and revise every day and stay consistent inshallah.</div>
<div style="height:30px;flex:none"></div>
<div class="media"><img src="../desk2.jpg"></div>
<div class="cap" style="text-align:left;font-family:Jost;font-weight:500;font-size:42px;margin-top:28px">Comment <mark style="font-family:'Playfair Display';font-weight:800">PLANNER</mark> and I'll send you the link</div>
<div class="foot" style="font-size:30px;margin-top:10px">$16.99 one-time</div>""")
jobs = []
for n, s in S.items():
    tease = f'<div class="tease">{s["tease"]} {ARROW}</div>' if s["tease"] else ""
    html = f"""<!doctype html><html class="{s.get('cls','')}"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fonts/fonts.css"><style>{CSS}</style></head>
<body><div class="frame"></div><img class="logo" src="../logo.png"><div class="count">{n}/{TOTAL}</div>
<div class="content">{s['body']}</div>{tease}</body></html>"""
    f = f"build/v4-{n:02d}.html"
    open(os.path.join(OUT, f), "w").write(html)
    jobs.append(f)
json.dump(jobs, open(os.path.join(OUT, "build/v4.json"), "w"))
