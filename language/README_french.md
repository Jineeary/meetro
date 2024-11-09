<!---
Copyright 2020 The HuggingFace Team. Tous droits réservés.

Ce document est sous licence Apache, version 2.0 (la "Licence"). Sauf autorisation explicite dans la Licence, vous ne pouvez pas utiliser ce fichier. Vous pouvez obtenir une copie de la Licence via le lien ci-dessous :

    http://www.apache.org/licenses/LICENSE-2.0

Sauf si requis par la loi applicable ou convenu par écrit, le logiciel distribué sous la Licence est distribué "EN L'ÉTAT", SANS GARANTIES NI CONDITIONS D'AUCUNE SORTE, explicites ou implicites. Consultez la Licence pour connaître les droits et restrictions.
-->

<h1 align="center">
    <p>Meetro🚇 : Planification facile de rencontres aux stations de métro</p>
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
    <p>Cliquez sur l'image ci-dessous pour visiter la page web.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Cliquez sur l'image pour visiter la page web">
    </a>
</h3>

<h2 align="center">
    <p>La solution optimale pour trouver un point de rencontre central !</p>
</h2>

## Aperçu
Meetro est un service web innovant conçu pour simplifier le processus de recherche d'un lieu de rencontre central, spécialement pour les amis ou les groupes dispersés dans une zone urbaine. Notre solution calcule non seulement la station de métro centrale optimale, mais recommande également des attractions à proximité pour rendre la rencontre plus agréable.

## Identification et analyse du problème
Pour les amis vivant dans différents endroits, trouver un lieu de rencontre central peut être un défi. Les plateformes existantes comme [WeMeetPlace](https://wemeetplace.com) et [Ya-manna](https://ya-manna.com) essaient de trouver des points centraux mais manquent souvent d'attractions intéressantes ou de données mises à jour. Meetro combine le calcul du point central avec des données actuelles pour offrir des lieux de rencontre pratiques et attrayants.

### Opportunités de recherche et d'amélioration
1. **WeMeetPlace** ([Site web](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace se concentre sur la localisation de points centraux, mais manque d'attractions à proximité dans de nombreuses stations et utilise souvent des données obsolètes. Notre objectif est de garantir que Meetro fournisse une expérience basée sur des attractions pertinentes et mises à jour.

2. **Ya-manna** ([Site web](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Bien que Ya-manna inclue des options de divertissement, il priorise des points centraux exacts, qui peuvent manquer de destinations populaires. Nous visons à pallier cela en attribuant une importance accrue aux attractions populaires, même si elles sont légèrement en dehors de la zone centrale.

En traitant ces limitations, Meetro fournit une expérience adaptée aux utilisateurs recherchant plus qu'un simple point de rencontre, en permettant un accès facile à des lieux intéressants avec des données d'attractions à jour.

## Nom et marque du projet
**Meetro** est dérivé de "Meet" (rencontre) et "Metro" (métro), représentant l'idée de se rencontrer aux stations de métro. Le nom met l'accent sur notre focalisation sur les zones urbaines et la recherche de lieux de rencontre agréables et pratiques.

## Déclaration de mission
"Notre mission est d'aider les amis à trouver la station de métro la plus pratique et les lieux à proximité pour en profiter. Que ce soit pour des rencontres informelles ou des occasions spéciales, nous simplifions le processus de choix du lieu de rencontre parfait."

- **Objectif**: Développer un service web qui localise la station de métro centrale idéale et fournit des recommandations pour des attractions populaires à proximité.
- **Public cible**: Meetro est conçu pour les amis, familles ou groupes qui recherchent un moyen pratique, agréable et efficace de planifier des rencontres dans des lieux centraux en métro.

## Caractéristiques et fonctionnalités
Le système de notation unique de Meetro combine les calculs du point central avec un classement des attractions, garantissant que les utilisateurs se voient recommander une station de métro centrale équipée de destinations populaires pour un moment de rencontre mémorable.

### Principales caractéristiques
- **Calcul du point central avec plage flexible**: Au lieu d'un point central strict, Meetro calcule un point dans une plage, permettant aux utilisateurs de prioriser les stations avec des attractions à proximité.
- **Pondération des attractions**: Meetro attribue des poids aux attractions. Les lieux communs sont notés 1, tandis que les attractions populaires (ex : parcs d'attractions, centres commerciaux) sont notées 3, offrant une préférence aux sites à fort attrait.
- **Évaluation des stations**: Chaque station de métro proche du point central est notée en fonction de sa proximité et de la pondération des attractions. Les stations éloignées du point central ont des scores réduits, tandis que les stations avec des attractions populaires bénéficient d'un bonus.
- **Recommandations optimisées**: Meetro propose aux utilisateurs la station de métro ayant le score le plus élevé dans la plage centrale, garantissant un équilibre entre accessibilité et plaisir.

### Ce qui rend Meetro unique
| Caractéristique                     | WeMeetPlace / Ya-manna                | Meetro                                    |
|-------------------------------------|---------------------------------------|-------------------------------------------|
| **Calcul du point central**         | Point central fixe                    | Point central avec attractions populaires |
| **Informations sur les attractions**| Limitées ou obsolètes                 | Attractions actuelles et populaires       |
| **Volume de données**               | Petit                                 | Données étendues couvrant plus d'attractions |
| **Choix de l'utilisateur**          | Limité                                | Flexible, basé sur la popularité et l'emplacement |

En utilisant des données actualisées et en fournissant des options basées sur la popularité des attractions, Meetro améliore l'expérience de planification des rencontres.

## Outils et langages de développement
Meetro est développé avec une pile technologique robuste pour assurer des performances efficaces, une évolutivité et une interface utilisateur conviviale.

- **Langages et frameworks**:
  - **JavaScript (Node.js)**: Gère la logique backend et les intégrations API.
  - **Python**: Utilisé pour le traitement des données, la pondération des attractions et l'intégration des cartes.
  - **HTML/CSS**: Définit la structure et le design de l'interface utilisateur.
  - **JavaScript (React)**: Crée une interface dynamique et réactive.
- **Outils**:
  - **GitHub**: Contrôle de version pour suivre les progrès et permettre la collaboration en équipe.
  - **OpenStreetMap (OSM)**: Fournit des données cartographiques complètes en open source.
  - **Google Maps API**: Supporte la visualisation des cartes, les calculs de points centraux et la récupération de données d'attractions.
  - **Figma**: Un outil collaboratif pour la conception UI/UX, assurant une cohérence dans l'expérience utilisateur.

## Responsabilités de l'équipe
Pour garantir une exécution fluide du projet, chaque membre de l'équipe a un rôle clairement défini :

- **Chef de projet**: Soo-bin Yoon – Supervise le développement et la coordination générale du projet.
- **Responsable du code**: Ye-eun Yeom – Gère le dépôt et l'intégration du code.
- **Collecteur de données**: Yeon-jin Kim – Rassemble et traite les données, garantissant l'exactitude des informations sur les attractions.
- **Créateur du site**: Yeo-jin Kim – Conçoit et développe l'interface du site pour une expérience utilisateur fluide.

## Démarrage rapide
Pour commencer à utiliser Meetro, cliquez simplement sur le lien ci-dessous pour visiter le site :

[Visiter Meetro](http://localhost:3000)

## Utilisation
1. **Saisir les emplacements** : Entrez les emplacements de chaque personne de votre groupe.
2. **Trouver le point central** : L'application calcule une plage autour du point central et affiche les stations de métro à proximité.
3. **Voir les recommandations** : Les stations ayant les scores les plus élevés, basés sur la proximité et la popularité des attractions, sont suggérées comme lieux de rencontre.
Meetro rend le choix du lieu de rencontre plus facile en offrant des fonctionnalités conviviales et des recommandations pertinentes.

## Contribution
Nous accueillons les contributions pour améliorer Meetro. Pour contribuer, veuillez suivre les directives dans CONTRIBUTING.md. Les contributions peuvent inclure des améliorations de code, de nouvelles fonctionnalités ou des mises à jour des données d'attractions.

## Licence
Ce projet est sous licence Apache 2.0. Voir le fichier [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) pour plus de détails.

## Démos et exemples en ligne
En plus des fonctionnalités principales, nous fournissons les démos suivantes pour présenter les capacités de Meetro :

1. Démo de calcul du point central : montre comment Meetro calcule un point central dans une plage flexible et propose des stations.
2. Pondération des attractions : montre comment les lieux populaires sont priorisés en fonction des préférences des utilisateurs.
3. Parcours utilisateur : suivez un groupe exemple naviguant dans l'interface de Meetro pour trouver le lieu de rencontre idéal.
Explorez Meetro dès aujourd'hui pour découvrir une façon plus intelligente de se rencontrer !
