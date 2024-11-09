<!---
版权 2020 The HuggingFace Team. 保留所有权利。

本文件依据 Apache License, Version 2.0（以下简称 "许可证"）授权。除非遵守许可证，否则不得使用本文件。可通过以下链接查看许可证副本。

    http://www.apache.org/licenses/LICENSE-2.0

除非适用法律要求或书面同意，按“现有”方式提供此文件，不含任何明示或暗示的担保。
有关许可证下的权限和限制，请参阅许可证。
-->

<h1 align="center">
    <p>Meetro🚇: 在地铁站轻松计划聚会</p>
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
    <p>点击下方图片访问网页。</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="点击图片访问网页">
    </a>
</h3>

<h2 align="center">
    <p>找到最佳中间点的解决方案！</p>
</h2>

## 概述
Meetro是一款创新的网页服务，专为帮助分散在大都市区的朋友或团队轻松找到中心聚会地点设计。我们的解决方案不仅计算最佳地铁中间站，还推荐附近的热门景点，为您带来更愉快的聚会体验。

## 问题分析与解决方案
对于住在不同地点的朋友，找到一个中心聚会地点是一项挑战。现有平台如[WeMeetPlace](https://wemeetplace.com)和[Ya-manna](https://ya-manna.com)尝试找到中间点，但往往缺乏更新的或理想的景点。Meetro结合中间点计算和最新的景点数据，为用户提供实用且吸引人的聚会地点。

### 研究和改进机会
1. **WeMeetPlace** ([网站](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace 只注重找到中间点，很多站点缺少周边景点，数据也经常是过时的。我们致力于让 Meetro 提供更相关、基于景点的体验。

2. **Ya-manna** ([网站](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna 包含娱乐选项，但更倾向于精准中间点，而中间点附近可能缺乏受欢迎的景点。我们通过在范围内优先推荐受欢迎景点来改善这一点。

通过解决这些限制，Meetro 为用户提供超越单纯中间点的体验，便于用户轻松找到周边热门景点，打造贴心的聚会地点选择。

## 项目名称与品牌
**Meetro** 的名称源于“Meet”（会面）和“Metro”（地铁），表达了在地铁站会面的理念。名称突出地铁区域为核心，提供便利、愉快的聚会地点。

## 使命宣言
“我们的使命是帮助朋友轻松找到最便捷的地铁站和附近的好去处。无论是日常聚会还是特殊场合，我们简化了选择完美聚会地点的过程。”

- **目标**：开发一个基于地铁中间点的理想聚会地点并提供热门景点推荐的网页服务。
- **目标用户**：Meetro 专为那些频繁在城市中安排聚会，且希望有更组织化方式选择聚会地点的朋友、家人或团队。

## 功能与特色
Meetro 的独特评分系统结合了中间点计算和景点评级，确保推荐的地铁站不仅在中间位置，而且附近拥有热门景点，为您带来难忘的聚会体验。

### 主要功能
- **灵活的中间点计算**：Meetro 并非严格定位中间点，而是优先计算附近有景点的站点。
- **景点权重**：Meetro 为景点分配权重。普通景点评分为 1，热门景点（如游乐园、商场）评分为 3，更偏重高吸引力的地点。
- **站点评分**：每个靠近中间点的地铁站依据距离和景点权重打分。远离中间点的站点得分降低，热门景点的站点得分提升。
- **优化推荐**：Meetro 在中间点范围内推荐评分最高的地铁站，确保平衡了便利性和乐趣。

### 差异化：Meetro 的独特之处
| 功能                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **中间点计算**           | 固定中间点                          | 带热门景点的中间点          |
| **景点信息**         | 过时或有限                     | 最新、热门景点             |
| **数据量**                    | 小                                   | 覆盖更多景点   |
| **用户选择**                   | 限制                                 | 基于景点流行度和位置的灵活选择 | 

通过利用最新数据并基于景点受欢迎程度提供选项，Meetro 提供了超越目前服务的更优聚会体验。

## 开发工具和语言
Meetro 使用坚固的技术栈开发，确保高效性能、可扩展性以及用户友好的界面。

- **语言和框架**：
  - **JavaScript (Node.js)**：处理后端逻辑和 API 集成。
  - **Python**：用于数据处理、景点权重及地图集成。
  - **HTML/CSS**：定义用户界面的结构和设计。
  - **JavaScript (React)**：创建动态和响应式的前端。
- **工具**：
  - **GitHub**：版本控制以跟踪进度并实现团队协作。
  - **OpenStreetMap (OSM)**：提供全面的开源地图数据。
  - **Google Maps API**：支持地图可视化、中间点计算和景点数据检索。
  - **Figma**：为 UI/UX 设计的协作工具，确保用户体验的一致性。

## 团队角色和职责
为确保项目的顺利执行，每位团队成员都有明确的职责：

- **项目负责人**：尹秀彬 – 负责总体项目开发和协调。
- **代码经理**：廉艺恩 – 管理存储库和代码集成。
- **数据收集员**：金妍真 – 收集并处理数据，确保景点信息的准确性。
- **网站创建者**：金丽珍 – 设计并开发网站界面，为用户提供无缝体验。

## 快速开始
要开始使用 Meetro，请点击以下链接访问网站：

[访问 Meetro](http://localhost:3000)

## 使用方法
1. **输入位置**：输入团队中每个人的位置。
2. **查找中间点**：应用计算中间点范围并推荐附近的地铁站。
3. **查看推荐**：基于位置和景点人气得分最高的站点推荐为聚会地点。
Meetro 让聚会地点选择变得更加轻松，提供简洁的功能和相关的推荐。

## 贡献
我们欢迎任何帮助改进 Meetro 的贡献。请按照我们的 CONTRIBUTING.md 指南参与。贡献内容包括代码改进、新功能或景点数据更新。

## 许可证
此项目依据 Apache License 2.0 授权。详情请参阅 [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) 文件。

## 在线演示和示例
我们提供以下演示来展示 Meetro 的功能：

1. 中间点计算演示：展示 Meetro 如何在灵活范围内计算中间点并推荐站点。
2. 景点加权：展示如何根据用户偏好优先推荐热门景点。
3. 用户旅程：跟随示例团队探索 Meetro 界面，找到最佳聚会地点。
立即体验 Meetro，探索更智能的聚会方式！
