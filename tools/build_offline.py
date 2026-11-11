"""Build AI-Study-Offline.html: the whole course in one file that opens without internet.
Usage: python3 tools/build_offline.py [out_path]"""
import json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'AI-Study-Offline.html')
idx = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
m = json.load(open(os.path.join(root, 'manifest.json'), encoding='utf-8'))
days = {}
for d in m['days']:
    p = os.path.join(root, 'days', f"day-{d['n']:03d}.html")
    if d['r'] and os.path.exists(p):
        days[d['n']] = open(p, encoding='utf-8').read()
    else:
        d['r'] = False
blob = json.dumps({'m': m, 'd': days}, ensure_ascii=False).replace('</', '<\\/')
a = "fetch('manifest.json',{cache:'no-cache'}).then(r=>r.json())"
b = "let html;\n  try{const r=await fetch('days/day-'+pad(n)+'.html',{cache:'no-cache'});if(!r.ok)throw 0;html=await r.text()}"
assert a in idx and b in idx, 'index.html loader changed; update build_offline.py'
idx = idx.replace(a, "Promise.resolve(OFF.m)").replace(b, "let html;\n  try{html=OFF.d[n];if(!html)throw 0}")
idx = idx.replace('--f-display:"Readex Pro","IBM Plex Sans Arabic",', '--f-display:"Readex Pro","IBM Plex Sans Arabic",Tahoma,"Segoe UI",')
idx = idx.replace('--f-body:"IBM Plex Sans Arabic","Readex Pro",', '--f-body:"IBM Plex Sans Arabic","Readex Pro",Tahoma,"Segoe UI",')
idx = idx.replace('<title>مذاكرة الـ AI من الصفر</title>', '<title>مذاكرة الـ AI من الصفر (أوفلاين)</title>', 1)
data = f'<script type="application/json" id="offline-data">{blob}</script>\n<script>window.OFF=JSON.parse(document.getElementById("offline-data").textContent);</script>\n'
i = idx.index('<script>')
open(out, 'w', encoding='utf-8').write(idx[:i] + data + idx[i:])
print(f'{len(days)} days -> {out}')
