# -*- coding: utf-8 -*-
import html

# ── EDIT THESE THREE FOR A NEW BOOK ──────────────────────────────
BOOK_NUM   = "1"
BOOK_TITLE = "Rise of the Earth Dragon"
OUTFILE    = f"DM{BOOK_NUM}_KeyWord_Retelling_AllChapters.html"
# ─────────────────────────────────────────────────────────────────

# chapter: (num, title, [stops]); stop=(where, when, who[], did[])
chapters=[
("1","To the Castle!",[
 ("The Onion Patch","One morning",
   ["Drake (a farm boy)","a king's soldier"],
   ["was digging up onions","came on a black horse","took Drake to see King Roland"]),
 ("Castle Halls & Stairs","After arriving at the castle",
   ["Drake","the soldier"],
   ["rode through the village, over a stone bridge","saw paintings, statues, fancy clothes","went down the stairs","said \"[quote from the chapter]\" and left"]),
 ("The Big Stone Door","End of the chapter",
   ["Drake","a giant red dragon"],
   ["stood alone — afraid but curious","pushed the door open","shot a huge fireball"]),
]),
("2","The Dragon Stone",[
 ("The Stone Door","Right after Chapter 1",
   ["a red-haired girl","the dragon (Vulcan)","a wizard — white beard, pointy hat"],
   ["yelled \"[quote from the chapter]\"","had shiny red scales, a long tail","walked out"]),
 ("Griffith's Workshop","After the wizard led Drake inside",
   ["the wizard Griffith","Drake"],
   ["opened the lock with sparks","showed powders & a wooden box","said Drake had \"[quote from the chapter]\"","gave a green stone on a gold chain","warned dragons are dangerous"]),
]),
("3","More Dragons!",[
 ("The Underground Room","After leaving the workshop",
   ["Drake","Rori & Vulcan","Bo & Shu","Ana & Kepri"],
   ["entered a room with no windows, only torches","met the other masters & dragons","thought \"[quote from the chapter]\""]),
 ("Drake's Dragon Cave","When they reached the cave",
   ["Griffith","Drake"],
   ["said \"[quote from the chapter]\"","showed a small cave with wood bars","felt nervous but excited"]),
]),
("4","Worm",[
 ("Inside Worm's Cave","After the bars were opened",
   ["Drake","his dragon"],
   ["saw a brown, snake-like dragon — tiny wings, no legs","put on the stone and felt tingly","named it Worm"]),
 ("Walking to the Training Room","After leaving the cave",
   ["Drake","Worm","Rori"],
   ["said \"[quote from the chapter]\"","teased \"[quote from the chapter]\"","worried he wasn't a real Dragon Master"]),
]),
("5","Do Something!",[
 ("The Training Room","The day after arriving",
   ["Rori & Vulcan","Bo & Shu","Ana & Kepri","Drake & Worm"],
   ["shot fire at the bull's-eye","sprayed water to put out the fire","made a rainbow with light","did nothing — Drake felt \"[quote from the chapter]\""]),
]),
("6","A New Friend",[
 ("The Dining Room","At suppertime",
   ["Drake","Bo","Ana"],
   ["ate a feast — chicken, potatoes, cheese","the plate floated over with sparks","came from the east / the south","Bo wrote Drake's letter to his mother — no dragons"]),
]),
("7","A Strange Dream",[
 ("The Dining Room","After the letter was taken",
   ["King Roland the Bold","Drake"],
   ["stomped in — red hair, bushy beard","called Drake \"[quote from the chapter]\"","said \"[quote from the chapter]\""]),
 ("The Bedroom","Later that night",
   ["Drake","Bo"],
   ["had a chest & desk, shared a desk","watched the moon shine in","Bo slept peacefully"]),
 ("A Dark Cave (in his dream)","While Drake slept",
   ["Drake","dragons with green eyes"],
   ["smelled dirt, like the onions","saw brown dragons","heard a loud explosion, smoke","woke up sweating"]),
]),
("8","Flying Practice",[
 ("The Underground Hallway","Next morning, after breakfast",
   ["Rori","Drake","Griffith"],
   ["said the dragons are a secret","wondered about a dragon army","said \"[quote from the chapter]\""]),
 ("The Valley of Clouds","After the dark tunnel",
   ["Kepri","Vulcan","Shu","Drake & Worm"],
   ["reached a field of grass and hills","looped and circled in the air","flew like swimming","the Dragon Stone glowed!"]),
]),
("9","Whispers",[
 ("Griffith's Workshop","Later that week",
   ["Griffith","Drake"],
   ["taught them to shine the scales","stuck inside for three days","got a letter from his mother","must keep the dragons secret"]),
 ("Walking to the Caves","Leaving the Training Room",
   ["Rori","Ana","Drake"],
   ["whispered with a sneaky look","wondered what they were up to"]),
]),
("10","Worm's Story",[
 ("Inside Worm's Cave","Time to shine the dragons",
   ["Drake","Worm"],
   ["brought a brush, basket, towels","purred and closed his eyes","felt peaceful"]),
 ("Inside Worm's Cave","Suddenly — a vision",
   ["Drake","Worm","the king's soldiers"],
   ["his hand tingled, stuck to Worm","saw a vision — a cave, an explosion","chained Worm and dragged him out","doubted King Roland"]),
]),
("11","A Noise in the Night",[
 ("Outside Worm's Cave","After the vision",
   ["Griffith","Drake"],
   ["said soldiers captured the dragons","\"[quote from the chapter]\""]),
 ("The Bedroom","After supper",
   ["Bo","Drake"],
   ["taught Drake the alphabet","drew a D like a dragon's belly","said his Stone glowed with Worm"]),
 ("Still in the Bedroom","Just after getting into bed",
   ["Drake","two figures — Rori & Ana"],
   ["heard a loud thunk","sat up","saw them by Bo's bed"]),
]),
("12","A Sneaky Plan",[
 ("The Bedroom","Late at night",
   ["Rori & Ana","Bo","Drake"],
   ["wanted to take dragons outside while the castle slept","said it was a bad idea","agreed to go"]),
 ("Stairs & Hallways","After sneaking out",
   ["Griffith","the guard Simon","Rori"],
   ["snored — his beard flew up","was asleep at the door","lit candles for everyone"]),
 ("The Dragon Caves","Before the outside tunnel",
   ["the dragons","Worm","Drake"],
   ["woke up Vulcan, Kepri, Shu, Worm","warned \"[quote from the chapter]\"","went anyway — Worm followed"]),
]),
("13","Trouble in the Tunnel",[
 ("The Long Dark Tunnel","Walking toward outside",
   ["a red orb","Bo","Vulcan"],
   ["floated closer, getting bigger","said it wasn't Griffith's magic — scary","roared and thrashed his tail"]),
 ("The Long Dark Tunnel","Moments later",
   ["Vulcan","Drake","the tunnel"],
   ["banged his tail on the walls","yelled \"[quote from the chapter]\"","shook — dirt fell, the walls caved in"]),
]),
("14","Trapped!",[
 ("The Collapsed Tunnel","Right after the cave-in",
   ["the masters","Worm","Ana & Kepri"],
   ["candles out — very dark","had no dust on him","made a white ball of light"]),
 ("The Collapsed Tunnel","Trying to get out",
   ["Vulcan","Shu","Worm"],
   ["pushed the rock — it wouldn't budge","water might flood the tunnel","his green eyes glowed over his body"]),
]),
("15","Worm's Surprise",[
 ("The Collapsed Tunnel","When Worm starts to glow",
   ["Drake","Rori","Worm"],
   ["his Stone glowed too","thought Worm would explode","used his mind to break the rocks — the tunnel cleared"]),
 ("The Tunnel Entrance","After Worm saved everyone",
   ["Drake","Griffith & Simon"],
   ["came face-to-face with them","said the castle was awake","King Roland was furious"]),
]),
("16","Just the Beginning",[
 ("The Training Room","Returning through the tunnel",
   ["six guards","Griffith","Rori","Worm"],
   ["were waiting","said the dragons tried to escape","admitted it was her fault","saved them — turned rocks to dust"]),
 ("The Training Room","Griffith explains",
   ["Griffith","the masters"],
   ["said Earth Dragons have great power","Worm was hiding it","the Stone glows with a strong link","the red light means danger is coming"]),
 ("Walking back to Worm's Cave","At the very end",
   ["Drake","Worm"],
   ["felt a strong connection to his dragon","wouldn't go back to the onion fields","is a Dragon Master now!"]),
]),
]

models={
 "1":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "2":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "3":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "4":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "5":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "6":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "7":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "8":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "9":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "10":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "11":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "12":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "13":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "14":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "15":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
 "16":"Write the model retell for this chapter here (teacher only, 3-5 short sentences in your own words).",
}

def esc(s): return html.escape(s,quote=True)
tabs="".join(f'<button class="tab" data-ch="{c[0]}" onclick="showCh(\'{c[0]}\')">{c[0]}</button>' for c in chapters)

panels=[]
for num,title,stops in chapters:
    sh=[]
    for si,(where,when,who,did) in enumerate(stops,1):
        who_c="".join(f'<span class="chip who">{esc(x)}</span>' for x in who)
        did_c="".join(f'<span class="chip did">{esc(x)}</span>' for x in did)
        sh.append(f'''
        <div class="stop">
          <div class="badge"><div class="stopno">STOP {si}</div></div>
          <div class="body">
            <div class="meta"><span class="k">Where</span>{esc(where)}</div>
            <div class="meta"><span class="k">When</span>{esc(when)}</div>
            <div class="grouprow">
              <div class="glabel who">WHO</div>
              <div class="chips">{who_c}</div>
            </div>
            <div class="grouprow">
              <div class="glabel did">DID WHAT</div>
              <div class="chips">{did_c}</div>
            </div>
          </div>
        </div>''')
    panels.append(f'''
    <section class="panel" id="ch{num}" style="display:none">
      <h2>Chapter {num} · {esc(title)}</h2>
      {''.join(sh)}
      <details class="teacher"><summary>Model retell (teacher only)</summary><p>{esc(models[num])}</p></details>
    </section>''')

doc=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dragon Masters #{BOOK_NUM} — Key-Word Retelling</title>
<style>
  *{{box-sizing:border-box;}}
  body{{font-family:"Trebuchet MS","Segoe UI",Arial,sans-serif;color:#1A2744;margin:0;background:#fff;}}
  .wrap{{max-width:880px;margin:0 auto;padding:28px 32px 60px;}}
  h1{{text-align:center;font-size:25px;margin:0 0 4px;}}
  .sub{{text-align:center;color:#B85C00;font-size:16px;font-weight:bold;margin:0 0 6px;}}
  .howto{{text-align:center;color:#666;font-size:13.5px;margin:0 auto 8px;max-width:680px;line-height:1.55;}}
  .howto b{{color:#B85C00;}}
  .legend{{text-align:center;font-size:12.5px;color:#888;margin-bottom:18px;}}
  .legend .lw,.legend .ld{{font-weight:bold;padding:2px 9px;border-radius:999px;border:1.5px solid;}}
  .legend .lw{{color:#2C6FA8;border-color:#9CC2E2;}}
  .legend .ld{{color:#B85C00;border-color:#E8B877;}}
  .tabs{{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;position:sticky;top:0;
    background:#fff;padding:10px 0;border-bottom:1px solid #eee;z-index:5;margin-bottom:24px;}}
  .tab{{width:34px;height:34px;border:1px solid #ddd;background:#fff;color:#1A2744;border-radius:8px;
    font-size:14px;font-weight:bold;cursor:pointer;transition:.15s;}}
  .tab:hover{{border-color:#B85C00;}}
  .tab.active{{background:#B85C00;color:#fff;border-color:#B85C00;}}

  /* ── chapter prev/next (auto-added) ── */
  .tabs .navtab{{width:auto;padding:0 14px;height:34px;border:1px solid #ddd;background:#fff;color:#1A2744;
    border-radius:8px;font-size:14px;font-weight:bold;cursor:pointer;transition:.15s;white-space:nowrap;}}
  .tabs .navtab:hover{{background:#B85C00;color:#fff;border-color:#B85C00;}}
  h2{{font-size:19px;color:#B85C00;margin:0 0 18px;}}
  .stop{{display:flex;border:1px solid #ececec;border-radius:14px;overflow:hidden;margin-bottom:16px;}}
  .badge{{flex:0 0 78px;display:flex;align-items:center;justify-content:center;padding:14px 6px;border-right:1px solid #f0f0f0;}}
  .stopno{{font-size:12px;font-weight:bold;color:#B85C00;text-transform:uppercase;letter-spacing:.5px;text-align:center;line-height:1.3;}}
  .body{{flex:1;padding:14px 18px;}}
  .meta{{font-size:14.5px;margin-bottom:3px;}}
  .meta .k{{display:inline-block;min-width:52px;color:#888;font-weight:bold;font-size:12px;text-transform:uppercase;letter-spacing:.5px;}}
  .grouprow{{display:flex;align-items:flex-start;gap:12px;margin-bottom:10px;}}
  .glabel{{flex:0 0 78px;font-size:11px;font-weight:bold;text-transform:uppercase;letter-spacing:.5px;
    padding-top:7px;text-align:right;}}
  .glabel.who{{color:#2C6FA8;}} .glabel.did{{color:#B85C00;}}
  .chips{{display:flex;flex-wrap:wrap;gap:8px;flex:1;}}
  .chip{{border-radius:999px;padding:6px 14px;font-size:14.5px;font-weight:bold;background:#fff;border:1.5px solid;}}
  .chip.who{{color:#1A2744;border-color:#9CC2E2;background:#F4F9FD;}}
  .chip.did{{color:#1A2744;border-color:#E8B877;background:#FFF9F1;}}
  .teacher{{margin-top:22px;border:1px solid #eee;border-radius:12px;padding:12px 16px;background:#fafafa;}}
  .teacher summary{{font-weight:bold;cursor:pointer;font-size:13px;color:#888;}}
  .teacher p{{font-size:14px;line-height:1.55;color:#555;margin:10px 0 0;}}
  @media print{{
    .tabs{{display:none;}} .panel{{display:block!important;page-break-after:always;}}
    .teacher,.stop{{break-inside:avoid;}}
  }}
</style></head><body>
<div class="wrap">
  <h1>Dragon Masters #{BOOK_NUM} · {BOOK_TITLE}</h1>
  <div class="sub">Key-Word Retelling</div>
  <div class="howto">Each card gives you <b>Where</b> and <b>When</b>. Your job: find
    <b>WHO</b> + <b>DID WHAT</b> and say it in your own words — don't read sentences, make your own!</div>
  <div class="legend"><span class="lw">WHO</span> = the people / dragons &nbsp;·&nbsp; <span class="ld">DID WHAT</span> = the action</div>
  <div class="tabs"><button class="navtab" onclick="stepCh(-1)">← Prev</button>{tabs}<button class="navtab" onclick="stepCh(1)">Next →</button></div>
  {''.join(panels)}
</div>
<script>
  function stepCh(d){{var tabs=Array.prototype.slice.call(document.querySelectorAll('.tabs .tab'));var i=tabs.findIndex(function(t){{return t.classList.contains('active')}});var n=i+d;if(n<0||n>=tabs.length)return;showCh(tabs[n].dataset.ch);}}
  function showCh(n){{
    document.querySelectorAll('.panel').forEach(p=>p.style.display='none');
    document.getElementById('ch'+n).style.display='block';
    document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.ch===n));
    window.scrollTo({{top:0,behavior:'instant'}});
  }}
  showCh('1');
</script></body></html>'''
open(OUTFILE,"w",encoding="utf-8").write(doc)
print("wrote", OUTFILE, len(doc), "bytes")
