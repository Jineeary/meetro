<!---
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<h1 align="center">
    <p>Meetro🚇: మెట్రో స్టేషన్లలో సులభమైన మీటప్ ప్లానింగ్</p>
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
    <p>క్రింద ఉన్న చిత్రంపై క్లిక్ చేయడం ద్వారా వెబ్‌పేజ్‌ను సందర్శించండి.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Click the image to visit the webpage">
    </a>
</h3>

<h2 align="center">
    <p>మధ్యబిందువును కనుగొనే ఉత్తమ పరిష్కారం!</p>
</h2>

## అవలోకనం
మీట్రో అనేది వెబ్ సర్వీస్, ఇది మిత్రులు లేదా మెట్రోపాలిటన్ ప్రాంతంలో వివిధ ప్రదేశాలలో ఉన్న గుంపులకు కేంద్ర సమావేశ ప్రదేశాన్ని కనుగొనే ప్రక్రియను సులభతరం చేయడానికి రూపొందించబడింది. మా పరిష్కారం కేవలం ఉత్తమ మధ్యబిందు మెట్రో స్టేషన్‌ను లెక్కించడమే కాకుండా, సమీప ఆకర్షణీయ ప్రదేశాలను కూడా సూచిస్తుంది, సైట్‌ల ప్రజాదరణను పరిగణనలోకి తీసుకుని మరింత ఆనందదాయకమైన సమావేశ అనుభవాన్ని అందిస్తుంది.

## సమస్య గుర్తింపు మరియు విశ్లేషణ
వివిధ ప్రదేశాలలో నివసించే మిత్రులతో, కేంద్ర సమావేశ ప్రదేశాన్ని నిర్ణయించడం సవాల్‌గా మారుతుంది. [WeMeetPlace](https://wemeetplace.com) మరియు [Ya-manna](https://ya-manna.com) వంటి ఉన్నతమైన ప్లాట్‌ఫారమ్‌లు మధ్యబిందువులను కనుగొనడానికి ప్రయత్నిస్తాయి కానీ చాలా సందర్భాల్లో ఆ ప్రదేశాలలో తాజా లేదా ఆకర్షణీయమైన ప్రదేశాలు ఉండవు. మా పరిష్కారం, మీట్రో, మధ్యబిందువు లెక్కింపు మరియు ప్రస్తుత ఆకర్షణీయ ప్రదేశాల సమాచారాన్ని కలిపి, ఉపయోగకరమైన మరియు ఆకర్షణీయమైన సమావేశ ప్రదేశాలను అందిస్తుంది.

### పరిశోధన మరియు మెరుగుదల అవకాశాలు
1. **WeMeetPlace** ([Website](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend)):    
   WeMeetPlace మధ్యబిందువులను కనుగొనడంపై దృష్టి సారిస్తుంది, కానీ అనేక స్టేషన్లలో సమీప ఆకర్షణలు లేకుండా మరియు తరచూ పాత డేటాను ఉపయోగిస్తుంది. మా లక్ష్యం Meetro ఒక సంబంధిత, ఆకర్షణ ఆధారిత అనుభవాన్ని అందించడమే.

2. **Ya-manna** ([Website](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa)):  
   Ya-manna వినోద ఎంపికలను చేర్చినప్పటికీ, అది ఖచ్చితమైన మధ్యబిందువులను ప్రాధాన్యం ఇస్తుంది, అవి ప్రజాదరణ పొందిన ప్రదేశాలను కలిగి ఉండకపోవచ్చు. ఈ సమస్యను పరిష్కరించడానికి, మేము ప్రజాదరణ పొందిన ఆకర్షణలకు ఎక్కువ బరువు ఇవ్వాలని లక్ష్యంగా పెట్టుకున్నాము, అవి మధ్యబిందు పరిధి నుండి కొంత దూరంలో ఉన్నా కూడా.

ఈ పరిమితులను పరిష్కరించడం ద్వారా, Meetro కేవలం ఒక సమావేశ స్థలాన్ని మాత్రమే కాకుండా, వినియోగదారులకు ఆకర్షణీయమైన ప్రదేశాలను సులభంగా చేరుకోవడానికి సహాయపడుతుంది, వాటి తాజా ఆకర్షణ డేటాతో.

ప్రాజెక్ట్ పేరు మరియు బ్రాండింగ్
**Meetro** అనేది “Meet” మరియు “Metro” అనే పదాల నుండి ఉద్భవించింది, ఇది మెట్రో స్టేషన్ల వద్ద సమావేశం ఆలోచనను సూచిస్తుంది. ఈ పేరు మా దృష్టిని మెట్రో ప్రాంతాలపై మరియు మెట్రో స్టేషన్ల ఆధారంగా సులభమైన, ఆనందకరమైన సమావేశ ప్రదేశాలను కనుగొనే లక్ష్యాన్ని ప్రతిబింబిస్తుంది.

## లక్ష్య ప్రకటన
“మా లక్ష్యం మిత్రులకు సులభతరంగా సమర్థవంతమైన మెట్రో స్టేషన్ మరియు సమీప ప్రదేశాలను కనుగొనడంలో సహాయపడటమే. సాధారణ సమావేశాలు అయినా, ప్రత్యేక సందర్భాలు అయినా, సరైన సమావేశ ప్రదేశాన్ని ఎంచుకునే ప్రక్రియను సులభతరం చేస్తాము.”

- **Objective**: మధ్యబిందు మెట్రో స్టేషన్‌ను కనుగొనడంలో మరియు సమీపంలోని ప్రజాదరణ పొందిన ఆకర్షణలను సూచించడంలో నైపుణ్యం కలిగిన వెబ్ సేవను అభివృద్ధి చేయడం.
- **Target Audience**: Meetro మిత్రులు, కుటుంబాలు లేదా గుంపుల కోసం రూపొందించబడింది, వీరు సులభమైన, ఆనందదాయకమైన, మరియు సమర్థవంతమైన విధానంలో కేంద్ర మెట్రో ప్రదేశాల్లో సమావేశాలను ప్లాన్ చేయాలనుకుంటున్నారు. ఇది నగరంలో తరచూ సమావేశాలు ఏర్పాటుచేసే మరియు ఒక సమృద్ధమైన, సులభమైన పరిష్కారం కోసం చూస్తున్న వారందరికీ ఉద్దేశించబడింది.
- 
## లక్షణాలు మరియు ఫంక్షనాలిటీలు
Meetro యొక్క ప్రత్యేక స్కోరింగ్ సిస్టమ్ మధ్యబిందు లెక్కింపుతో ఆకర్షణ ర్యాంకింగ్స్‌ను కలిపి, వినియోగదారులకు ప్రజాదరణ పొందిన గమ్య స్థలాలతో కూడిన ఒక కేంద్ర మెట్రో స్టేషన్‌ను సూచిస్తుంది.

### ముఖ్య లక్షణాలు
- **మధ్యబిందు లెక్కింపు విత్ ఫ్లెక్సిబుల్ పరిధి**: Meetro కఠినమైన మధ్యబిందు కాకుండా, ఒక పరిధిలో మధ్యబిందును లెక్కిస్తుంది, వినియోగదారులకు సమీప ఆకర్షణలతో ఉన్న స్టేషన్లను ప్రాధాన్యం ఇవ్వడాన్ని అనుమతిస్తుంది.
- **ఆకర్షణ లెక్కింపు**: Meetro ఆకర్షణలకు బరువు ఇచ్చింది. సాధారణ ప్రదేశాలు 1 వద్ద రేటింగ్ పొందుతాయి, పాప్యులర్ ఆకర్షణలు (ఉదాహరణకు, వినోద పార్కులు, షాపింగ్ మాల్స్) 3 వద్ద రేటింగ్ పొందుతాయి, ప్రజాదరణ ఉన్న ప్రదేశాలకు ప్రాధాన్యం ఇస్తుంది.
- **స్టేషన్ స్కోరింగ్**: మధ్యబిందు సమీపంలో ఉన్న ప్రతి మెట్రో స్టేషన్‌ను సమీపం మరియు ఆకర్షణ లెక్కింపుతో స్కోరింగ్ చేస్తుంది. మధ్యబిందు నుండి దూరంగా ఉన్న స్టేషన్లు తగ్గిన స్కోరులు పొందుతాయి, ప్రజాదరణ పొందిన ఆకర్షణలు ఉన్న స్టేషన్లు మెరుగైన స్కోరును పొందుతాయి.
- **ఆప్టిమైజ్డ్ సిఫార్సులు**: Meetro వినియోగదారులకు మధ్యబిందు పరిధిలో అత్యధిక స్కోరు ఉన్న మెట్రో స్టేషన్‌ను సూచిస్తుంది, ఇది ప్రాప్యత మరియు ఆనందం యొక్క సంతులిత మిశ్రణాన్ని నిర్ధారిస్తుంది.
- 
### వేరుబాటు: Meetro ఎందుకు ప్రత్యేకంగా ఉంది
| లక్షణం                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **మధ్యబిందు లెక్కింపు**          | స్థిరమైన మధ్యబిందు                          | ప్రజాదరణ పొందిన ఆకర్షణలతో మధ్యబిందు          |
| **ఆకర్షణ సమాచారము**           | 	పాత లేదా పరిమితమైన                     | తాజా, ట్రెండీ ఆకర్షణలు             |
| **డేటా పరిమాణం**                | చిన్న                                   | ఎక్కువ డేటా, మరిన్ని ఆకర్షణలు   |
| **వినియోగదారు ఎంపికలు**         | పరిమితమైన                                 | ప్రజాదరణ మరియు స్థానాన్ని ఆధారంగా సరికొత్త |

ప్రస్తుతం అందుబాటులో ఉన్నవాటిని మించి, Meetro ఆకర్షణ ప్రజాదరణ ఆధారంగా ఎంపికలను అందించడం ద్వారా సమావేశం ప్రణాళిక అనుభవాన్ని మెరుగుపరుస్తుంది.

## అభివృద్ధి సాధనాలు మరియు భాషలు
Meetro సమర్థవంతమైన పనితీరు, స్కేలబిలిటీ మరియు వినియోగదారుడు అనుకూల ఇంటర్ఫేస్‌ను నిర్ధారించడానికి ఒక బలమైన సాంకేతిక స్టాక్‌తో అభివృద్ధి చేయబడింది.

- **భాషలు మరియు ఫ్రేమ్‌వర్క్లు**:
  - **JavaScript (Node.js)**: బ్యాక్‌ఎండ్ లాజిక్ మరియు API ఇంటిగ్రేషన్లను నిర్వహిస్తుంది.
  - **Python**: డేటా ప్రాసెసింగ్, ఆకర్షణ బరువు మరియు మ్యాప్ ఇంటిగ్రేషన్ కోసం ఉపయోగిస్తారు.
  - **HTML/CSS**: వినియోగదారు ఇంటర్ఫేస్ యొక్క నిర్మాణం మరియు డిజైన్‌ను నిర్వచిస్తుంది.
  - **JavaScript (React)**: డైనమిక్ మరియు స్పందనాత్మక ఫ్రంటెండ్‌ను సృష్టిస్తుంది.
- **Tools**:
  - **GitHub**: పురోగతి ట్రాక్ చేయడానికి మరియు బృంద సహకారాన్ని ప్రోత్సహించడానికి సంస్కరణ నియంత్రణ.
  - **OpenStreetMap (OSM)**: విస్తృతమైన ఓపెన్-సోర్స్ మ్యాప్ డేటాను అందిస్తుంది.
  - **Google Maps API**: మ్యాప్ విజువలైజేషన్లు, మధ్యబిందు లెక్కింపులు మరియు ఆకర్షణ డేటా తిరిగి పొందడాన్ని మద్దతు చేస్తుంది.
  - **Figma**: UI/UX డిజైన్ కోసం ఒక సహకార సాధనం, వినియోగదారు అనుభవంలో స్థిరత్వాన్ని నిర్ధారిస్తుంది.

## బృంద బాధ్యతలు
సమగ్ర ప్రాజెక్ట్ అమలును నిర్ధారించడానికి, ప్రతి బృంద సభ్యుడు స్పష్టమైన పాత్రను కలిగి ఉన్నారు:

- **ప్రాజెక్ట్ నాయకుడు**: Soo-bin Yoon – మొత్తం ప్రాజెక్ట్ అభివృద్ధి మరియు సమన్వయాన్ని పర్యవేక్షిస్తారు.
- **ప్రాజెక్ట్ నాయకుడు**: Ye-eun Yeom – రిపోజిటరీ మరియు కోడ్ ఇంటిగ్రేషన్‌ను నిర్వహిస్తారు.
- **ప్రాజెక్ట్ నాయకుడు**: Yeon-jin Kim – డేటాను సేకరిస్తారు మరియు ప్రాసెస్ చేస్తారు, ఆకర్షణ సమాచారపు ఖచ్చితత్వాన్ని నిర్ధారిస్తారు.
- **ప్రాజెక్ట్ నాయకుడు**: Yeo-jin Kim – వెబ్‌సైట్ ఇంటర్ఫేస్‌ను డిజైన్ చేసి, సుళభమైన వినియోగదారు అనుభవాన్ని అందించే అభివృద్ధి చేస్తారు.

## త్వరగా ప్రారంభం
Meetro ఉపయోగం ప్రారంభించడానికి, క్రింది లింక్‌పై క్లిక్ చేసి వెబ్‌సైట్‌ను సందర్శించండి:

[Visit Meetro](http://localhost:3000)

## వినియోగం
1. **స్థానాలను ఎంటర్ చేయండి**: మీ గుంపులోని ప్రతి వ్యక్తి యొక్క స్థానాలను ఎంటర్ చేయండి.
2. **మధ్యబిందు కనుగొనండి**: అనువర్తనం ఒక మధ్యబిందు పరిధిని లెక్కించి, సమీపంలోని మెట్రో స్టేషన్లను చూపిస్తుంది.
3. **సిఫార్సులను వీక్షించండి**: సమీపత మరియు ఆకర్షణ ప్రజాదరణ ఆధారంగా ఉన్న అత్యధిక స్కోర్లతో స్టేషన్లు సమావేశం స్థలంగా సూచించబడతాయి.
Meetro వినియోగదారుడు అనుకూలమైన ఫంక్షనాలిటీ మరియు సంబంధిత సిఫార్సులను అందించడం ద్వారా సమావేశ స్థలం ప్రణాళికను సులభతరం చేస్తుంది.

## సహకారం
Meetroను మెరుగుపరిచేందుకు మేము సహకారాలను స్వాగతిస్తున్నాము. సహకరించడానికి, దయచేసి మా CONTRIBUTING.md మార్గదర్శకాలను అనుసరించండి. సహకారాలు కోడ్ అభివృద్ధులు, కొత్త లక్షణాలు లేదా ఆకర్షణ డేటా నవీకరణలను కలిగి ఉండవచ్చు.

## లైసెన్స్
ఈ ప్రాజెక్ట్ Apache License 2.0 కింద లైసెన్స్ చేయబడింది. మరిన్ని వివరాలకు, దయచేసి [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) ఫైల్ చూడండి.

## ఆన్‌లైన్ డెమోలు మరియు ఉదాహరణలు
ప్రధాన ఫంక్షనాలిటీలతో పాటు, Meetro యొక్క సామర్థ్యాలను ప్రదర్శించే క్రింది డెమోలు అందించాము:

మధ్యబిందు లెక్కింపు డెమో: Meetro ఎలా మధ్యబిందును ఒక సడలింపు పరిధిలో లెక్కించి, స్టేషన్లను సూచించేది చూపిస్తుంది.
ఆకర్షణ బరువు: వినియోగదారుల ప్రాధాన్యత ఆధారంగా ప్రజాదరణ పొందిన ప్రదేశాలను ఎలా ప్రాధాన్యం ఇవ్వబడతాయో చూపిస్తుంది.
వినియోగదారు ప్రయాణం: Meetro ఇంటర్ఫేస్‌ను ఉపయోగించి ఒక నమూనా గుంపు ఎలా గమనించి, అనుకూలమైన సమావేశ స్థలాన్ని కనుగొంటుందో చూపిస్తుంది.
Meetroను ఈ రోజు అన్వేషించండి, సమావేశం చేసుకునే మరింత తెలివైన మార్గాన్ని అనుభవించండి!
