import json,os,sys

REPO="/Users/home/פרוייקטים/wishlist-ida"
BASE="https://yaelavgil.github.io/wishlist-ida/"
DBURL="https://home-picks-47450-default-rtdb.europe-west1.firebasedatabase.app"

def tags(n):
    t=[]
    if "קיר" in n: t.append("מנורת קיר")
    if "תלוי" in n or "תלויה" in n: t.append("תלויה")
    if "צמוד" in n: t.append("צמודת תקרה")
    if not t: t.append("גוף תאורה")
    return t

items=json.load(open("/private/tmp/claude-501/-Users-home----------/4126668b-e0e5-4b5e-9e7f-2f21afab79a0/scratchpad/wishlist.json"))
DATA=[]
for k,it in enumerate(items):
    DATA.append({"id":"l"+str(k+1),"cat":"תאורה","type":"product","name":it["name"],"price":it["price"],
                 "link":it["link"],"img":"img/"+it["img"],"tags":tags(it["name"])})

# --- Kitchen handles (Domicile) — pulled from home-picks ---
HANDLES=[
 ("H1","ידית צינור וינטאג'","6880","handle01.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%a6%d7%99%d7%a0%d7%95%d7%a8-%d7%95%d7%99%d7%a0%d7%98%d7%90%d7%92-%d7%93%d7%92%d7%9d-6880/"),
 ("H2","ידית עם כדורים בקצוות בסגנון וינטג'","6988","handle02.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%a2%d7%9d-%d7%9b%d7%93%d7%95%d7%a8%d7%99%d7%9d-%d7%91%d7%a7%d7%a6%d7%95%d7%95%d7%aa-%d7%91%d7%a1%d7%92%d7%a0%d7%95%d7%9f-%d7%95%d7%99%d7%a0%d7%98%d7%92-%d7%93%d7%92/"),
 ("H3","ידית עם חיבורים גליליים בקצוות","6048","handle03.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%a2%d7%9d-%d7%97%d7%99%d7%91%d7%95%d7%a8%d7%99%d7%9d-%d7%92%d7%9c%d7%99%d7%9c%d7%99%d7%99%d7%9d-%d7%91%d7%a7%d7%a6%d7%95%d7%95%d7%aa-%d7%93%d7%92%d7%9d-6048/"),
 ("H4","ידית צינור עם בסיס ברגליים","6160","handle04.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%a6%d7%99%d7%a0%d7%95%d7%a8-%d7%a2%d7%9d-%d7%91%d7%a1%d7%99%d7%a1-%d7%91%d7%a8%d7%92%d7%9c%d7%99%d7%99%d7%9d-%d7%93%d7%92%d7%9d-6160/"),
 ("H5","ידית וינטאג' בסגנון כפרי","5190","handle05.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%95%d7%99%d7%a0%d7%98%d7%90%d7%92-%d7%91%d7%a1%d7%92%d7%a0%d7%95%d7%9f-%d7%9b%d7%a4%d7%a8%d7%99-%d7%93%d7%92%d7%9d-5190/"),
 ("H6","ידית ריהוט לארונות ומטבחים","F010","handle06.jpg","https://www.domicile.co.il/product/%d7%99%d7%93%d7%99%d7%aa-%d7%a8%d7%99%d7%94%d7%95%d7%98-%d7%9c%d7%90%d7%a8%d7%95%d7%a0%d7%95%d7%aa-%d7%95%d7%9e%d7%98%d7%91%d7%97%d7%99%d7%9d-%d7%93%d7%92%d7%9d-f010/"),
]
def htags(n):
    t=[]
    if "וינט" in n: t.append("וינטג'")
    if "כפרי" in n: t.append("כפרי")
    if "צינור" in n: t.append("צינור")
    if not t: t.append("קלאסי")
    return t
for h in HANDLES:
    DATA.append({"id":h[0],"cat":"ידיות","type":"product","name":h[1]+" · "+h[2],
                 "price":None,"link":h[4],"img":"img/"+h[3],"tags":htags(h[1])})

# --- Paint colors (Nirlat "Color Is") — pulled from home-picks ---
COLORS=[("C1","White Kitten","IS 0022","dfdedb","נייטרלים"),("C2","Mission Hills","IS 0363","e1dbc6","נייטרלים"),
 ("C3","Flan","IS 0237","e1caad","נייטרלים"),("C4","Phelps Putty","NTC 109","c0bbab","נייטרלים"),
 ("C5","Beacon Fog","IS 0490","a1adae","נייטרלים"),("C6","Lickety Split","IS 0699","c7dbd2","ירוקים"),
 ("C7","Resting Place","IS 0462","c1cbc1","ירוקים"),("C8","Uninhibited","IS 0700","bad2c9","ירוקים"),
 ("C9","Fair Maiden","IS 0456","acb8aa","ירוקים"),("C10","Plunge","IS 0701","aac5bb","ירוקים"),
 ("C11","Peg's Promise","IS 0702","93b1a6","ירוקים"),("C12","Melville","NTC 074","90a79c","ירוקים"),
 ("C13","Malarca","IS 0458","778575","ירוקים"),("C14","Drifting Tide","IS 0670","e0efec","ירוק-כחול"),
 ("C15","Dream Catcher","IS 0481","dce5de","ירוק-כחול"),("C16","Zircon Ice","IS 0664","d0e3e5","ירוק-כחול"),
 ("C17","Cape Hope","IS 0496","c2d3d3","ירוק-כחול"),("C18","Monet Magic","IS 0665","bedade","ירוק-כחול"),
 ("C19","Dreaming of the Day","IS 0470","b1c6c1","ירוק-כחול"),("C20","Restful Retreat","IS 0497","b5c8ca","ירוק-כחול"),
 ("C21","Stormy Bay","IS 0484","9fb3b2","ירוק-כחול"),("C22","Trisha's Eyes","IS 0666","93bac5","ירוק-כחול"),
 ("C23","Brush Blue","IS 0607","d6e2ed","כחולים"),("C24","Sea Foam Mist","IS 0642","cddde2","כחולים"),
 ("C25","Empress Lila","IS 0636","c7deed","כחולים"),("C26","Simple Serenity","IS 0614","cadae6","כחולים"),
 ("C27","Bridgewater Bay","IS 0650","c1d9e3","כחולים"),("C28","Abstract Idea","IS 0643","bdd2de","כחולים"),
 ("C29","Blue Bayou","IS 0615","b8cde0","כחולים"),("C30","Dream Whisper","NRC 085","b8cbd4","כחולים"),
 ("C31","Pompeii Ruins","IS 0623","b8c8d4","כחולים"),("C32","Dancing in the Rain","IS 0644","afc7d7","כחולים"),
 ("C33","Bluette","IS 0616","a4bfd8","כחולים"),("C34","In The Blue","IS 0504","a1b3be","כחולים"),
 ("C35","Cape Cod Bay","IS 0633","5e7585","כחולים"),("C36","Peninsula","IS 0654","4a80a1","כחולים")]
for c in COLORS:
    fan="https://nirlat.com/fan/#/category/wall/family//color-fan//hue/"+c[2].replace(" ","_")
    DATA.append({"id":c[0],"cat":"צבעים","type":"color","name":c[1],"code":c[2],
                 "hex":"#"+c[3],"price":None,"link":fan,"img":"","tags":[c[4]]})
CATS=[{"key":"all","label":"הכול","icon":"✦"},
      {"key":"תאורה","label":"תאורה","icon":"💡"},
      {"key":"צבעים","label":"צבעים","icon":"🎨"},
      {"key":"ידיות","label":"ידיות מטבח","icon":"🔩"}]

tpl=r'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>לוח החלטות · הבית של עידה</title>
<meta property="og:type" content="website">
<meta property="og:url" content="__BASE__">
<meta property="og:title" content="לוח החלטות — הבית של עידה">
<meta property="og:description" content="תאורה · צבעים · ידיות מטבח — בחירה, מיון וסינון נוחים לשיתוף.">
<meta property="og:site_name" content="הבית של עידה">
<meta property="og:image" content="__BASE__og.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="לוח החלטות — תאורה, צבעים וידיות מטבח">
<meta property="og:locale" content="he_IL">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="__BASE__og.jpg">
<meta name="theme-color" content="#b08a54">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#f5f1ea;--bg2:#efe8dc;--paper:#fffefb;--surface:#fff;
  --ink:#332c25;--ink-soft:#645a4f;--muted:#a3978a;--faint:#cabfae;
  --brass:#b08a54;--brass-d:#946f3c;--brass-soft:#f2ead9;
  --line:#eee7db;--line-2:#e6ddce;
  --yes:#5f8f5c;--yes-bg:#eef4ec;--maybe:#c79a3e;--maybe-bg:#f7efdd;--no:#c2604a;--no-bg:#f8ece7;
  --shadow:0 2px 6px rgba(95,72,40,.05),0 18px 40px -22px rgba(95,72,40,.30);
  --shadow-h:0 8px 18px rgba(95,72,40,.10),0 30px 60px -24px rgba(95,72,40,.40);
  --r:20px;--r-sm:13px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{font-family:"Rubik",-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;color:var(--ink);margin:0;
  padding:0 clamp(12px,3.5vw,40px) 90px;line-height:1.5;-webkit-font-smoothing:antialiased;
  background:radial-gradient(1200px 500px at 82% -6%,#fbf6ec 0,rgba(251,246,236,0) 60%),
    radial-gradient(900px 480px at 8% 4%,#f7efe1 0,rgba(247,239,225,0) 55%),linear-gradient(180deg,var(--bg),var(--bg2));
  background-attachment:fixed}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto}
header{padding:clamp(26px,4.5vw,50px) 4px 6px}
.kicker{display:inline-flex;align-items:center;gap:9px;font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--brass-d);margin:0 0 12px}
.kicker::before{content:"";width:28px;height:2px;border-radius:2px;background:var(--brass);opacity:.7}
h1{font-weight:700;font-size:clamp(28px,5vw,46px);letter-spacing:-.025em;margin:0 0 8px;line-height:1.05}
.sub{color:var(--ink-soft);font-size:clamp(14px,1.5vw,16px);max-width:60ch;margin:0}
.sub b{font-weight:600;color:var(--ink)}

/* sticky control deck */
.deck{position:sticky;top:0;z-index:30;margin:16px 0 0;padding:12px 0 10px;
  background:color-mix(in srgb,var(--bg) 86%,transparent);backdrop-filter:saturate(1.15) blur(12px);border-bottom:1.5px solid var(--line)}
.tabs{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding:2px 2px 8px}
.tabs::-webkit-scrollbar{display:none}
.tab{position:relative;flex:0 0 auto;border:1.5px solid var(--line-2);background:var(--paper);border-radius:999px;
  padding:9px 17px;font:inherit;font-weight:600;font-size:14px;color:var(--ink-soft);cursor:pointer;transition:.18s;display:inline-flex;align-items:center;gap:8px}
.tab .c{font-size:12px;color:var(--muted);background:var(--brass-soft);border-radius:999px;padding:1px 8px;font-weight:700}
.tab:hover{border-color:var(--faint);transform:translateY(-1px)}
.tab.on{background:linear-gradient(180deg,#bf9760,var(--brass-d));color:#fff;border-color:var(--brass-d);box-shadow:0 8px 18px -10px rgba(148,111,60,.8)}
.tab.on .c{background:rgba(255,255,255,.25);color:#fff}
.tools{display:flex;gap:9px;align-items:center;flex-wrap:wrap;padding:4px 2px 0}
.search{flex:1;min-width:180px;position:relative}
.search input{width:100%;border:1.5px solid var(--line-2);border-radius:var(--r-sm);padding:10px 38px 10px 14px;font:inherit;font-size:14px;background:var(--paper);transition:.18s}
.search input:focus{outline:none;border-color:var(--brass);box-shadow:0 0 0 4px var(--brass-soft)}
.search .i{position:absolute;inset-inline-start:12px;top:50%;transform:translateY(-50%);color:var(--muted);pointer-events:none}
select,.tbtn{border:1.5px solid var(--line-2);border-radius:var(--r-sm);padding:10px 14px;font:inherit;font-size:14px;font-weight:600;background:var(--paper);color:var(--ink);cursor:pointer;transition:.18s}
select:hover,.tbtn:hover{border-color:var(--faint)}
.tbtn.primary{background:linear-gradient(180deg,#bf9760,var(--brass-d));color:#fff;border-color:var(--brass-d);box-shadow:0 8px 18px -10px rgba(148,111,60,.8)}
.chips{display:flex;gap:7px;flex-wrap:wrap;padding:10px 2px 2px}
.chip{border:1.5px solid var(--line-2);background:var(--paper);border-radius:999px;padding:6px 13px;font:inherit;font-size:12.5px;font-weight:600;color:var(--ink-soft);cursor:pointer;transition:.15s}
.chip:hover{border-color:var(--faint)}
.chip.on{background:var(--brass-soft);border-color:var(--brass);color:var(--brass-d)}
.chip.st-yes.on{background:var(--yes-bg);border-color:var(--yes);color:var(--yes)}
.chip.st-maybe.on{background:var(--maybe-bg);border-color:var(--maybe);color:var(--maybe)}
.chip.st-no.on{background:var(--no-bg);border-color:var(--no);color:var(--no)}
.whoami{padding:9px 4px 0;font-size:13px;color:var(--ink-soft)}
.whoami b{color:var(--ink)}
.linkbtn{background:none;border:0;color:var(--brass-d);font:inherit;font-size:13px;cursor:pointer;text-decoration:underline;padding:0}
.people{display:flex;gap:5px;flex-wrap:wrap;margin:1px 0}
.pchip{width:23px;height:23px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11.5px;font-weight:700;color:#fff;box-shadow:0 1px 3px rgba(0,0,0,.18)}
.pchip.s-yes{background:var(--yes)}.pchip.s-maybe{background:var(--maybe)}.pchip.s-no{background:var(--no)}
.pchip.meC{box-shadow:0 0 0 2px var(--paper),0 0 0 3.5px var(--ink)}
.mepick{display:flex;gap:9px;flex-wrap:wrap}
.mepick .tbtn{flex:1;justify-content:center;font-size:15px;padding:13px}
.summ{display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:11px 4px 0;color:var(--ink-soft);font-size:13.5px;font-weight:500}
.summ b{color:var(--ink)}.summ .money{color:var(--brass-d);font-weight:700}

/* grid */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(clamp(210px,26vw,268px),1fr));gap:clamp(14px,1.8vw,22px);margin:20px 0 0;position:relative}
.card{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;
  box-shadow:var(--shadow);transition:box-shadow .22s,border-color .22s;will-change:transform}
.card:hover{box-shadow:var(--shadow-h)}
.card.hidden{display:none}
.card::before{content:"";position:absolute;inset-inline-start:0;top:0;bottom:0;width:5px;background:transparent;transition:.2s;z-index:2}
.card.s-yes::before{background:var(--yes)}.card.s-maybe::before{background:var(--maybe)}.card.s-no::before{background:var(--no)}
.card.s-no{opacity:.6}
.thumb{position:relative;aspect-ratio:4/3.4;overflow:hidden;background:#fbf8f2;display:block;cursor:zoom-in}
.thumb img{width:100%;height:100%;object-fit:contain;padding:12px;display:block;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.card:hover .thumb img{transform:scale(1.05)}
.tag{position:absolute;top:11px;inset-inline-end:11px;background:rgba(255,255,255,.86);backdrop-filter:blur(4px);color:var(--ink-soft);font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px}
.body{padding:13px 14px 15px;display:flex;flex-direction:column;gap:9px;flex:1}
.name{font-size:15.5px;font-weight:600;text-decoration:none;line-height:1.28;color:var(--ink)}
.name:hover{color:var(--brass-d)}
.price{font-weight:700;font-size:18px;color:var(--brass-d)}
.price.muted{color:var(--muted);font-weight:500;font-size:13px}
.thumb.swatch{cursor:zoom-in;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.thumb.swatch img{display:none}
.thumb.ph{display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#faf6ee,#efe7d9)}
.thumb.ph .phico{font-size:46px;opacity:.45}
.code{font-weight:600;font-size:14px;color:var(--ink-soft);letter-spacing:.03em}
.rmc{margin-top:6px;align-self:flex-start;background:none;border:0;color:var(--muted);font:inherit;font-size:12.5px;cursor:pointer;padding:2px 0}
.rmc:hover{color:var(--no)}
.form{display:flex;flex-direction:column;gap:12px}
.form label{font-size:13px;font-weight:600;color:var(--ink-soft);display:flex;flex-direction:column;gap:5px}
.form input,.form select{border:1.5px solid var(--line-2);border-radius:11px;padding:10px 12px;font:inherit;font-size:14px;background:var(--paper);color:var(--ink)}
.form input:focus,.form select:focus{outline:none;border-color:var(--brass);box-shadow:0 0 0 3px var(--brass-soft)}
.form .row2{display:flex;gap:10px}
.form input[type=color]{padding:4px;height:46px;cursor:pointer}
.seg{display:flex;gap:6px;margin-top:auto}
.seg button{flex:1;border:1.5px solid var(--line-2);background:var(--paper);border-radius:11px;padding:8px 0;font:inherit;font-size:15px;font-weight:700;cursor:pointer;transition:.15s;color:var(--muted)}
.seg button:hover{border-color:var(--faint)}
.seg .yes.on{background:var(--yes-bg);border-color:var(--yes);color:var(--yes)}
.seg .maybe.on{background:var(--maybe-bg);border-color:var(--maybe);color:var(--maybe)}
.seg .no.on{background:var(--no-bg);border-color:var(--no);color:var(--no)}
.qty{display:flex;align-items:center;justify-content:space-between;gap:8px}
.qty .ql{font-size:12.5px;color:var(--muted);font-weight:500}
.stp{display:inline-flex;align-items:center;border:1.5px solid var(--line-2);border-radius:10px;overflow:hidden;background:var(--paper)}
.stp button{border:0;background:transparent;padding:4px 12px;font-size:15px;cursor:pointer;color:var(--ink-soft)}
.stp button:hover{background:var(--brass-soft);color:var(--brass-d)}
.stp .qv{min-width:26px;text-align:center;font-weight:600;font-size:13.5px}
.note textarea{width:100%;border:1.5px solid var(--line-2);border-radius:12px;padding:8px 11px;font:inherit;font-size:13px;background:var(--paper);resize:vertical;min-height:0;height:38px;color:var(--ink);transition:.18s}
.note textarea:focus{outline:none;border-color:var(--brass);box-shadow:0 0 0 3px var(--brass-soft);height:64px}
.note textarea::placeholder{color:var(--faint)}
.empty{grid-column:1/-1;text-align:center;padding:56px 20px;color:var(--muted)}
.empty .big{font-size:40px;margin-bottom:12px}
.empty h3{font-size:18px;color:var(--ink-soft);margin:0 0 6px}
.empty p{margin:0 auto;max-width:46ch;font-size:14px}

/* lightbox */
.lb{position:fixed;inset:0;z-index:80;background:rgba(45,34,22,.62);backdrop-filter:blur(4px);display:none;align-items:center;justify-content:center;padding:24px;opacity:0;transition:opacity .2s}
.lb.on{display:flex;opacity:1}
.lb .box{background:var(--paper);border-radius:24px;max-width:640px;width:100%;overflow:hidden;transform:scale(.94);transition:transform .22s cubic-bezier(.2,.8,.2,1);box-shadow:0 40px 90px -20px rgba(40,28,12,.6)}
.lb.on .box{transform:scale(1)}
.lb .im{aspect-ratio:16/11;background:#fbf8f2;display:flex;align-items:center;justify-content:center}
.lb .im img{max-width:100%;max-height:100%;object-fit:contain;padding:18px}
.lb .info{padding:16px 20px 20px}
.lb .info h3{margin:0 0 4px;font-size:20px}
.lb .info .p{color:var(--brass-d);font-weight:700;font-size:20px}
.lb .x{position:absolute;top:18px;inset-inline-start:18px;width:40px;height:40px;border-radius:50%;border:0;background:rgba(255,255,255,.9);font-size:18px;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.2)}
.lb a.store{display:inline-block;margin-top:12px;color:var(--brass-d);font-weight:600;text-decoration:none;border-bottom:1.5px solid var(--brass-soft)}

.fab{position:fixed;bottom:20px;inset-inline-start:50%;transform:translateX(-50%);z-index:40}
dialog{border:0;border-radius:22px;padding:0;max-width:600px;width:92%;box-shadow:0 40px 90px -24px rgba(50,36,18,.55)}
dialog::backdrop{background:rgba(50,38,24,.42);backdrop-filter:blur(3px)}
.dh{padding:17px 20px 14px;border-bottom:1px solid var(--line);font-weight:700;font-size:17px}
.db{padding:16px 20px}.db textarea{width:100%;border:1.5px solid var(--line-2);border-radius:14px;padding:13px;font:inherit;font-size:13px;min-height:260px;background:var(--paper);line-height:1.6}
.df{padding:13px 20px 17px;display:flex;gap:10px}
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(16px);opacity:0;background:var(--ink);color:#fff;padding:12px 22px;border-radius:999px;font-weight:600;font-size:14px;transition:.28s;z-index:90;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
@media(max-width:520px){.thumb{aspect-ratio:4/3.2}.name{font-size:14px}.tab{padding:8px 13px}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="kicker">הבית של עידה · לוח החלטות</div>
  <h1>מה בוחרים לבית</h1>
  <p class="sub">כל ההחלטות במקום אחד — תאורה, צבעים וידיות. כל אחד בוחר שם ומסמן <b>✓ נבחר</b> / <b>? אולי</b> / <b>✕ לא</b> — <b>וכולם רואים את הבחירות של כולם, בזמן אמת</b>. אפשר גם למיין, לסנן ולהוסיף פריטים.</p>
</header>

<div class="deck">
  <div class="tabs" id="tabs"></div>
  <div class="tools">
    <div class="search"><span class="i">🔍</span><input id="q" placeholder="חיפוש לפי שם…" oninput="RE()"></div>
    <select id="sort" onchange="RE()">
      <option value="def">מיון: ברירת מחדל</option>
      <option value="pa">מחיר — מהזול ליקר</option>
      <option value="pd">מחיר — מהיקר לזול</option>
      <option value="name">שם (א׳→ת׳)</option>
      <option value="status">לפי סטטוס (נבחרו קודם)</option>
    </select>
    <button class="tbtn" onclick="openAdd()">➕ הוסף</button>
    <button class="tbtn primary" onclick="openSummary()">📋 סיכום לשליחה</button>
    <button class="tbtn" onclick="resetAll()">איפוס</button>
  </div>
  <div class="chips" id="stchips"></div>
  <div class="chips" id="tagchips"></div>
  <div class="whoami" id="whoami"></div>
  <div class="summ" id="summ"></div>
</div>

<div id="grid" class="grid"></div>
</div>

<div class="lb" id="lb" onclick="if(event.target===this)closeLB()"><button class="x" onclick="closeLB()">✕</button>
  <div class="box"><div class="im"><img id="lbimg" src="" alt=""></div>
  <div class="info"><h3 id="lbname"></h3><div class="p" id="lbprice"></div><a class="store" id="lbstore" target="_blank" rel="noopener">לצפייה בחנות ↗</a></div></div>
</div>

<dialog id="dlg"><div class="dh">📋 סיכום לשליחה</div>
  <div class="db"><textarea id="out"></textarea></div>
  <div class="df"><button class="tbtn primary" onclick="copyOut()">העתק ללוח</button><button class="tbtn" onclick="dlg.close()">סגור</button></div>
</dialog>
<div class="toast" id="toast">✓ הועתק</div>

<dialog id="meDlg"><div class="dh">👋 מי את/ה?</div>
  <div class="db">
    <p>בחרו שם — כל הסימונים שלכם יופיעו לכולם על אותו לוח, תחת השם הזה.</p>
    <div class="mepick">
      <button type="button" class="tbtn" onclick="setMe('יעל')">יעל</button>
      <button type="button" class="tbtn" onclick="setMe('רועי')">רועי</button>
      <button type="button" class="tbtn" onclick="setMe('נופר')">נופר</button>
    </div>
    <div class="form" style="margin-top:12px"><label>או שם אחר<input id="meOther" placeholder="השם שלך"></label></div>
  </div>
  <div class="df"><button class="tbtn primary" onclick="setMe(document.getElementById('meOther').value)">המשך</button></div>
</dialog>

<dialog id="addDlg"><div class="dh">➕ הוספת פריט</div>
  <div class="db"><div class="form">
    <label>קטגוריה<select id="a_sec" onchange="addToggle()"></select></label>
    <div id="a_newFields" class="row2" style="display:none">
      <label style="flex:2">שם קטגוריה חדשה<input id="a_secNew" placeholder="למשל: כלים סניטריים"></label>
      <label style="flex:1">אייקון<input id="a_secIcon" value="📌" maxlength="2" style="text-align:center"></label>
    </div>
    <label>סוג<select id="a_type" onchange="addToggle()"><option value="product">מוצר (תמונה)</option><option value="color">צבע / גוון</option></select></label>
    <label>שם<input id="a_name" placeholder="שם הפריט"></label>
    <div id="a_prodFields">
      <div class="row2">
        <label>מחיר ₪ (לא חובה)<input id="a_price" type="number" min="0" inputmode="numeric"></label>
        <label>תגית לסינון (לא חובה)<input id="a_tag" placeholder="למשל: תלוי"></label>
      </div>
      <label>קישור לתמונה (לא חובה)<input id="a_img" placeholder="https://…/image.jpg"></label>
    </div>
    <div id="a_colorFields" style="display:none">
      <div class="row2">
        <label style="flex:1">גוון<input id="a_hex" type="color" value="#c8bdae"></label>
        <label style="flex:2">קוד (לא חובה)<input id="a_code" placeholder="IS 0000"></label>
      </div>
    </div>
    <label>קישור לעמוד המוצר/הגוון (לא חובה)<input id="a_link" placeholder="https://…"></label>
    <p style="margin:2px 0 0;font-size:12px;color:var(--muted)">נשמר במכשיר שלך בלבד. כדי שכולם (בעל / מעצבת) יראו — שלחי לי את הפרטים ואטמיע בקביעות.</p>
  </div></div>
  <div class="df"><button class="tbtn primary" onclick="submitAdd()">הוסף</button><button class="tbtn" onclick="document.getElementById('addDlg').close()">ביטול</button></div>
</dialog>

<script>
const BITEMS=__DATA__, BCATS=__CATS__;
const DB="__DBURL__";
const KEY="ida-board-v1";
let st=JSON.parse(localStorage.getItem(KEY)||"{}"); st.s=st.s||{}; st.custom=st.custom||{cats:[],items:[],seq:0};
let me=JSON.parse(localStorage.getItem('ida-me')||'null'); // {pk,name}
let remote={}; // {pk:{name,items:{id:{s,n,q}}}}
let cat="all", stf=new Set(), tagf=new Set();
let ITEMS=[],CATS=[],byId={};
function rebuild(){ITEMS=BITEMS.concat(st.custom.items);CATS=BCATS.concat(st.custom.cats);byId=Object.fromEntries(ITEMS.map(x=>[x.id,x]));}
const els=new Map();
const dlg=document.getElementById('dlg'), grid=document.getElementById('grid');
const nis=n=>"₪"+(n||0).toLocaleString('en-US');
const S=id=>st.s[id]||(st.s[id]={status:'none',note:'',qty:1});
const save=()=>localStorage.setItem(KEY,JSON.stringify(st));
const STL={yes:'נבחר',maybe:'אולי',no:'לא',none:''};

function tabsHTML(){
  const t=document.getElementById('tabs'); t.innerHTML="";
  CATS.forEach(c=>{
    const n=c.key==='all'?ITEMS.length:ITEMS.filter(i=>i.cat===c.key).length;
    const b=document.createElement('button'); b.className="tab"+(cat===c.key?" on":"");
    b.innerHTML=`<span>${c.icon}</span>${c.label}<span class="c">${n}</span>`;
    b.onclick=()=>{cat=c.key;tagf.clear();buildChips();tabsHTML();RE(true);};
    t.appendChild(b);
  });
}
function buildChips(){
  const sc=document.getElementById('stchips');
  const sts=[['yes','✓ נבחר','st-yes'],['maybe','? אולי','st-maybe'],['no','✕ לא','st-no'],['none','לא הוחלט','']];
  sc.innerHTML=""; sts.forEach(([k,lab,cls])=>{
    const c=document.createElement('button'); c.className="chip "+cls+(stf.has(k)?" on":""); c.textContent=lab;
    c.onclick=()=>{stf.has(k)?stf.delete(k):stf.add(k);buildChips();RE();}; sc.appendChild(c);
  });
  const pool=ITEMS.filter(i=>cat==='all'||i.cat===cat).flatMap(i=>i.tags||[]);
  const uniq=[...new Set(pool)];
  const tc=document.getElementById('tagchips'); tc.innerHTML="";
  uniq.forEach(tg=>{const c=document.createElement('button'); c.className="chip"+(tagf.has(tg)?" on":""); c.textContent=tg;
    c.onclick=()=>{tagf.has(tg)?tagf.delete(tg):tagf.add(tg);buildChips();RE();}; tc.appendChild(c);});
}
function visible(){
  const q=(document.getElementById('q').value||"").trim();
  let a=ITEMS.filter(i=>(cat==='all'||i.cat===cat)
    &&(!q||i.name.includes(q))
    &&(stf.size===0||stf.has(S(i.id).status))
    &&(tagf.size===0||(i.tags||[]).some(t=>tagf.has(t))));
  const s=document.getElementById('sort').value, rank={yes:0,maybe:1,none:2,no:3};
  if(s==='pa')a.sort((x,y)=>x.price-y.price);
  else if(s==='pd')a.sort((x,y)=>y.price-x.price);
  else if(s==='name')a.sort((x,y)=>x.name.localeCompare(y.name,'he'));
  else if(s==='status')a.sort((x,y)=>rank[S(x.id).status]-rank[S(y.id).status]);
  return a;
}
function cardEl(it){
  if(els.has(it.id))return els.get(it.id);
  const c=document.createElement('div'); c.dataset.id=it.id;
  const badge=(it.tags&&it.tags[0])?`<span class="tag">${it.tags[0]}</span>`:'';
  const media=it.type==='color'
    ?`<div class="thumb swatch" style="background:${it.hex}" onclick="openLB('${it.id}')">${badge}</div>`
    :it.img
      ?`<div class="thumb" onclick="openLB('${it.id}')">${badge}<img loading="lazy" src="${it.img}" alt="${it.name}"></div>`
      :`<div class="thumb ph" onclick="openLB('${it.id}')">${badge}<span class="phico">${(CATS.find(x=>x.key===it.cat)||{}).icon||'📦'}</span></div>`;
  const nameEl=it.link?`<a class="name" href="${it.link}" target="_blank" rel="noopener">${it.name}</a>`:`<span class="name">${it.name}</span>`;
  const sub=it.type==='color'?`<div class="code">${it.code||''}</div>`
    :(it.price!=null?`<div class="price">${nis(it.price)}</div>`:`<div class="price muted">המחיר בחשבון שלך בחנות</div>`);
  const qty=it.type==='product'
    ?`<div class="qty"><span class="ql">כמות</span><span class="stp"><button title="הפחת" onclick="setQ('${it.id}',-1)">−</button><span class="qv">1</span><button title="הוסף" onclick="setQ('${it.id}',1)">+</button></span></div>`:'';
  c.innerHTML=`${media}
    <div class="body">
      ${nameEl}
      ${sub}
      <div class="people" style="display:none"></div>
      ${qty}
      <div class="seg">
        <button class="yes" title="נבחר" onclick="setS('${it.id}','yes')">✓</button>
        <button class="maybe" title="אולי" onclick="setS('${it.id}','maybe')">?</button>
        <button class="no" title="לא" onclick="setS('${it.id}','no')">✕</button>
      </div>
      <div class="note"><textarea placeholder="הערה…" oninput="setN('${it.id}',this.value)"></textarea></div>
      ${it.custom?`<button class="rmc" onclick="removeCustom('${it.id}')">🗑 הסר פריט</button>`:''}
    </div>`;
  els.set(it.id,c); grid.appendChild(c); paint(it.id,c); return c;
}
function paint(id,c){
  c=c||els.get(id); if(!c)return; const s=S(id);
  c.className="card"+(s.status!=='none'?" s-"+s.status:"");
  c.querySelectorAll('.seg button').forEach(b=>b.classList.toggle('on',b.classList.contains(s.status)));
  const ta=c.querySelector('textarea'); if(ta&&ta.value!==s.note)ta.value=s.note;
  const qv=c.querySelector('.qv'); if(qv)qv.textContent=s.qty||1;
}
function RE(animate){
  ITEMS.forEach(it=>cardEl(it));
  const vis=visible(), visSet=new Set(vis.map(v=>v.id));
  // FLIP: measure first
  const first=new Map();
  els.forEach((c,id)=>{if(!c.classList.contains('hidden'))first.set(id,c.getBoundingClientRect());});
  // reorder + toggle
  vis.forEach(v=>grid.appendChild(els.get(v.id)));
  els.forEach((c,id)=>c.classList.toggle('hidden',!visSet.has(id)));
  // measure last + animate
  els.forEach((c,id)=>{
    if(c.classList.contains('hidden'))return;
    const f=first.get(id), l=c.getBoundingClientRect();
    if(f){const dx=f.left-l.left, dy=f.top-l.top;
      if(dx||dy){c.style.transition='none';c.style.transform=`translate(${dx}px,${dy}px)`;
        requestAnimationFrame(()=>{c.style.transition='transform .4s cubic-bezier(.2,.7,.2,1)';c.style.transform='';});}
    }else if(animate){c.style.transition='none';c.style.opacity='0';c.style.transform='scale(.96)';
      requestAnimationFrame(()=>{c.style.transition='.3s';c.style.opacity='';c.style.transform='';});}
  });
  // empty state
  let e=grid.querySelector('.empty'); if(e)e.remove();
  if(vis.length===0){const d=document.createElement('div'); d.className="empty";
    const isEmptyCat=ITEMS.filter(i=>cat===i.cat).length===0 && cat!=='all';
    d.innerHTML=isEmptyCat
      ?`<div class="big">${(CATS.find(c=>c.key===cat)||{}).icon||'✦'}</div><h3>הקטגוריה הזו עדיין ריקה</h3><p>שלחי לי את המקור (לינקים/תמונות/טבלה) ואמלא אותה כאן — עם אותם כלי בחירה, מיון וסינון.</p>`
      :`<div class="big">🔍</div><h3>אין תוצאות לסינון הנוכחי</h3><p>נסי לנקות חלק מהמסננים או החיפוש.</p>`;
    grid.appendChild(d);}
  updateSumm(vis);
}
function updateSumm(vis){
  const inCat=ITEMS.filter(i=>cat==='all'||i.cat===cat);
  const yes=inCat.filter(i=>S(i.id).status==='yes'); const maybe=inCat.filter(i=>S(i.id).status==='maybe');
  const sum=yes.reduce((a,i)=>a+(i.price||0)*(S(i.id).qty||1),0);
  document.getElementById('summ').innerHTML=
    `מוצג: <b>${vis.length}</b> · נבחרו: <b style="color:var(--yes)">${yes.length}</b> · אולי: <b style="color:var(--maybe)">${maybe.length}</b> · סה״כ נבחרים: <span class="money">${nis(sum)}</span>`;
}
function setS(id,v){const s=S(id); s.status=(s.status===v)?'none':v; save(); paint(id); fbPushMark(id); renderPeople();
  const so=document.getElementById('sort').value; updateSumm(visible());
  if(stf.size||so==='status')RE(); }
function setN(id,v){S(id).note=v;save();fbPushMark(id);}
function setQ(id,d){const s=S(id);s.qty=Math.max(1,(s.qty||1)+d);save();paint(id);fbPushMark(id);updateSumm(visible());}
function openLB(id){const it=byId[id];
  const im=document.querySelector('.lb .im'), img=document.getElementById('lbimg');
  if(it.type==='color'){img.style.display='none';im.style.background=it.hex;}
  else if(it.img){img.style.display='';im.style.background='';img.src=it.img;}
  else{img.style.display='none';im.style.background='linear-gradient(135deg,#faf6ee,#efe7d9)';}
  document.getElementById('lbname').textContent=it.name;
  document.getElementById('lbprice').textContent=it.type==='color'?(it.code||''):(it.price!=null?nis(it.price):'');
  const stEl=document.getElementById('lbstore'); if(it.link){stEl.style.display='';stEl.href=it.link;stEl.textContent=it.type==='color'?'לגוון באתר נירלט ↗':'לצפייה בחנות ↗';}else{stEl.style.display='none';}
  document.getElementById('lb').classList.add('on');}
function closeLB(){document.getElementById('lb').classList.remove('on');}
function resetAll(){if(confirm("לאפס את כל הבחירות וההערות?")){st.s={};save();els.forEach((c,id)=>paint(id));RE();}}
function openSummary(){
  let out=""; const cats=CATS.filter(c=>c.key!=='all');
  cats.forEach(c=>{
    const its=ITEMS.filter(i=>i.cat===c.key);
    const yes=its.filter(i=>S(i.id).status==='yes'), maybe=its.filter(i=>S(i.id).status==='maybe'), no=its.filter(i=>S(i.id).status==='no');
    if(!yes.length&&!maybe.length&&!no.length)return;
    out+=`\n${c.icon} ${c.label}\n`+"—".repeat(20)+"\n";
    const line=i=>{const q=S(i.id).qty||1; let l="• "+i.name; if(i.type==='color'&&i.code)l+="  ("+i.code+")"; if(i.price!=null)l+=(q>1?"  ×"+q:"")+"  —  "+nis(i.price*q); const n=S(i.id).note; if(n&&n.trim())l+="\n   ↳ "+n.trim(); return l;};
    if(yes.length){out+="✓ נבחרו:\n"+yes.map(line).join("\n")+"\n";}
    if(maybe.length){out+="\n? אולי:\n"+maybe.map(line).join("\n")+"\n";}
    if(no.length){out+="\n✕ לא:\n"+no.map(i=>"• "+i.name).join("\n")+"\n";}
  });
  out=(out.trim()?"✦ לוח החלטות — הבית של עידה\n"+out:"עדיין לא סומנו פריטים.");
  document.getElementById('out').value=out; dlg.showModal();
}
function copyOut(){const o=document.getElementById('out');o.select();
  const d=()=>{const t=document.getElementById('toast');t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1500);};
  navigator.clipboard?navigator.clipboard.writeText(o.value).then(d,()=>{document.execCommand('copy');d();}):(document.execCommand('copy'),d());}
function addToggle(){
  const sec=document.getElementById('a_sec').value;
  document.getElementById('a_newFields').style.display=sec==='__new__'?'flex':'none';
  const t=document.getElementById('a_type').value;
  document.getElementById('a_prodFields').style.display=t==='product'?'':'none';
  document.getElementById('a_colorFields').style.display=t==='color'?'':'none';
}
function openAdd(){
  const sel=document.getElementById('a_sec'); sel.innerHTML="";
  CATS.filter(c=>c.key!=='all').forEach(c=>{const o=document.createElement('option');o.value=c.key;o.textContent=c.icon+' '+c.label;sel.appendChild(o);});
  const o=document.createElement('option');o.value='__new__';o.textContent='➕ קטגוריה חדשה…';sel.appendChild(o);
  if(cat!=='all')sel.value=cat;
  ['a_name','a_price','a_img','a_link','a_tag','a_code','a_secNew'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('a_secIcon').value='📌';
  addToggle(); document.getElementById('addDlg').showModal();
}
function submitAdd(){
  const name=document.getElementById('a_name').value.trim();
  if(!name){alert('צריך שם לפריט');return;}
  let secKey=document.getElementById('a_sec').value;
  if(secKey==='__new__'){
    const lab=document.getElementById('a_secNew').value.trim();
    if(!lab){alert('צריך שם לקטגוריה החדשה');return;}
    const icon=document.getElementById('a_secIcon').value.trim()||'📌';
    secKey='uc'+(++st.custom.seq); st.custom.cats.push({key:secKey,label:lab,icon:icon});
  }
  const type=document.getElementById('a_type').value;
  const it={id:'ui'+(++st.custom.seq),cat:secKey,type:type,name:name,custom:true,link:document.getElementById('a_link').value.trim()};
  if(type==='color'){it.hex=document.getElementById('a_hex').value;const cd=document.getElementById('a_code').value.trim();if(cd)it.code=cd;it.price=null;it.tags=[];}
  else{const p=document.getElementById('a_price').value;it.price=p?Number(p):null;const img=document.getElementById('a_img').value.trim();if(img)it.img=img;const tg=document.getElementById('a_tag').value.trim();it.tags=tg?[tg]:[];}
  st.custom.items.push(it); save(); rebuild(); cat=secKey; stf.clear(); tagf.clear();
  document.getElementById('addDlg').close(); buildChips(); tabsHTML(); RE(true);
}
function removeCustom(id){
  if(!confirm('להסיר את הפריט?'))return;
  st.custom.items=st.custom.items.filter(x=>x.id!==id); delete st.s[id]; save();
  const el=els.get(id); if(el){el.remove();els.delete(id);} rebuild(); buildChips(); tabsHTML(); RE();
}
/* ---------- shared backend (Firebase RTDB via REST) ---------- */
function uid(){try{return crypto.randomUUID();}catch(e){return 'p'+Date.now().toString(36)+Math.random().toString(16).slice(2);}}
function meaningful(s){return s&&((s.status&&s.status!=='none')||(s.note&&s.note.trim())||(s.qty&&s.qty>1));}
function fbPushMark(id){ if(!me)return; const s=st.s[id]||{};
  const u=`${DB}/picks/${me.pk}/items/${encodeURIComponent(id)}.json`;
  if(meaningful(s)) fetch(u,{method:'PUT',body:JSON.stringify({s:s.status||'none',n:s.note||'',q:s.qty||1})}).catch(()=>{});
  else fetch(u,{method:'DELETE'}).catch(()=>{}); }
function fbPushAll(){ if(!me)return; const items={};
  Object.keys(st.s).forEach(id=>{const s=st.s[id]; if(meaningful(s)) items[id]={s:s.status,n:s.note||'',q:s.qty||1};});
  fetch(`${DB}/picks/${me.pk}.json`,{method:'PATCH',body:JSON.stringify({name:me.name})}).catch(()=>{});
  fetch(`${DB}/picks/${me.pk}/items.json`,{method:'PATCH',body:JSON.stringify(items)}).catch(()=>{}); }
function fbPoll(){ fetch(`${DB}/picks.json`).then(r=>r.json()).then(d=>{remote=d||{};renderPeople();}).catch(()=>{}); }
const STL2={yes:'✓ נבחר',maybe:'? אולי',no:'✕ לא'};
function marksFor(id){
  const out=[];
  Object.entries(remote).forEach(([pk,p])=>{ if(!p||!p.items)return; const m=p.items[id];
    if(m&&m.s&&m.s!=='none') out.push({pk,name:p.name||'?',status:m.s,mine:me&&pk===me.pk}); });
  if(me){ const s=st.s[id]; const mine=out.find(o=>o.mine);
    if(s&&s.status&&s.status!=='none'){ if(mine)mine.status=s.status; else out.push({pk:me.pk,name:me.name,status:s.status,mine:true}); }
    else if(mine) out.splice(out.indexOf(mine),1); }
  return out;
}
function renderPeople(){
  els.forEach((c,id)=>{const box=c.querySelector('.people'); if(!box)return; const ms=marksFor(id);
    box.innerHTML=ms.map(m=>`<span class="pchip s-${m.status}${m.mine?' meC':''}" title="${m.name}: ${STL2[m.status]||''}">${(m.name||'?').trim().charAt(0)||'?'}</span>`).join('');
    box.style.display=ms.length?'':'none'; });
  const names=new Set(Object.values(remote||{}).map(p=>p&&p.name).filter(Boolean)); if(me&&me.name)names.add(me.name);
  const el=document.getElementById('whoami');
  if(el) el.innerHTML=(me?`אני: <b>${me.name}</b> <button class="linkbtn" onclick="openMe()">(החלף)</button>`:'')
    +(names.size?` &nbsp;·&nbsp; משתתפים: ${[...names].join(' · ')}`:'');
}
function openMe(){ document.getElementById('meOther').value=(me&&!['יעל','רועי','נופר'].includes(me.name))?me.name:''; document.getElementById('meDlg').showModal(); }
function setMe(name){ name=(name||'').trim(); if(!name){alert('צריך שם');return;}
  const pk=(me&&me.pk)||uid(); me={pk,name}; localStorage.setItem('ida-me',JSON.stringify(me));
  document.getElementById('meDlg').close(); fbPushAll(); startSync(); renderPeople(); }
function startSync(){ fbPoll(); if(!window._pollI) window._pollI=setInterval(fbPoll,5000); }
document.addEventListener('visibilitychange',()=>{if(!document.hidden)fbPoll();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeLB();}});
rebuild(); tabsHTML(); buildChips(); RE(true);
if(me) startSync(); else openMe();
</script>
</body>
</html>'''
out=(tpl.replace("__DATA__",json.dumps(DATA,ensure_ascii=False))
        .replace("__CATS__",json.dumps(CATS,ensure_ascii=False))
        .replace("__DBURL__",DBURL)
        .replace("__BASE__",BASE))
open(os.path.join(REPO,"index.html"),"w",encoding="utf-8").write(out)

# Fresh-URL copy at /picks/ — never seen by WhatsApp, so it forces a clean re-scrape.
# <base> makes relative assets (img/, favicon) resolve to the repo root; og:url is self-referential.
picks=out.replace('<meta property="og:url" content="'+BASE+'">',
                  '<meta property="og:url" content="'+BASE+'picks/">')
picks=picks.replace('<head>\n','<head>\n<base href="'+BASE+'">\n',1)
os.makedirs(os.path.join(REPO,"picks"),exist_ok=True)
open(os.path.join(REPO,"picks","index.html"),"w",encoding="utf-8").write(picks)
print("board built | items",len(DATA),"| bytes",len(out),"| + /picks/ fresh copy")
