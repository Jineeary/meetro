<!---
Copyright 2020 The HuggingFace Team. Alle Rechte vorbehalten.

Dieses Dokument ist unter der Apache-Lizenz, Version 2.0 (die "Lizenz"), lizenziert. Sofern nicht ausdrücklich durch die Lizenz erlaubt, dürfen Sie diese Datei nicht verwenden. Eine Kopie der Lizenz ist über den folgenden Link erhältlich:

    http://www.apache.org/licenses/LICENSE-2.0

Sofern nicht durch geltendes Recht erforderlich oder schriftlich vereinbart, wird die Software, die unter der Lizenz vertrieben wird, "WIE BESEHEN" bereitgestellt, OHNE GEWÄHRLEISTUNGEN ODER BEDINGUNGEN JEGLICHER ART, sei es ausdrücklich oder stillschweigend. Weitere Informationen zu Rechten und Einschränkungen finden Sie in der Lizenz.
-->

<h1 align="center">
    <p>Meetro🚇: Einfache Planung von Treffen an U-Bahn-Stationen</p>
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
    <p>Klicken Sie auf das Bild unten, um die Webseite zu besuchen.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Klicken Sie auf das Bild, um die Webseite zu besuchen">
    </a>
</h3>

<h2 align="center">
    <p>Die optimale Lösung, um den zentralen Treffpunkt zu finden!</p>
</h2>

## Überblick
Meetro ist ein innovativer Webservice, der den Prozess der Suche nach einem zentralen Treffpunkt, insbesondere für Freunde oder Gruppen, die in einer Metropolregion verstreut sind, vereinfacht. Unsere Lösung berechnet nicht nur die optimale U-Bahn-Station, sondern schlägt auch nahegelegene Sehenswürdigkeiten vor, um das Treffen noch angenehmer zu gestalten.

## Problemidentifikation und Analyse
Für Freunde, die an verschiedenen Orten wohnen, kann es schwierig sein, einen zentralen Treffpunkt zu finden. Bestehende Plattformen wie [WeMeetPlace](https://wemeetplace.com) und [Ya-manna](https://ya-manna.com) versuchen, Mittelpunkte zu finden, bieten jedoch oft keine aktuellen oder attraktiven Sehenswürdigkeiten in der Nähe an. Meetro kombiniert die Berechnung des Mittelpunkts mit aktuellen Sehenswürdigkeiten, um praktische und ansprechende Treffpunkte zu bieten.

### Forschung und Verbesserungsmöglichkeiten
1. **WeMeetPlace** ([Website](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace konzentriert sich auf das Finden von Mittelpunkten, es fehlen jedoch oft Sehenswürdigkeiten in der Nähe vieler Stationen, und die Daten sind häufig veraltet. Unser Ziel ist es, sicherzustellen, dass Meetro eine relevante, auf Attraktionen basierende Erfahrung bietet.

2. **Ya-manna** ([Website](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna bietet Unterhaltungsoptionen an, priorisiert jedoch exakte Mittelpunkte, die möglicherweise keine beliebten Ziele enthalten. Wir streben an, dieses Problem zu beheben, indem wir beliebten Attraktionen, selbst wenn sie etwas außerhalb des Mittelpunkts liegen, eine höhere Gewichtung geben.

Durch die Beseitigung dieser Einschränkungen bietet Meetro eine auf die Nutzer abgestimmte Erfahrung, die es ermöglicht, interessante Orte mit aktuellen Attraktionsdaten leicht zu finden.

## Projektname und Branding
**Meetro** leitet sich aus den Wörtern "Meet" (Treffen) und "Metro" (U-Bahn) ab und symbolisiert die Idee, sich an U-Bahn-Stationen zu treffen. Der Name betont unseren Fokus auf urbane Bereiche und die Suche nach praktischen und angenehmen Treffpunkten.

## Leitbild
"Unsere Mission ist es, Freunden zu helfen, die bequemste U-Bahn-Station und nahegelegene Orte zu finden, um gemeinsame Zeit zu genießen. Ob für spontane Treffen oder besondere Anlässe, wir vereinfachen den Prozess, den perfekten Treffpunkt auszuwählen."

- **Ziel**: Entwicklung eines Webservices, der den idealen U-Bahn-Mittelpunkt findet und beliebte Sehenswürdigkeiten in der Nähe empfiehlt.
- **Zielgruppe**: Meetro ist für Freunde, Familien oder Gruppen konzipiert, die eine praktische, angenehme und effiziente Möglichkeit suchen, sich an zentralen U-Bahn-Orten zu treffen.

## Merkmale und Funktionen
Meetros einzigartiges Bewertungssystem kombiniert die Berechnung des Mittelpunkts mit einer Gewichtung der Sehenswürdigkeiten und stellt sicher, dass den Nutzern eine zentrale U-Bahn-Station mit beliebten Zielen für ein unvergessliches Treffen empfohlen wird.

### Hauptmerkmale
- **Mittelpunktberechnung mit flexiblem Bereich**: Anstelle eines festen Mittelpunkts berechnet Meetro einen Mittelpunkt innerhalb eines Bereichs, sodass die Nutzer Stationen mit nahegelegenen Attraktionen priorisieren können.
- **Gewichtung der Attraktionen**: Meetro weist Attraktionen Gewichtungen zu. Gewöhnliche Orte werden mit 1 bewertet, während beliebte Attraktionen (z. B. Vergnügungsparks, Einkaufszentren) eine Bewertung von 3 erhalten, wodurch attraktive Orte bevorzugt werden.
- **Bewertung der Stationen**: Jede U-Bahn-Station in der Nähe des Mittelpunkts wird basierend auf der Entfernung und der Gewichtung der Attraktionen bewertet. Stationen, die weiter vom Mittelpunkt entfernt sind, haben niedrigere Bewertungen, während Stationen mit beliebten Attraktionen einen Bonus erhalten.
- **Optimierte Empfehlungen**: Meetro zeigt den Nutzern die U-Bahn-Station mit der höchsten Bewertung innerhalb des Mittelpunktbereichs an und sorgt so für ein Gleichgewicht zwischen Erreichbarkeit und Erlebniswert.

### Besonderheit: Was Meetro auszeichnet
| Merkmal                              | WeMeetPlace / Ya-manna                   | Meetro                                      |
|--------------------------------------|------------------------------------------|---------------------------------------------|
| **Mittelpunktberechnung**            | Fester Mittelpunkt                       | Mittelpunkt mit beliebten Attraktionen      |
| **Attraktionsinformationen**         | Eingeschränkt oder veraltet              | Aktuelle und beliebte Attraktionen          |
| **Datenmenge**                       | Klein                                    | Umfangreiche Daten mit mehr Attraktionen    |
| **Nutzerwahl**                       | Eingeschränkt                            | Flexibel, basierend auf Beliebtheit und Lage|

Durch die Nutzung aktueller Daten und die Bereitstellung von Optionen, die auf der Beliebtheit der Attraktionen basieren, verbessert Meetro das Planungserlebnis für Treffen.

## Entwicklungswerkzeuge und Sprachen
Meetro wurde mit einem robusten Technologie-Stack entwickelt, um effiziente Leistung, Skalierbarkeit und eine benutzerfreundliche Oberfläche sicherzustellen.

- **Sprachen und Frameworks**:
  - **JavaScript (Node.js)**: Handhabt die Backend-Logik und API-Integrationen.
  - **Python**: Wird zur Datenverarbeitung, Gewichtung der Attraktionen und Kartenintegration verwendet.
  - **HTML/CSS**: Definiert die Struktur und das Design der Benutzeroberfläche.
  - **JavaScript (React)**: Erstellt eine dynamische und reaktionsschnelle Benutzeroberfläche.
- **Werkzeuge**:
  - **GitHub**: Versionskontrolle zur Fortschrittsverfolgung und Ermöglichung der Teamzusammenarbeit.
  - **OpenStreetMap (OSM)**: Bietet umfassende Open-Source-Kartendaten.
  - **Google Maps API**: Unterstützt die Kartenvisualisierung, die Mittelpunktberechnung und das Abrufen von Attraktionsdaten.
  - **Figma**: Ein kollaboratives Tool für UI/UX-Design, das Konsistenz im Nutzererlebnis gewährleistet.

## Teamverantwortlichkeiten
Um eine reibungslose Projektdurchführung zu gewährleisten, hat jedes Teammitglied eine klar definierte Rolle:

- **Projektleiter**: Soo-bin Yoon – Überwacht die Entwicklung und Koordination des Projekts.
- **Code-Manager**: Ye-eun Yeom – Verwaltert das Repository und die Code-Integration.
- **Daten-Sammler**: Yeon-jin Kim – Sammelt und verarbeitet die Daten und stellt die Genauigkeit der Attraktionsinformationen sicher.
- **Website-Ersteller**: Yeo-jin Kim – Entwirft und entwickelt die Website-Oberfläche, um ein nahtloses Benutzererlebnis zu bieten.

## Schnellstart
Um Meetro zu nutzen, klicken Sie einfach auf den folgenden Link, um die Website zu besuchen:

[Meetro besuchen](http://localhost:3000)

## Nutzung
1. **Standorte eingeben**: Geben Sie die Standorte jeder Person in Ihrer Gruppe ein.
2. **Mittelpunkt finden**: Die Anwendung berechnet einen Bereich um den Mittelpunkt und zeigt nahegelegene U-Bahn-Stationen an.
3. **Empfehlungen anzeigen**: Die Stationen mit den höchsten Bewertungen basierend auf Nähe und Attraktivität werden als Treffpunkte vorgeschlagen.
Meetro erleichtert die Wahl eines Treffpunkts durch benutzerfreundliche Funktionen und relevante Empfehlungen.

## Beitrag
Wir begrüßen Beiträge zur Verbesserung von Meetro. Um beizutragen, befolgen Sie bitte die Richtlinien in CONTRIBUTING.md. Beiträge können Codeverbesserungen, neue Funktionen oder Aktualisierungen der Attraktionsdaten umfassen.

## Lizenz
Dieses Projekt ist unter der Apache-Lizenz 2.0 lizenziert. Weitere Details finden Sie in der Datei [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE).

## Online-Demos und Beispiele
Zusätzlich zu den Hauptfunktionen bieten wir die folgenden Demos an, um die Möglichkeiten von Meetro zu zeigen:

1. Demo zur Mittelpunktberechnung: Zeigt, wie Meetro einen Mittelpunkt innerhalb eines flexiblen Bereichs berechnet und Stationen vorschlägt.
2. Gewichtung der Attraktionen: Zeigt, wie beliebte Orte basierend auf den Vorlieben der Benutzer priorisiert werden.
3. Benutzerreise: Folgen Sie einer Beispielgruppe, die die Meetro-Oberfläche nutzt, um den idealen Treffpunkt zu finden.
Entdecken Sie Meetro noch heute und erleben Sie eine intelligentere Art, sich zu treffen!
