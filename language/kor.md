<!---
저작권 2020 The HuggingFace Team. 모든 권리 보유.

본 문서는 Apache License, Version 2.0 (이하 "라이선스")에 따라 라이선스됩니다.
라이선스에 따라야만 본 문서를 사용할 수 있습니다. 라이선스 사본은 아래 링크에서 확인할 수 있습니다.

    http://www.apache.org/licenses/LICENSE-2.0

법적으로 요구되거나 서면으로 동의하지 않는 한, 본 문서는 "있는 그대로"(AS IS) 제공되며 명시적 또는 묵시적인 보증이 없습니다.
라이선스에 따른 특정 권한과 제한 사항을 확인하려면 라이선스를 참조하십시오.
-->

<h1 align="center">
    <p>Meetro🚇: 지하철역에서 손쉽게 만남을 계획하세요</p>
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
    <p>아래 이미지를 클릭하여 웹페이지로 이동하세요.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="웹페이지로 이동하려면 이미지를 클릭하세요">
    </a>
</h3>

<h2 align="center">
    <p>최적의 중간 지점을 찾는 솔루션!</p>
</h2>

## 개요
Meetro는 대도시 지역에 분산된 친구나 그룹이 중앙 만남 장소를 쉽게 찾을 수 있도록 설계된 혁신적인 웹 서비스입니다. 이 솔루션은 최적의 중간 지하철역을 계산할 뿐만 아니라 인근의 인기 명소도 추천하여 더욱 즐거운 만남을 제공합니다.

## 문제 분석 및 해결방안
여러 장소에 거주하는 친구들과 중앙 만남 장소를 정하는 것은 어려운 일입니다. [WeMeetPlace](https://wemeetplace.com)와 [Ya-manna](https://ya-manna.com) 같은 기존 플랫폼은 중간 지점을 찾지만, 해당 지역의 최신 명소 정보가 부족한 경우가 많습니다. Meetro는 중간 지점 계산과 함께 최신 명소 데이터를 결합하여 실용적이고 매력적인 만남 장소를 제공합니다.

### 연구 및 개선 기회
1. **WeMeetPlace** ([웹사이트](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend)):  
   WeMeetPlace는 중간 지점만 찾을 뿐, 많은 역에 근처 명소가 부족하며 데이터가 최신이 아닙니다. Meetro는 관련성 높은 명소 기반의 경험을 제공하여 이를 개선하고자 합니다.

2. **Ya-manna** ([웹사이트](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa)):  
   Ya-manna는 여가 옵션을 포함하지만, 정확한 중간 지점을 우선시하여 인기 명소가 부족할 수 있습니다. Meetro는 조금 떨어져 있어도 인기 있는 명소를 우선시하여 이를 보완합니다.

이러한 제한점을 해결하여 Meetro는 단순한 중간 지점을 넘어서서 유저가 쉽게 즐길 수 있는 명소를 이용할 수 있도록 맞춤화된 경험을 제공합니다.

## 프로젝트 이름 및 브랜드
**Meetro**는 "Meet"와 "Metro"에서 유래된 이름으로 지하철역에서 만나는 아이디어를 나타냅니다. 이름은 지하철역을 중심으로 편리하고 즐거운 만남 장소를 찾는 것에 중점을 둡니다.

## 미션 선언문
"우리의 목표는 친구들이 가장 효율적인 지하철역과 근처의 즐길 거리를 쉽게 찾도록 돕는 것입니다. 일상적인 만남이나 특별한 모임을 위해 완벽한 만남 장소를 선택하는 과정을 단순화합니다."

- **목적**: 이상적인 지하철 중간 지점을 찾아 인기 명소를 추천하는 웹 서비스를 개발
- **대상 사용자**: Meetro는 도시 내에서 중앙 지하철역을 중심으로 모임을 자주 가지며 더 조직적인 만남 장소 선택을 원하는 친구, 가족 또는 그룹을 대상으로 합니다.

## 기능 및 기능성
Meetro의 독창적인 점수 시스템은 중간 지점 계산과 명소 순위를 결합하여, 사용자가 기억에 남는 만남을 가질 수 있도록 인근의 인기 명소와 함께 중간 지하철역을 추천합니다.

### 주요 기능
- **유연한 범위의 중간 지점 계산**: Meetro는 엄격한 중간 지점 대신, 명소가 근처에 있는 역을 우선으로 계산합니다.
- **명소 가중치**: Meetro는 명소에 가중치를 부여합니다. 일반 명소는 1점, 인기 명소(놀이공원, 쇼핑몰 등)는 3점으로 설정하여 매력도가 높은 장소에 대한 선호를 제공합니다.
- **역 점수화**: 중간 지점 근처의 각 지하철역은 접근성과 명소 가중치에 따라 점수를 받습니다. 중간 지점에서 더 멀리 떨어진 역은 점수가 낮아지며, 인기 명소가 있는 역은 보너스 점수를 받습니다.
- **최적화된 추천**: Meetro는 중간 지점 범위 내에서 가장 높은 점수를 가진 지하철역을 사용자에게 제시하여 접근성과 즐거움이 균형을 이루도록 합니다.

### 차별화: Meetro의 특별한 점
| 기능                           | WeMeetPlace /
