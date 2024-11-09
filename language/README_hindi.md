<!---
कॉपीराइट 2020 The HuggingFace Team. सर्वाधिकार सुरक्षित।

यह दस्तावेज़ Apache License, Version 2.0 (इसके बाद "लाइसेंस" कहा गया है) के तहत लाइसेंस प्राप्त है। जब तक लाइसेंस में अनुमति न दी जाए, इस दस्तावेज़ का उपयोग नहीं किया जा सकता। आप नीचे दिए गए लिंक पर लाइसेंस की एक प्रति प्राप्त कर सकते हैं:

    http://www.apache.org/licenses/LICENSE-2.0

जब तक लागू कानून द्वारा आवश्यक न हो या लिखित में सहमति न दी गई हो, लाइसेंस के तहत वितरित सॉफ़्टवेयर "जैसा है" के आधार पर वितरित किया जाता है, बिना किसी वारंटी या शर्तों के, चाहे वह स्पष्ट हो या निहित। कृपया लाइसेंस में विशिष्ट अधिकारों और प्रतिबंधों के लिए लाइसेंस को देखें।
-->

<h1 align="center">
    <p>Meetro🚇: मेट्रो स्टेशनों पर मिलना हुआ आसान</p>
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
        <b>English</b> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hant.md">繁體中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ko.md">한국어</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_es.md">Español</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ja.md">日本語</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_hd.md">हिन्दी</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ru.md">Русский</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_pt-br.md">Рortuguês</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_te.md">తెలుగు</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_fr.md">Français</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_de.md">Deutsch</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_vi.md">Tiếng Việt</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ar.md">العربية</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ur.md">اردو</a> |
    </p>
</h4>

<h3 align="center">
    <p>वेबसाइट पर जाने के लिए नीचे दी गई तस्वीर पर क्लिक करें।</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="वेबसाइट पर जाने के लिए तस्वीर पर क्लिक करें">
    </a>
</h3>

<h2 align="center">
    <p>मिलने का सबसे उपयुक्त स्थान खोजने का समाधान!</p>
</h2>

## अवलोकन
Meetro एक अभिनव वेब सेवा है जो विशेष रूप से एक महानगरीय क्षेत्र में फैले दोस्तों या समूहों के लिए केंद्रीय मिलन स्थल ढूंढने की प्रक्रिया को आसान बनाने के लिए डिज़ाइन की गई है। हमारा समाधान न केवल सबसे उपयुक्त मेट्रो स्टेशन की गणना करता है बल्कि आस-पास के आकर्षणों को भी सुझाता है, जिससे मिलन का अनुभव और भी आनंददायक हो जाता है।

## समस्या की पहचान और विश्लेषण
विभिन्न स्थानों में रहने वाले दोस्तों के लिए एक केंद्रीय मिलन स्थल तय करना चुनौतीपूर्ण हो सकता है। मौजूदा प्लेटफार्म जैसे [WeMeetPlace](https://wemeetplace.com) और [Ya-manna](https://ya-manna.com) अक्सर इन क्षेत्रों में आकर्षण की कमी या अप्रचलित डेटा के साथ मध्य बिंदु का सुझाव देते हैं। Meetro, मध्य बिंदु की गणना को अद्यतन आकर्षण डेटा के साथ संयोजित करता है, जिससे उपयोगकर्ताओं को व्यावहारिक और आकर्षक मिलन स्थल मिल सके।

### शोध और सुधार के अवसर
1. **WeMeetPlace** ([वेबसाइट](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace मध्य बिंदु खोजने पर केंद्रित है, लेकिन कई स्टेशनों पर आसपास के आकर्षण की कमी है और अक्सर डेटा पुराना होता है। हमारा उद्देश्य Meetro को एक संबंधित, आकर्षण-आधारित अनुभव प्रदान करना है।

2. **Ya-manna** ([वेबसाइट](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna मनोरंजन के विकल्पों को शामिल करता है, लेकिन सटीक मध्य बिंदु को प्राथमिकता देता है, जिसमें लोकप्रिय गंतव्यों की कमी हो सकती है। हम इसमें सुधार के लिए लोकप्रिय आकर्षणों को अधिक महत्व देंगे, भले ही वे मध्य बिंदु से थोड़े बाहर हों।

इन सीमाओं को दूर करके, Meetro उपयोगकर्ताओं को एक ऐसा अनुभव प्रदान करता है जो केवल एक मध्य बिंदु से अधिक है, जिससे वे आसानी से आनंदमय स्थानों तक पहुंच सकते हैं।

## परियोजना का नाम और ब्रांडिंग
**Meetro** "Meet" और "Metro" से लिया गया है, जो मेट्रो स्टेशनों पर मिलने का विचार व्यक्त करता है। नाम इस बात पर जोर देता है कि हम मेट्रो क्षेत्र को केंद्र में रखकर सुविधाजनक और आनंददायक मिलन स्थल खोजने पर ध्यान केंद्रित करते हैं।

## मिशन वक्तव्य
"हमारा मिशन यह है कि हम दोस्तों को सबसे सुविधाजनक मेट्रो स्टेशन और उसके आस-पास के स्थानों को खोजने में मदद करें। चाहे वह सामान्य मुलाकात हो या विशेष अवसर, हम सही मिलन स्थल चुनने की प्रक्रिया को सरल बनाते हैं।"

- **उद्देश्य**: एक वेब सेवा विकसित करना जो मेट्रो का आदर्श मध्य बिंदु खोजती है और आस-पास के लोकप्रिय आकर्षणों की सिफारिश करती है।
- **लक्षित दर्शक**: Meetro उन दोस्तों, परिवारों या समूहों के लिए है जो एक केंद्रीय मेट्रो स्थान पर मिलने के लिए एक संगठित दृष्टिकोण की तलाश कर रहे हैं।

## विशेषताएँ और कार्यक्षमता
Meetro का अनोखा स्कोरिंग सिस्टम मध्य बिंदु की गणना को आकर्षण रैंकिंग के साथ जोड़ता है, यह सुनिश्चित करता है कि उपयोगकर्ताओं को एक केंद्रीय मेट्रो स्टेशन की सिफारिश की जाती है जो लोकप्रिय स्थलों से सुसज्जित है।

### मुख्य विशेषताएँ
- **लचीले दायरे के साथ मध्य बिंदु की गणना**: सख्त मध्य बिंदु के बजाय, Meetro एक ऐसा दायरा प्रदान करता है जिससे उपयोगकर्ता ऐसे स्टेशनों को प्राथमिकता दे सकें जिनके पास आकर्षण हों।
- **आकर्षण का भार**: Meetro आकर्षणों को वज़न देता है। सामान्य स्थानों को 1 की रेटिंग दी जाती है जबकि लोकप्रिय आकर्षणों (जैसे, मनोरंजन पार्क, मॉल) को 3 की रेटिंग दी जाती है, जिससे उच्च आकर्षण वाले स्थलों को प्राथमिकता मिलती है।
- **स्टेशन स्कोरिंग**: मध्य बिंदु के निकट प्रत्येक मेट्रो स्टेशन को निकटता और आकर्षण भार के आधार पर स्कोर किया जाता है। मध्य बिंदु से दूर स्टेशनों की स्कोर कम हो जाती है, जबकि लोकप्रिय आकर्षण वाले स्टेशनों को अतिरिक्त स्कोर मिलती है।
- **अनुकूलित सिफारिशें**: Meetro उपयोगकर्ताओं को मध्य बिंदु के दायरे में उच्चतम स्कोर वाले मेट्रो स्टेशन का सुझाव देता है, जिससे पहुंच और आनंद का संतुलन सुनिश्चित होता है।

### भिन्नता: Meetro क्यों खास है
| विशेषता                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **मध्य बिंदु की गणना**           | निश्चित मध्य बिंदु                          | लोकप्रिय आकर्षणों के साथ मध्य बिंदु         |
| **आकर्षण की जानकारी**         | सीमित या पुरानी                     | नवीनतम और लोकप्रिय आकर्षण             |
| **डेटा की मात्रा**                    | छोटा                                   | अधिक आकर्षण को कवर करने वाला विस्तृत डेटा   |
| **उपयोगकर्ता की पसंद**                   | सीमित                                 | लोकप्रियता और स्थान पर आधारित लचीला विकल्प |

नवीनतम डेटा का उपयोग करके और आकर्षण की लोकप्रियता के आधार पर विकल्प प्रदान करके, Meetro वर्तमान में उपलब्ध विकल्पों से परे एक बेहतर अनुभव प्रदान करता है।

## विकास उपकरण और भाषाएँ
Meetro को उच्च-प्रदर्शन, स्केलेबल और उपयोगकर्ता के अनुकूल इंटरफेस सुनिश्चित करने के लिए एक मजबूत तकनीकी स्टैक के साथ विकसित किया गया है।

- **भाषाएँ और फ्रेमवर्क**:
  - **JavaScript (Node.js)**: बैकएंड लॉजिक और API एकीकरण को संभालता है।
  - **Python**: डेटा प्रोसेसिंग, आकर्षण भार और मानचित्र एकीकरण के लिए उपयोग किया जाता है।
  - **HTML/CSS**: उपयोगकर्ता इंटरफ़ेस की संरचना और डिज़ाइन को परिभाषित करता है।
  - **JavaScript (React)**: एक गतिशील और प्रतिक्रियाशील फ्रंटेंड बनाता है।
- **उपकरण**:
  - **GitHub**: संस्करण नियंत्रण के माध्यम से प्रगति को ट्रैक करता है और टीम सहयोग को सक्षम करता है।
  - **OpenStreetMap (OSM)**: व्यापक ओपन-सोर्स मैप डेटा प्रदान करता है।
  - **Google Maps API**: मानचित्र दृश्य, मध्य बिंदु गणना और आकर्षण डेटा पुनर्प्राप्ति का समर्थन करता है।
  - **Figma**: UI/UX डिज़ाइन के लिए एक सहयोगी उपकरण है जो उपयोगकर्ता अनुभव में स्थिरता सुनिश्चित करता है।

## टीम की ज़िम्मेदारियाँ
परियोजना के सुचारू निष्पादन के लिए, प्रत्येक टीम सदस्य की स्पष्ट भूमिका होती है:

- **परियोजना लीडर**: Soo-bin Yoon – परियोजना विकास और समन्वय की देखरेख करते हैं।
- **कोड मैनेजर**: Ye-eun Yeom – भंडार और कोड एकीकरण का प्रबंधन करते हैं।
- **डेटा कलेक्टर**: Yeon-jin Kim – डेटा एकत्र करते हैं और प्रक्रिया को सुनिश्चित करते हैं कि आकर्षण की जानकारी सटीक हो।
- **वेबसाइट क्रिएटर**: Yeo-jin Kim – एक सहज उपयोगकर्ता अनुभव प्रदान करने के लिए वेबसाइट इंटरफ़ेस को डिज़ाइन और विकसित करते हैं।

## त्वरित शुरुआत
Meetro का उपयोग शुरू करने के लिए, बस नीचे दिए गए लिंक पर क्लिक करें और वेबसाइट पर जाएं:

[Meetro पर जाएं](http://localhost:3000)

## उपयोग
1. **स्थान दर्ज करें**: अपने समूह के प्रत्येक व्यक्ति का स्थान दर्ज करें।
2. **मध्य बिंदु खोजें**: ऐप्लिकेशन एक मध्य बिंदु सीमा की गणना करता है और निकटतम मेट्रो स्टेशनों को दिखाता है।
3. **सिफारिशें देखें**: निकटता और आकर्षण लोकप्रियता के आधार पर उच्चतम स्कोर वाले स्टेशन मिलन स्थल के रूप में सुझाए जाते हैं।
Meetro मिलन स्थल योजना को आसान बनाता है, जिससे उपयोगी सिफारिशें प्राप्त होती हैं।

## योगदान
Meetro में सुधार के लिए हम योगदान का स्वागत करते हैं। योगदान करने के लिए, कृपया हमारे CONTRIBUTING.md दिशानिर्देशों का पालन करें। योगदान में कोड में सुधार, नई सुविधाएँ या आकर्षण डेटा अपडेट शामिल हो सकते हैं।

## लाइसेंस
यह परियोजना Apache License 2.0 के तहत लाइसेंस प्राप्त है। अधिक जानकारी के लिए [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) फ़ाइल देखें।

## ऑनलाइन डेमो और उदाहरण
मुख्य कार्यात्मकताओं के अलावा, हम Meetro की क्षमताओं को दिखाने के लिए निम्नलिखित डेमो प्रदान करते हैं:

1. मध्य बिंदु गणना डेमो: दिखाता है कि Meetro कैसे एक लचीली सीमा के भीतर मध्य बिंदु की गणना करता है और स्टेशनों का सुझाव देता है।
2. आकर्षण भार: दिखाता है कि कैसे लोकप्रिय स्थानों को उपयोगकर्ता की प्राथमिकताओं के आधार पर प्राथमिकता दी जाती है।
3. उपयोगकर्ता यात्रा: एक नमूना समूह Meetro इंटरफ़ेस को नेविगेट करते हुए, आदर्श मिलन स्थल ढूंढते हुए।
आज ही Meetro का अन्वेषण करें और एक स्मार्ट तरीका अनुभव करें!