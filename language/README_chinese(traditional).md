<!---
版權 2020 The HuggingFace Team. 保留所有權利。

本文件依據 Apache License, Version 2.0（以下簡稱“許可證”）授權。除非遵守許可證，否則不得使用本文件。可通過以下鏈接查看許可證副本。

    http://www.apache.org/licenses/LICENSE-2.0

除非適用法律要求或書面同意，否則按“現狀”（AS IS）提供本文件，不含任何明示或暗示的擔保。
有關許可證下的權利和限制，請參閱許可證。
-->

<h1 align="center">
    <p>Meetro🚇: 在地鐵站輕鬆規劃聚會</p>
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
    <p>點擊下方圖片訪問網頁。</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="點擊圖片訪問網頁">
    </a>
</h3>

<h2 align="center">
    <p>找到最佳中間點的解決方案！</p>
</h2>

## 概述
Meetro是一款創新的網頁服務，專為幫助分散在大都市區的朋友或團隊輕鬆找到中心聚會地點設計。我們的解決方案不僅計算最佳地鐵中間站，還推薦附近的熱門景點，為您帶來更愉快的聚會體驗。

## 問題分析與解決方案
對於住在不同地點的朋友，找到一個中心聚會地點是一項挑戰。現有平台如[WeMeetPlace](https://wemeetplace.com)和[Ya-manna](https://ya-manna.com)嘗試找到中間點，但往往缺乏更新的或理想的景點。Meetro結合中間點計算和最新的景點數據，為用戶提供實用且吸引人的聚會地點。

### 研究和改進機會
1. **WeMeetPlace** ([網站](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace只注重找到中間點，很多站點缺少周邊景點，數據也經常是過時的。Meetro致力於讓用戶提供更多基於景點的體驗。

2. **Ya-manna** ([網站](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna包含娛樂選項，但更傾向於精確中間點，而中間點附近可能缺乏受歡迎的景點。我們通過在範圍內優先推薦受歡迎景點來改善這一點。

通過解決這些限制，Meetro為用戶提供超越單純中間點的體驗，便於用戶輕鬆找到周邊熱門景點，打造貼心的聚會地點選擇。

## 項目名稱與品牌
**Meetro** 的名稱源於「Meet」（會面）和「Metro」（地鐵），表達了在地鐵站會面的理念。名稱突出地鐵區域為核心，提供便利、愉快的聚會地點。

## 使命宣言
「我們的使命是幫助朋友輕鬆找到最便捷的地鐵站和附近的好去處。無論是日常聚會還是特殊場合，我們簡化了選擇完美聚會地點的過程。」

- **目標**：開發基於地鐵中間點的理想聚會地點並提供熱門景點推薦的網頁服務。
- **目標用戶**：Meetro專為那些頻繁在城市中安排聚會，且希望有更組織化方式選擇聚會地點的朋友、家人或團隊。

## 功能與特點
Meetro的獨特評分系統結合了中間點計算和景點評級，確保推薦的地鐵站不僅在中間位置，而且附近擁有熱門景點，為您帶來難忘的聚會體驗。

### 主要功能
- **靈活的中間點計算**：Meetro並非嚴格定位中間點，而是優先計算附近有景點的站點。
- **景點評分**：Meetro為景點分配權重。普通景點評分為1，熱門景點（如遊樂園、購物中心等）評分為3，更偏重高吸引力的地點。
- **站點評分**：每個靠近中間點的地鐵站依據距離和景點權重打分。遠離中間點的站點得分降低，熱門景點的站點得分提升。
- **優化推薦**：Meetro在中間點範圍內推薦評分最高的地鐵站，確保平衡了便利性和樂趣。

### 差異化：Meetro的獨特之處
| 功能                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **中間點計算**           | 固定中間點                          | 帶熱門景點的中間點          |
| **景點信息**         | 過時或有限                     | 最新、熱門景點             |
| **數據量**                    | 小                                   | 覆蓋更多景點   |
| **用戶選擇**                   | 限制                                 | 基於景點流行度和位置的靈活選擇 | 

通過利用最新數據並基於景點受歡迎程度提供選項，Meetro提供了超越目前服務的更優聚會體驗。

## 開發工具和語言
Meetro使用堅固的技術棧開發，確保高效性能、可擴展性以及用戶友好的界面。

- **語言和框架**：
  - **JavaScript (Node.js)**：處理後端邏輯和 API 集成。
  - **Python**：用於數據處理、景點權重及地圖集成。
  - **HTML/CSS**：定義用戶界面的結構和設計。
  - **JavaScript (React)**：創建動態和響應式的前端。
- **工具**：
  - **GitHub**：版本控制以跟蹤進度並實現團隊協作。
  - **OpenStreetMap (OSM)**：提供全面的開源地圖數據。
  - **Google Maps API**：支持地圖可視化、中間點計算和景點數據檢索。
  - **Figma**：為 UI/UX 設計的協作工具，確保用戶體驗的一致性。

## 團隊角色和職責
為確保項目的順利執行，每位團隊成員都有明確的職責：

- **項目負責人**：尹秀彬 – 負責整體項目開發和協調。
- **代碼經理**：廉藝恩 – 管理存儲庫和代碼集成。
- **數據收集員**：金妍真 – 收集並處理數據，確保景點信息的準確性。
- **網站創建者**：金麗珍 – 設計並開發網站界面，為用戶提供無縫體驗。

## 快速開始
要開始使用 Meetro，請點擊以下鏈接訪問網站：

[訪問 Meetro](http://localhost:3000)

## 使用方法
1. **輸入位置**：輸入團隊中每個人的位置。
2. **查找中間點**：應用計算中間點範圍並推薦附近的地鐵站。
3. **查看推薦**：基於位置和景點人氣得分最高的站點推薦為聚會地點。
Meetro 讓聚會地點選擇變得更加輕鬆，提供簡潔的功能和相關的推薦。

## 貢獻
我們歡迎任何幫助改進 Meetro 的貢獻。請按照我們的 CONTRIBUTING.md 指南參與。貢獻內容包括代碼改進、新功能或景點數據更新。

## 許可證
此項目依據 Apache License 2.0 授權。詳情請參閱 [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) 文件。

## 在線演示和示例
我們提供以下演示來展示 Meetro 的功能：

1. 中間點計算演示：展示 Meetro 如何在靈活範圍內計算中間點並推薦站點。
2. 景點加權：展示如何根據用戶偏好優先推薦熱門景點。
3. 用戶旅程：跟隨示例團隊探索 Meetro 界面，找到最佳聚會地點。
立即體驗 Meetro，探索更智能的聚會方式！
