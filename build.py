"""Builds the standalone Fed Up site (index.html) from the app page plus the sign-in/storage layer."""
import sys
app = open(sys.argv[1]).read()
shim = open(sys.argv[2]).read()
def rep(a, b):
    global app
    assert app.count(a) >= 1, a[:60]
    app = app.replace(a, b)
rep('<strong>Share with the group</strong>', '<strong>Share with everyone on Fed Up</strong>')
rep('Everyone this page is shared with can see and use this recipe', 'Everyone signed in to Fed Up can see and use this recipe')
rep("'someone in the group'", "'another member'")
rep('>From the group</button>', '>From the community</button>')
rep("off: 'Saved on this device only right now. Open it in Claude while signed in to sync across your devices and share recipes.'", "off: 'Saved on this device only right now. Check your connection and reload to sync across your devices.'")
rep("Ask the owner for edit access to sync and to share recipes.", "Reload and sign in again to sync.")
cut = app.index('<div class="wrap">')
head, body = app[:cut], app[cut:]
k = body.index('<script>')
body = body[:k] + shim + '\n' + body[k:]
extra_css = """<style>
.auth { position: fixed; inset: 0; z-index: 50; background: var(--bg); display: grid; place-items: center; padding: 24px 16px; overflow: auto; }
.auth-card { width: min(400px, 100%); display: flex; flex-direction: column; gap: 16px; }
.auth input[type="password"] { background: var(--soft); border: 1px solid transparent; border-radius: 12px; padding: 10px 12px; width: 100%; height: 44px; }
.auth input[type="password"]:focus { background: #fff; border-color: var(--ink); outline: none; }
.update-bar { position: fixed; left: 50%; transform: translateX(-50%); top: calc(10px + env(safe-area-inset-top, 0px)); z-index: 60; width: min(440px, calc(100vw - 24px)); border: 0; border-radius: 999px; padding: 12px 18px; background: #FF1F8F; color: #fff; font: inherit; font-size: 0.9rem; line-height: 1.3; text-align: center; box-shadow: 0 10px 26px rgba(255, 31, 143, 0.38); cursor: pointer; }
.update-bar strong { text-decoration: underline; text-underline-offset: 2px; white-space: nowrap; }
</style>"""
SPLASH_FONT = {'fam': 'Dancing Script', 'css': 'Dancing+Script:wght@700', 'w': 700, 's1': 50, 's2': 40}
SPLASH = """<div id="splash" role="status" aria-label="Fed Up Meals is loading">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%(css)s&display=block&text=FedUpMals">
<style>
#splash { position: fixed; inset: 0; z-index: 100; display: grid; place-items: center; background-color: #FFFFFF;
  background-image: conic-gradient(#FBCFE2 25%%, transparent 0 50%%, #FBCFE2 0 75%%, transparent 0); background-size: 72px 72px;
  transition: opacity .35s ease, visibility .35s; }
#splash.done { opacity: 0; visibility: hidden; }
#splash .sp-in { display: flex; flex-direction: column; align-items: center; gap: 18px; }
#splash .sp-plate { width: 236px; height: 236px; border-radius: 50%%; background: #FFFFFF; display: grid; place-items: center; box-shadow: 6px 12px 0 rgba(217, 138, 174, .35); }
#splash .sp-rim { width: 198px; height: 198px; border-radius: 50%%; background: #FBFAF8; border: 2px solid #EFE7EA; }
#splash .sp-rim svg { width: 100%%; height: 100%%; overflow: visible; }
#splash .sp-w { fill: #E0247A; stroke: #E0247A; stroke-width: 1.1; stroke-linejoin: round; stroke-dasharray: 700; stroke-dashoffset: 700; fill-opacity: 0; font-family: "%(fam)s", cursive; font-weight: %(w)s; }
#splash .sp-tag { background: #FFFFFF; color: #111113; font: 600 .95rem/1.2 "Instrument Sans", system-ui, sans-serif; padding: 8px 16px; border-radius: 999px; box-shadow: 0 2px 10px rgba(0,0,0,.06); opacity: 0; }
#splash .sp-dots { display: flex; gap: 8px; }
#splash .sp-dots i { width: 10px; height: 10px; border-radius: 50%%; background: #E0247A; animation: sp-bounce 1s infinite ease-in-out; }
#splash .sp-dots i:nth-child(2) { animation-delay: .15s; } #splash .sp-dots i:nth-child(3) { animation-delay: .3s; }
#splash.go .sp-plate { animation: sp-pop .5s cubic-bezier(.2, 1.4, .4, 1) both; }
#splash.go .sp-w { animation: sp-write 1.5s ease-in-out forwards, sp-ink .6s ease-out forwards; }
#splash.go .sp-w1 { animation-delay: .2s, 1.1s; }
#splash.go .sp-w2 { animation-delay: .95s, 1.85s; }
#splash.go .sp-tag { animation: sp-fade .5s 1.8s forwards; }
@keyframes sp-write { to { stroke-dashoffset: 0; } }
@keyframes sp-ink { to { fill-opacity: 1; } }
@keyframes sp-fade { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
@keyframes sp-pop { from { transform: scale(.6); opacity: 0; } to { transform: scale(1); opacity: 1; } }
@keyframes sp-bounce { 0%%, 80%%, 100%% { transform: translateY(0); opacity: .45; } 40%% { transform: translateY(-8px); opacity: 1; } }
@media (prefers-reduced-motion: reduce) { #splash .sp-w { stroke-dashoffset: 0; fill-opacity: 1; } #splash .sp-tag { opacity: 1; } #splash.go .sp-plate, #splash.go .sp-w, #splash.go .sp-tag, #splash .sp-dots i { animation: none; } }
</style>
<div class="sp-in">
  <div class="sp-plate"><div class="sp-rim"><svg viewBox="0 0 200 200" aria-hidden="true">
    <text class="sp-w sp-w1" x="100" y="96" text-anchor="middle" font-size="%(s1)s">Fed Up</text>
    <text class="sp-w sp-w2" x="100" y="146" text-anchor="middle" font-size="%(s2)s">Meals</text>
  </svg></div></div>
  <div class="sp-tag">Plan it. Price it. Shop it.</div>
  <div class="sp-dots" aria-hidden="true"><i></i><i></i><i></i></div>
</div>
<script>
(function () {
  var el = document.getElementById('splash'), start = Date.now(), began = 0, gone = false;
  /* start writing once the handwriting font is ready (never in a plain font), or after 1.2s at most */
  function go() { if (began) return; began = Date.now(); el.classList.add('go'); }
  try { document.fonts.load('%(w)s 50px "%(fam)s"', 'FedUpMals').then(go, go); } catch (e) { go(); }
  setTimeout(go, 1200);
  window.fedupSplashDone = function () {
    if (gone) return; gone = true;
    (function wait() {
      /* let the writing finish (about 2.4s), unless loading took long anyway */
      if (!began) return setTimeout(wait, 100);
      var left = Math.max(0, 2500 - (Date.now() - began));
      setTimeout(function () { el.classList.add('done'); setTimeout(function () { el.remove(); }, 400); }, left);
    })();
  };
  setTimeout(window.fedupSplashDone, 8000);
})();
</script>
</div>
""" % SPLASH_FONT
import time
version = time.strftime('%Y%m%d%H%M%S')
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="fedup-version" content="' + version + '">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="theme-color" content="#FFFFFF">\n'
       '<link rel="manifest" href="manifest.webmanifest">\n'
       '<link rel="apple-touch-icon" href="icon-180.png">\n'
       '<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">\n'
       '<meta name="apple-mobile-web-app-capable" content="yes">\n'
       '<meta name="mobile-web-app-capable" content="yes">\n'
       '<meta name="apple-mobile-web-app-title" content="Fed Up">\n'
       '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
       '<style>:root{color-scheme:light;padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
       + head + extra_css + '\n</head>\n<body>\n' + SPLASH + body + '\n</body>\n</html>\n')
open(sys.argv[3], 'w').write(out)
print('built', len(out))
