<div dir="rtl">

# مذاكرة الـ AI من الصفر

**By Mostafa Eliwa**

كورس [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) كامل بالعربي المصري البسيط: من الرياضيات والـ Machine Learning لحد الـ Transformers والـ LLMs والـ MCP والـ Agents. **515 يوم مذاكرة**، كل يوم صفحة تفاعلية فيها:

- شرح مبسط بالعربي لكل مفاهيم الدرس، مع تشبيهات من الحياة
- معامل تفاعلية تحرّك فيها sliders وتسحب نقط وتشوف الفكرة بعينك
- الكود خطوة بخطوة، والأمر اللي تشغّله بيه عندك
- تمارين بتلميحات وإجابات، وتمرين زيادة عملي
- كويز في الآخر، وchecklist تتابع بيها نفسك
- إضافات مش موجودة في الدرس الأصلي

## ذاكر أونلاين

افتح الموقع وابدأ على طول: **https://mostafaeliwaa.github.io/ai-engineering-arabic/**

تقدمك (الأيام اللي علّمت عليها والـ checklists) بيتحفظ في متصفحك، فلو قفلت ورجعت هتلاقيه زي ما هو.

## ذاكر أوفلاين

1. نزّل الملف **[AI-Study-Offline.html](https://github.com/mostafaeliwaa/ai-engineering-arabic/releases/download/offline/AI-Study-Offline.html)** (من صفحة الـ Releases).
2. افتحه بـ Chrome أو Edge أو Firefox. مش محتاج نت.

الملف بيتحدّث لوحده كل ما أيام جديدة تتضاف.

## انقل تقدمك

في آخر خريطة المذاكرة فيه «انقل تقدمك لجهاز أو نسخة تانية»: اضغط «انسخ كود التقدم» والصق الكود في النسخة التانية (الأونلاين أو الأوفلاين أو جهاز تاني).

## عشان تشغّل الكود

الصفحات بتشرح وتوريك، والكود بتكتبه وتشغّله عندك. اعمل clone للكورس الأصلي مرة واحدة وانت معاك نت:

</div>

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
```

<div dir="rtl">

وكل يوم مكتوب فيه الأمر اللي تشغّله من جوه الفولدر ده.

## الحالة

الأيام بتتضاف بالتدريج. الأيام اللي لسه ما اتبنتش بتظهر في الخريطة مكتوب جنبها «بيتبني».

</div>

---

## English

**Arabic study edition of AI Engineering from Scratch, by Mostafa Eliwa.**

The full [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) curriculum (by Rohit Ghumare) rewritten as 515 interactive study days in simple Egyptian Arabic: explanations, hands-on in-browser labs, step-by-step code, exercises with hints, and quizzes.

- **Study online:** https://mostafaeliwaa.github.io/ai-engineering-arabic/ — progress is saved in your browser.
- **Study offline:** download [AI-Study-Offline.html](https://github.com/mostafaeliwaa/ai-engineering-arabic/releases/download/offline/AI-Study-Offline.html) and open it in any modern browser. It is rebuilt automatically on every update.
- **Move progress** between devices or between the online and offline versions with the progress code at the bottom of the study map.

### Repository layout

| Path | What it is |
|---|---|
| `index.html` | The app: study map, navigation, shared helpers and the `AI.lab` widget library |
| `manifest.json` | All 515 days: titles, durations, source lesson paths, built or not |
| `days/day-NNN.html` | One study day (HTML fragment loaded by `index.html`) |
| `tools/build_offline.py` | Builds the single-file offline version |
| `tools/lab-example.html` | Reference for the `AI.lab` widgets |

Run locally: `python3 -m http.server` in the repo folder, then open http://localhost:8000.

### Credits and license

- Original curriculum, lesson content and code: [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) © 2026 Rohit Ghumare, MIT License.
- Arabic edition, explanations, interactive labs and site: © 2026 Mostafa Eliwa, MIT License.

See [LICENSE](LICENSE).
