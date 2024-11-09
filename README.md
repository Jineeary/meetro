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

Meetro: Effortless Meetup Planning at Metro Stations

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
    <p>The optimal solution to find the midpoint!</p>
</h3>

<h3 align="center">
    <a href="http://127.0.0.1:5500"><img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway.png"></a>
</h3>

## Overview
Meetro is an innovative web service designed to simplify the process of finding a central meeting location, especially for friends or groups scattered across a metropolitan area. Our solution not only calculates the optimal midpoint subway station but also recommends nearby attractions, taking into account the popularity of sites to create a more enjoyable meetup experience.

## Problem Identification and Analysis
With friends living in various locations, setting a central meeting spot can be challenging. Existing platforms like [WeMeetPlace](https://wemeetplace.com) and [Ya-manna](https://ya-manna.com) attempt to find midpoints but often lack updated or desirable attractions in those areas. Our solution, Meetro, combines midpoint calculation with current attraction data to offer practical and appealing meeting spots.

### Research and Improvement Opportunities
1. **WeMeetPlace** ([Website](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend)):  
   WeMeetPlace focuses on locating midpoints but lacks nearby attractions at many stations and often uses outdated data. Our goal is to ensure that Meetro provides a relevant, attraction-based experience.

2. **Ya-manna** ([Website](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa)):  
   While Ya-manna includes entertainment options, it prioritizes exact midpoints, which might lack popular destinations. We aim to address this by weighting popular attractions higher, even if they fall slightly outside the midpoint range.

By addressing these limitations, Meetro provides an experience tailored to users looking for more than just a meeting point, allowing them to easily access enjoyable spots with updated attraction data.

## Project Naming and Branding
**Meetro** is derived from “Meet” and “Metro,” representing the idea of meeting at subway stations. The name emphasizes our focus on metro areas and finding convenient, enjoyable meeting spots based on subway stations.

## Mission Statement
"Our mission is to help friends effortlessly find the most efficient subway station and nearby places to enjoy. Whether for casual meetups or special occasions, we simplify the process of choosing the perfect meeting spot."

- **Objective**: Develop a web service that locates the ideal subway midpoint and provides recommendations for nearby popular attractions.
- **Target Audience**: Meetro is designed for friends, families, or groups who want a convenient, enjoyable, and efficient way to plan meetups at central subway locations. This includes anyone who frequently arranges meetups across a city and is looking for a more organized approach to choosing meeting spots.

## Features and Functionalities
Meetro’s unique scoring system combines midpoint calculations with attraction rankings, ensuring that users are recommended a central subway station equipped with popular destinations for a memorable meetup.

### Key Features
- **Midpoint Calculation with Flexible Range**: Instead of a strict midpoint, Meetro calculates a midpoint within a range, allowing users to prioritize stations with nearby attractions.
- **Attraction Weighting**: Meetro assigns weights to attractions. Common places are rated at 1, while popular attractions (e.g., amusement parks, shopping malls) are rated at 3, providing a preference for sites with high appeal.
- **Station Scoring**: Each subway station near the midpoint is scored based on proximity and attraction weighting. Stations further from the midpoint have reduced scores, while stations with popular attractions receive a boost.
- **Optimized Recommendations**: Meetro presents users with the subway station that has the highest score within the midpoint range, ensuring a balanced blend of accessibility and enjoyment.

### Differentiation: Why Meetro Stands Out
| Feature                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **Midpoint Calculation**           | Fixed midpoint                          | Midpoint with popular attractions          |
| **Attraction Information**         | Outdated or limited                     | Up-to-date, trendy attractions             |
| **Data Volume**                    | Small                                   | Extensive data covering more attractions   |
| **User Choices**                   | Limited                                 | Flexible, based on popularity and location |

By leveraging current data and providing options based on attraction popularity, Meetro enhances the meetup planning experience beyond what’s currently available.

## Development Tools and Languages
Meetro is developed with a robust technical stack to ensure efficient performance, scalability, and a user-friendly interface.

- **Languages and Frameworks**:
  - **JavaScript (Node.js)**: Handles backend logic and API integrations.
  - **Python**: Used for data processing, attraction weighting, and map integration.
  - **HTML/CSS**: Defines the structure and design of the user interface.
  - **JavaScript (React)**: Creates a dynamic and responsive frontend.
- **Tools**:
  - **GitHub**: Version control to track progress and enable team collaboration.
  - **OpenStreetMap (OSM)**: Provides comprehensive open-source map data.
  - **Google Maps API**: Supports map visualizations, midpoint calculations, and attraction data retrieval.
  - **Figma**: A collaborative tool for UI/UX design, ensuring consistency in the user experience.

## Team Responsibilities
To ensure smooth project execution, each team member has a clearly defined role:

- **Project Leader**: Soo-bin Yoon – Oversees overall project development and coordination.
- **Code Manager**: Ye-eun Yeom – Manages the repository and code integration.
- **Data Collector**: Yeon-jin Kim – Gathers and processes data, ensuring the accuracy of attraction information.
- **Website Creator**: Yeo-jin Kim – Designs and develops the website interface to deliver a seamless user experience.

## Installation
To install and run Meetro locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/team9/meetro.git

2. Navigate to the project directory:
   ```bash
   cd meetro

3. Install the necessary dependencies:
   ```bash
   npm install

## Quick Start
1. Run the application:
   ```bash
   npm start

2. Open your browser and navigate to http://localhost:3000 to access the web interface.

## Usage
1. **Input Locations**: Enter the locations of each person in your group.
2. **Find Midpoint**: The application calculates a midpoint range and presents nearby subway stations.
3. **View Recommendations**: Stations with the highest scores based on proximity and attraction popularity are suggested as meetup locations.
Meetro makes planning a meeting spot as easy as possible by offering user-friendly functionality and relevant recommendations.

## Contributing
We welcome contributions to help improve Meetro. To contribute, please follow our CONTRIBUTING.md guidelines. Contributions can include code improvements, new features, or updates to attraction data.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Online Demos and Examples
In addition to the main functionalities, we provide the following demos to showcase Meetro’s capabilities:

1. Midpoint Calculation Demo: Demonstrates how Meetro calculates a midpoint within a flexible range and suggests stations.
2. Attraction Weighting: Shows how popular locations are prioritized based on user preferences.
3. User Journey: Follow a sample group navigating the Meetro interface, finding the optimal meeting spot.
Explore Meetro today to experience a smarter way to meet up!
