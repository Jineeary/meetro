<!---
حقوق الطبع والنشر 2020 The HuggingFace Team. جميع الحقوق محفوظة.

تم ترخيص هذا المستند بموجب رخصة أباتشي، الإصدار 2.0 ("الرخصة"). ما لم ينص على خلاف ذلك في الرخصة، لا يجوز لك استخدام هذا الملف. يمكنك الحصول على نسخة من الرخصة من الرابط أدناه:

    http://www.apache.org/licenses/LICENSE-2.0

ما لم يتطلب القانون المعمول به أو يتم الاتفاق كتابيًا، يتم توزيع البرنامج الموزع بموجب الرخصة "كما هو"، دون أي ضمانات أو شروط من أي نوع، سواء كانت صريحة أو ضمنية. يُرجى الرجوع إلى الرخصة للحصول على معلومات حول الأذونات والقيود.
-->

<h1 align="center">
    <p>Meetro🚇: تخطيط الاجتماعات بسهولة في محطات المترو</p>
</h1>

<p align="center">
    <a href="https://circleci.com/gh/huggingface/transformers"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/main"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/huggingface/transformers.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/transformers/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/transformers/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/transformers.svg"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
    <a href="https://zenodo.org/badge/latestdoi/155220641"><img src="https://zenodo.org/badge/155220641.svg" alt="DOI"></a>
</p>

<h4 align="center">
    <p>
        <a href="https://github.com/Jineeary/meetro/blob/main/README.md">English</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_chinese(simplified).md">简体中文</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_chinese(traditional).md">繁體中文</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_korean.md">한국어</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_spanish.md">Español</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_japanese.md">日本語</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_hindi.md">हिन्दी</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_russian.md">Русский</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_portuguese.md">Рortuguês</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_telugu.md">తెలుగు</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_french.md">Français</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_german.md">Deutsch</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_vietnamese.md">Tiếng Việt</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_urd.md">العربية</a> |
        <a href="https://github.com/Jineeary/meetro/blob/main/language/README_arabic.md">اردو</a> |
    </p>
</h4>

<h3 align="center">
    <p>انقر على الصورة أدناه لزيارة الصفحة.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="انقر على الصورة لزيارة الصفحة">
    </a>
</h3>

<h2 align="center">
    <p>الحل الأمثل للعثور على نقطة الاجتماع المركزية!</p>
</h2>

## نظرة عامة
Meetro هو خدمة ويب مبتكرة تم تصميمها لتسهيل عملية العثور على مكان اجتماع مركزي، خاصةً للأصدقاء أو المجموعات المنتشرة في أنحاء منطقة حضرية. حلنا لا يقوم فقط بحساب محطة المترو المثلى بل يقترح أيضًا معالم قريبة، مما يجعل تجربة الاجتماع أكثر متعة.

## تحديد المشكلة وتحليلها
لأصدقاء يعيشون في أماكن متفرقة، قد يكون من الصعب تحديد موقع اجتماع مركزي. المنصات الحالية مثل [WeMeetPlace](https://wemeetplace.com) و [Ya-manna](https://ya-manna.com) تحاول إيجاد نقاط مركزية، لكنها غالبًا تفتقر إلى بيانات حديثة أو أماكن مرغوبة. Meetro يجمع بين حساب النقطة المركزية مع بيانات المعالم الحالية لتقديم مواقع عملية وجذابة للقاءات.

### فرص البحث والتحسين
1. **WeMeetPlace** ([الموقع](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   يركز WeMeetPlace على إيجاد النقاط المركزية، لكنه يفتقر إلى المعالم القريبة في العديد من المحطات ويعتمد غالبًا على بيانات قديمة. هدفنا هو أن يضمن Meetro تجربة ذات صلة، تعتمد على المعالم الحالية والجذابة.

2. **Ya-manna** ([الموقع](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   بينما يتضمن Ya-manna خيارات ترفيهية، فإنه يركز على النقاط المركزية المحددة، والتي قد تفتقر إلى وجهات شهيرة. نهدف إلى معالجة ذلك من خلال إعطاء وزن أكبر للمعالم الشعبية حتى لو كانت خارج نطاق النقطة المركزية قليلاً.

من خلال معالجة هذه القيود، يقدم Meetro تجربة محسنة للمستخدمين الذين يبحثون عن أكثر من مجرد نقطة اجتماع، مما يسمح لهم بالوصول إلى مواقع ممتعة تحتوي على بيانات محدثة.

## تسمية المشروع والعلامة التجارية
**Meetro** مشتق من كلمتي "Meet" (اجتماع) و"Metro" (مترو)، مما يرمز إلى فكرة الاجتماع في محطات المترو. الاسم يركز على مناطق الحضر ويساعد في إيجاد مواقع اجتماعات مريحة وممتعة على مقربة من محطات المترو.

## بيان المهمة
"مهمتنا هي مساعدة الأصدقاء في العثور على أكثر محطات المترو ملاءمة والأماكن القريبة للاستمتاع. سواء كانت لقاءات عادية أو مناسبات خاصة، نبسط عملية اختيار المكان المثالي للاجتماع."

- **الهدف**: تطوير خدمة ويب لتحديد محطة المترو المثلى وتقديم توصيات حول المعالم الشعبية القريبة.
- **الفئة المستهدفة**: تم تصميم Meetro للأصدقاء أو العائلات أو المجموعات التي ترغب في وسيلة مريحة وفعالة لتخطيط اللقاءات في مواقع مترو مركزية.

## الميزات والوظائف
نظام Meetro الفريد لتقييم المعالم يجمع بين حساب النقاط المركزية وترتيب المعالم، مما يضمن أن يحصل المستخدمون على توصية بمحطة مترو مركزية تحتوي على مواقع شهيرة لتجربة اجتماعية ممتعة.

### الميزات الرئيسية
- **حساب النقطة المركزية بمرونة في النطاق**: بدلاً من نقطة مركزية صارمة، يحسب Meetro نقطة ضمن نطاق، مما يسمح للمستخدمين بتفضيل المحطات التي تحتوي على معالم قريبة.
- **وزن المعالم**: يعين Meetro أوزانًا للمعالم. الأماكن العادية تحصل على تصنيف 1، بينما المعالم الشهيرة (مثل المتنزهات الترفيهية، المولات) تحصل على تصنيف 3، مما يعطي الأفضلية للأماكن ذات الجاذبية العالية.
- **تقييم المحطات**: تحصل كل محطة مترو قريبة من النقطة المركزية على تقييم بناءً على القرب ووزن المعالم. المحطات الأبعد عن النقطة المركزية تحصل على تقييمات أقل، بينما تحصل المحطات ذات المعالم الشعبية على تعزيز في التقييم.
- **توصيات محسّنة**: يقدم Meetro للمستخدمين محطة المترو التي تحتوي على أعلى تقييم ضمن النطاق المركزي، مما يضمن توازنًا بين سهولة الوصول والمرح.

### ما الذي يجعل Meetro مميزًا
| الميزة                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **حساب النقطة المركزية**           | نقطة مركزية ثابتة                         | نقطة مركزية تحتوي على معالم شعبية           |
| **معلومات المعالم**                | محدودة أو قديمة                        | معالم حديثة وشعبية                          |
| **حجم البيانات**                   | صغير                                  | بيانات موسعة تغطي معالم أكثر              |
| **خيارات المستخدم**                 | محدودة                                 | مرنة، تعتمد على الشعبية والموقع              |

باستخدام بيانات حديثة وتقديم خيارات تعتمد على شعبية المعالم، يعزز Meetro تجربة تخطيط اللقاءات بشكل يتجاوز المتاح حاليًا.

## أدوات ولغات التطوير
تم تطوير Meetro بواجهة تقنية قوية لضمان الأداء الفعّال والقابلية للتوسع وتوفير واجهة مستخدم مريحة.

- **اللغات والأطر**:
  - **JavaScript (Node.js)**: يدير منطق الخلفية ودمج API.
  - **Python**: يستخدم لمعالجة البيانات، وترجيح المعالم، وتكامل الخرائط.
  - **HTML/CSS**: يحدد هيكل وتصميم واجهة المستخدم.
  - **JavaScript (React)**: ينشئ واجهة ديناميكية وتفاعلية.
- **الأدوات**:
  - **GitHub**: التحكم في الإصدارات لتتبع التقدم وتمكين التعاون الجماعي.
  - **OpenStreetMap (OSM)**: يوفر بيانات خرائط شاملة مفتوحة المصدر.
  - **Google Maps API**: يدعم عرض الخرائط، وحساب النقاط المركزية، واسترجاع بيانات المعالم.
  - **Figma**: أداة تعاونية لتصميم UI/UX، تضمن اتساق تجربة المستخدم.

## مسؤوليات الفريق
لضمان تنفيذ المشروع بسلاسة، يتمتع كل عضو في الفريق بدور محدد بوضوح:

- **قائد المشروع**: Soo-bin Yoon – يشرف على التطوير العام وتنسيق المشروع.
- **مدير الكود**: Ye-eun Yeom – يدير المستودع ودمج الكود.
- **جامع البيانات**: Yeon-jin Kim – يجمع البيانات ويعالجها، لضمان دقة المعلومات عن المعالم.
- **مصمم الموقع**: Yeo-jin Kim – يصمم ويطور واجهة الموقع لتقديم تجربة مستخدم سلسة.

## البدء السريع
لبدء استخدام Meetro، ببساطة انقر على الرابط أدناه لزيارة الموقع:

[قم بزيارة Meetro](http://localhost:3000)

## الاستخدام
1. **إدخال المواقع**: أدخل مواقع كل شخص في مجموعتك.
2. **البحث عن النقطة المركزية**: يحسب التطبيق نطاق النقطة المركزية ويعرض محطات المترو القريبة.
3. **عرض التوصيات**: المحطات التي تحتوي على أعلى التقييمات بناءً على القرب وشعبية المعالم تُقترح كنقاط لقاء.
يجعل Meetro عملية اختيار مكان اللقاء أسهل من خلال تقديم ميزات ودية وتوصيات ذات صلة.

## المساهمة
نرحب بالمساهمات لتحسين Meetro. للمساهمة، يُرجى اتباع إرشاداتنا في CONTRIBUTING.md. يمكن أن تشمل المساهمات تحسينات في الكود، أو ميزات جديدة، أو تحديثات لبيانات المعالم.

## الرخصة
تم ترخيص هذا المشروع بموجب Apache License 2.0. لمزيد من التفاصيل، راجع ملف [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE).

## العروض التوضيحية والأمثلة عبر الإنترنت
إلى جانب الميزات الرئيسية، نقدم العروض التوضيحية التالية لعرض قدرات Meetro:

1. عرض حساب النقطة المركزية: يعرض كيفية حساب Meetro للنقطة المركزية ضمن نطاق مرن ويقترح المحطات.
2. وزن المعالم: يوضح كيفية إعطاء الأولوية للأماكن الشهيرة بناءً على تفضيلات المستخدم.
3. تجربة المستخدم: تابع مجموعة مثال وهم يتنقلون في واجهة Meetro، ويجدون المكان الأمثل للقاء.
استكشف Meetro اليوم لتجربة طريقة أكثر ذكاءً للاجتماع!
