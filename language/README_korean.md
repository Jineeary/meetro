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

https://github.com/Jineeary/meetro/blob/main/README.md

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
| 기능                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **중간 지점 계산**           | 고정 중간 지점                          | 인기 명소가 있는 중간 지점          |
| **명소 정보**         | 제한적이고 구식 정보                     | 최신 트렌드 명소             |
| **데이터 양**                    | 적음                                   | 더 많은 명소를 다룸   |
| **사용자 선택**                   | 제한적                                 | 인기와 위치에 따른 유연한 선택 | 

최신 데이터를 활용하고 명소의 인기를 기반으로 선택 옵션을 제공함으로써 Meetro는 더 나은 만남 계획 경험을 제공합니다.

## 개발 도구 및 언어
Meetro는 효율적인 성능, 확장성, 사용자 친화적인 인터페이스를 보장하기 위해 견고한 기술 스택을 사용하여 개발되었습니다.

- **언어 및 프레임워크**:
  - **JavaScript (Node.js)**: 백엔드 로직 및 API 통합을 처리
  - **Python**: 데이터 처리, 명소 가중치, 지도 통합에 사용
  - **HTML/CSS**: 사용자 인터페이스 구조 및 디자인 정의
  - **JavaScript (React)**: 동적이고 반응형 프론트엔트 구현
- **도구**:
  - **GitHub**: 버전 관리를 통해 진행 상황을 추적하고 팀 협업을 지원
  - **OpenStreetMap (OSM)**: 종합적인 오픈 소스 지도 데이터 제공
  - **Google Maps API**: 지도 시각화, 중간 지점 계산, 명소 데이터 수집 지원
  - **Figma**: 일관된 사용자 경험을 위한 UI/UX 디자인 협업 도구

## 팀 역할 및 책임
프로젝트 실행의 원활함을 위해 각 팀원은 명확한 역할을 수행합니다:

- **프로젝트 리더**: 윤수빈 – 전체 프로젝트 개발 및 조정
- **코드 관리자**: 염예은 – 저장소 및 코드 통합 관리
- **데이터 수집자**: 김연진 – 명소 정보의 정확성을 보장하며 데이터 수집 및 처리
- **웹사이트 제작자**: 김여진 – 웹사이트 인터페이스 설계 및 개발로 매끄러운 사용자 경험 제공

## 빠른 시작
Meetro를 시작하려면 아래 링크를 클릭하여 웹사이트로 이동하세요:

[Meetro 방문하기](http://localhost:3000)

## 사용법
1. **위치 입력**: 그룹 내 각 인원의 위치를 입력하세요.
2. **중간 지점 찾기**: 애플리케이션은 중간 지점 범위를 계산하고 인근 지하철역을 제시합니다.
3. **추천 보기**: 접근성과 명소 인기를 기반으로 최고 점수를 받은 역이 만남 장소로 추천됩니다.
Meetro는 사용자가 편리하게 만나볼 수 있는 장소를 제공하여 만남 장소 선택을 더욱 쉽게 만듭니다.

## 기여
Meetro를 개선하는 데 도움이 될 기여를 환영합니다. 기여하려면 CONTRIBUTING.md 지침을 따르세요. 기여 사항은 코드 개선, 새로운 기능 또는 명소 데이터 업데이트를 포함할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) 파일을 참조하세요.

## 온라인 데모 및 예시
Meetro의 기능을 보여주기 위해 아래 데모를 제공합니다:

1. 중간 지점 계산 데모: Meetro가 유연한 범위 내에서 중간 지점을 계산하고 역을 추천하는 방법을 보여줍니다.
2. 명소 가중치: 인기 있는 장소가 사용자 선호도에 따라 우선시되는 모습을 보여줍니다.
3. 사용자 여정: 샘플 그룹이 Meetro 인터페이스를 탐색하여 최적의 만남 장소를 찾는 과정을 따릅니다.
Meetro를 경험하여 더 스마트한 만남 방식을 확인해보세요!
