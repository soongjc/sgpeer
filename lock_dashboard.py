#!/usr/bin/env python3
"""Lock an HTML dashboard behind a passphrase.

Usage:  python3 lock_dashboard.py input.html output.html "your passphrase"

The whole page is encrypted with AES-256-GCM using a key derived from the
passphrase (PBKDF2-SHA256, 600k iterations). The output file contains only
ciphertext plus a small decrypt-and-render shell; viewing the source reveals
nothing about the content. Decryption happens in the browser with Web Crypto.
Re-run this on every update; the passphrase never needs to change.
"""
import base64, json, os, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 600_000

def lock(src: str, dst: str, passphrase: str, title: str = "Dashboard"):
    plain = open(src, "rb").read()
    salt, iv = os.urandom(16), os.urandom(12)
    key = PBKDF2HMAC(hashes.SHA256(), 32, salt, ITER).derive(passphrase.encode())
    ct = AESGCM(key).encrypt(iv, plain, None)
    payload = json.dumps({
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(iv).decode(),
        "iter": ITER,
        "ct": base64.b64encode(ct).decode(),
    })
    shell = SHELL.replace("__PAYLOAD__", payload).replace("__TITLE__", title)
    open(dst, "w").write(shell)
    print(f"locked {src} -> {dst} ({len(ct)//1024} KB ciphertext)")

SHELL = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
  :root{color-scheme:light dark}
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;font-family:system-ui,sans-serif;background:#f5f6f4;color:#14171b}
  @media(prefers-color-scheme:dark){body{background:#111316;color:#eef0f2}}
  #f{width:min(360px,90vw);padding:24px;border:1px solid #8884;border-radius:8px}
  h1{font-size:16px;margin:0 0 12px}
  input{width:100%;box-sizing:border-box;font-size:16px;padding:12px;border:1px solid #8886;border-radius:4px;background:transparent;color:inherit}
  button{margin-top:10px;width:100%;padding:12px;font-size:15px;font-weight:600;border:0;border-radius:4px;background:#ffc83d;color:#14171b;cursor:pointer}
  p{font-size:12px;opacity:.7;margin:10px 0 0;min-height:1em}
</style></head>
<body>
<div id="f"><h1>__TITLE__</h1>
<input id="p" type="password" autocomplete="off" placeholder="Passphrase" autofocus>
<button type="button" id="go">Open</button><p id="m"></p></div>
<script id="payload" type="application/json">__PAYLOAD__</script>
<script>
const P=JSON.parse(document.getElementById('payload').textContent);
const b64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
async function open(){
  const m=document.getElementById('m'); m.textContent='Decrypting…';
  try{
    if(!(crypto&&crypto.subtle)) throw new Error('Web Crypto unavailable in this viewer. Open the file in a browser tab.');
    const enc=new TextEncoder();
    const base=await crypto.subtle.importKey('raw',enc.encode(document.getElementById('p').value),'PBKDF2',false,['deriveKey']);
    const key=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(P.salt),iterations:P.iter,hash:'SHA-256'},base,{name:'AES-GCM',length:256},false,['decrypt']);
    const pt=await crypto.subtle.decrypt({name:'AES-GCM',iv:b64(P.iv)},key,b64(P.ct));
    const html=new TextDecoder().decode(pt);
    try{ document.open(); document.write(html); document.close(); }
    catch(e2){ const fr=document.createElement('iframe'); fr.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;border:0'; fr.srcdoc=html; document.body.innerHTML=''; document.body.appendChild(fr); }
  }catch(err){ m.textContent = err.name==='OperationError' ? 'Wrong passphrase.' : ('Could not open: '+err.message); }
}
document.getElementById('go').addEventListener('click',open);
document.getElementById('p').addEventListener('keydown',e=>{ if(e.key==='Enter') open(); });
</script></body></html>"""

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    lock(sys.argv[1], sys.argv[2], sys.argv[3], "Singapore peers, 1H26")
