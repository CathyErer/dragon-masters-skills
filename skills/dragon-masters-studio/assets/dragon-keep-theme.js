(function(){
  // Works with both "Day N" (10-day pacing) and "Ch N" (per-chapter) titles.
  var match=document.title.match(/\b(?:Day|Ch(?:apter)?)\s*(\d+)\b/i);
  if(!match)return;

  // Hero art is OPTIONAL. Point ART_BASE at a folder of chapter art you own,
  // relative to the lesson HTML (e.g. 'assets/art/'). Leave '' to skip art —
  // the parchment hero renders fine without an image.
  var ART_BASE='';
  var STONE_LABEL=/\bDay\b/i.test(document.title)?'DAY ':'CH ';

  var day=Number(match[1]);
  var chapters={
    1:{label:'CHAPTER ONE · THE CALL',art:'ch01-onion-farm-v2-web.webp',position:'43%'},
    2:{label:'CHAPTER TWO · THE DRAGON STONE',art:'ch02-workshop-v2-web.webp',position:'50%'},
    3:{label:'CHAPTER THREE · MORE DRAGONS',art:'ch03-dragon-room-v2-web.webp',position:'48%'},
    4:{label:'CHAPTERS FOUR–FIVE · FIRST TRAINING',art:'ch05-training-room-v2-web.webp',position:'52%'},
    5:{label:'CHAPTERS SIX–SEVEN · NEW FRIENDS',art:'ch07-dream-cave-v2-web.webp',position:'50%'},
    6:{label:'CHAPTERS EIGHT–NINE · FLIGHT & WHISPERS',art:'ch08-valley-clouds-v2-web.webp',position:'48%'},
    7:{label:"CHAPTERS TEN–ELEVEN · WORM'S STORY",art:'ch10-worm-care-v3-web.webp',position:'50%'},
    8:{label:'CHAPTERS TWELVE–THIRTEEN · THE SNEAKY PLAN',art:'ch13-red-orb-tunnel-v2-web.webp',position:'50%'},
    9:{label:'CHAPTERS FOURTEEN–FIFTEEN · TRAPPED',art:'ch14-trapped-glow-v2-web.webp',position:'50%'},
    10:{label:'CHAPTER SIXTEEN · THE BOND',art:'ch16-final-bond-v2-web.webp',position:'50%'}
  };
  var chapter=chapters[day];
  if(!chapter)return;

  var doc=document.getElementById('doc');
  var hero=doc&&doc.querySelector('header.ed');
  if(hero){
    hero.classList.add('dragon-hero');
    hero.setAttribute('data-chapter-label',chapter.label);
    if(ART_BASE&&chapter.art){hero.style.setProperty('--hero-art','url("'+ART_BASE+chapter.art+'")');}
    hero.style.setProperty('--hero-position',chapter.position);
  }

  var progress=document.querySelector('.dragon-progress');
  if(!progress){
    progress=document.createElement('section');
    progress.className='dragon-progress';
    progress.setAttribute('aria-label','Dragon Stone course progress');

    var kicker=document.createElement('span');
    kicker.className='progress-kicker';
    var totalStones=Object.keys(chapters).length;
    kicker.textContent='Dragon Stone Course Path · '+totalStones+' Lessons';
    progress.appendChild(kicker);

    var track=document.createElement('div');
    track.className='stone-track';
    for(var i=1;i<=totalStones;i++){
      var stone=document.createElement('div');
      stone.className='stone';
      var label=document.createElement('span');
      label.textContent=STONE_LABEL+i;
      stone.appendChild(label);
      track.appendChild(stone);
    }
    progress.appendChild(track);

    var toolbar=document.querySelector('.toolbar');
    if(toolbar)toolbar.parentNode.insertBefore(progress,toolbar);
  }

  progress.querySelectorAll('.stone').forEach(function(stone,index){
    var active=index===day-1;
    stone.classList.toggle('current',active);
    if(active)stone.setAttribute('aria-current','step');
    else stone.removeAttribute('aria-current');
  });

  var tabMarks=['Aa','↟','◆','✦'];
  if(doc){
    doc.querySelectorAll('.tab').forEach(function(tab,index){
      if(!tab.querySelector('.tab-icon')){
        var mark=document.createElement('span');
        mark.className='tab-icon';
        mark.setAttribute('aria-hidden','true');
        mark.textContent=tabMarks[index]||'◆';
        tab.insertBefore(mark,tab.firstChild);
      }
    });
  }
})();
