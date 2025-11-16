// keep selected language cached (session used server-side, but JS can read for UI)
document.addEventListener('DOMContentLoaded', () => {
  // try to get displayed language from a data attribute if present
  const langElem = document.querySelector('[data-language]');
  window.vaaniLang = langElem ? langElem.dataset.language : 'English';

  // Dummy translation map
  window._translations = {
    English: {
      intro: "Welcome to the Vocabulary Module. Let's explore some useful words!",
      practiceQ: "Translate the word 'Confidence' into your language.",
      practiceA: "Confidence"
    },
    Hindi: {
      intro: "शब्दावली मॉड्यूल में आपका स्वागत है। चलिए कुछ उपयोगी शब्द सीखते हैं!",
      practiceQ: "शब्द 'Confidence' का अनुवाद अपने भाषा में लिखें।",
      practiceA: "आत्मविश्वास"
    },
    Tamil: {
      intro: "சொல்லகராதி தொகுதிக்கு வரவேற்கிறோம். சில பயனுள்ள சொற்களை பார்க்கலாம்!",
      practiceQ: "‘Confidence’ என்ற சொல்லை உங்கள் மொழியில் மொழிபெயர்க்கவும்.",
      practiceA: "தன்னம்பிக்கை"
    },
    Telugu: {
      intro: "పదసంపద మాడ్యూల్‌కి స్వాగతం. కొన్ని ఉపయోగకరమైన పదాలను తెలుసుకుందాం!",
      practiceQ: "'Confidence' పదాన్ని మీ భాషలో అనువదించండి.",
      practiceA: "ఆత్మవిశ్వాసం"
    }
  };

  // if module_intro page, populate translation
  const introText = document.getElementById('introEnglish');
  const translatedText = document.getElementById('introTranslated');
  if (introText && translatedText){
    const selected = window._translations[window.vaaniLang] || window._translations['English'];
    introText.innerText = selected.intro;
    translatedText.innerText = selected.intro; // placeholder; for real app use real translated text
  }

  // if module_practice page, set Q & translated answer
  const questionText = document.getElementById('questionText');
  const practiceTranslation = document.getElementById('practiceTranslation');
  if (questionText && practiceTranslation){
    const selected = window._translations[window.vaaniLang] || window._translations['English'];
    questionText.innerText = selected.practiceQ;
    practiceTranslation.innerText = selected.practiceA;
  }
});

// Text-to-speech helper: idOrText can be element id or direct text
function speakText(idOrText, langCode){
  let text = '';
  if (document.getElementById(idOrText)) text = document.getElementById(idOrText).innerText;
  else text = idOrText;

  const utter = new SpeechSynthesisUtterance(text);
  if (langCode === 'Hindi') utter.lang = 'hi-IN';
  else if (langCode === 'Tamil') utter.lang = 'ta-IN';
  else if (langCode === 'Telugu') utter.lang = 'te-IN';
  else utter.lang = 'en-US';
  speechSynthesis.cancel();
  speechSynthesis.speak(utter);
}

// Practice answer check (very simple)
function checkAnswer(){
  const user = document.getElementById('userAnswer').value.trim();
  if (!user){
    alert('Please type your answer before submitting.');
    return;
  }
  // simple positive feedback — in future compare to synonyms / DB
  const tip = document.getElementById('tipText');
  tip.innerText = '✅ Nice attempt! Keep practicing.';
}
