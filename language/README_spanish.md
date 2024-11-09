<!---
Derechos de autor 2020 The HuggingFace Team. Todos los derechos reservados.

Este documento está licenciado bajo la Licencia Apache, Versión 2.0 (la "Licencia"). Excepto cuando se indique lo contrario en la Licencia, no puede utilizar este archivo. Puede obtener una copia de la Licencia en el siguiente enlace:

    http://www.apache.org/licenses/LICENSE-2.0

Salvo cuando la ley aplicable lo requiera o se haya acordado por escrito, el software distribuido bajo la Licencia se distribuye "TAL CUAL", SIN GARANTÍAS NI CONDICIONES DE NINGÚN TIPO, ya sean expresas o implícitas. Consulte la Licencia para conocer el lenguaje específico que rige los permisos y limitaciones en virtud de la Licencia.
-->

<h1 align="center">
    <p>Meetro🚇: Planificación de encuentros en estaciones de metro</p>
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
    <p>Haz clic en la imagen de abajo para visitar la página web.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Haz clic en la imagen para visitar la página web">
    </a>
</h3>

<h2 align="center">
    <p>¡La solución óptima para encontrar el punto medio!</p>
</h2>

## Descripción general
Meetro es un innovador servicio web diseñado para simplificar el proceso de encontrar un lugar de reunión central, especialmente para amigos o grupos dispersos en un área metropolitana. Nuestra solución no solo calcula la estación de metro óptima, sino que también recomienda atracciones cercanas, teniendo en cuenta la popularidad de los sitios para crear una experiencia de encuentro más agradable.

## Identificación y análisis del problema
Para amigos que viven en distintas ubicaciones, encontrar un punto de encuentro central puede ser un desafío. Las plataformas existentes como [WeMeetPlace](https://wemeetplace.com) y [Ya-manna](https://ya-manna.com) intentan encontrar puntos medios, pero a menudo carecen de atracciones actualizadas o deseables en esas áreas. Nuestra solución, Meetro, combina el cálculo del punto medio con datos actualizados de atracciones para ofrecer lugares de encuentro prácticos y atractivos.

### Oportunidades de investigación y mejora
1. **WeMeetPlace** ([Sitio web](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace se enfoca en ubicar puntos medios, pero carece de atracciones cercanas en muchas estaciones y a menudo utiliza datos desactualizados. Nuestro objetivo es garantizar que Meetro proporcione una experiencia basada en atracciones relevantes y actualizadas.

2. **Ya-manna** ([Sitio web](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna incluye opciones de entretenimiento, pero prioriza los puntos medios exactos, los cuales pueden carecer de destinos populares. Apuntamos a solucionar esto otorgando mayor peso a las atracciones populares, incluso si están ligeramente fuera del rango del punto medio.

Al abordar estas limitaciones, Meetro brinda una experiencia adaptada a usuarios que buscan más que un simple punto de encuentro, permitiéndoles acceder fácilmente a lugares de interés con datos de atracciones actualizados.

## Nombre y marca del proyecto
**Meetro** deriva de “Meet” y “Metro”, representando la idea de encontrarse en estaciones de metro. El nombre enfatiza nuestro enfoque en áreas metropolitanas, facilitando lugares de reunión convenientes y agradables en estaciones de metro.

## Declaración de misión
“Nuestra misión es ayudar a los amigos a encontrar la estación de metro más eficiente y lugares cercanos para disfrutar. Ya sea para reuniones informales o eventos especiales, simplificamos el proceso de elegir el lugar de encuentro perfecto.”

- **Objetivo**: Desarrollar un servicio web que localice el punto medio ideal en el metro y proporcione recomendaciones de atracciones populares cercanas.
- **Público objetivo**: Meetro está diseñado para amigos, familias o grupos que desean una forma conveniente, agradable y eficiente de planificar reuniones en ubicaciones centrales de metro.

## Características y funcionalidades
El sistema de puntuación único de Meetro combina cálculos de puntos medios con clasificaciones de atracciones, asegurando que los usuarios reciban recomendaciones de una estación de metro central que esté equipada con destinos populares para un encuentro memorable.

### Características clave
- **Cálculo del punto medio con rango flexible**: En lugar de un punto medio estricto, Meetro calcula un rango que permite a los usuarios priorizar estaciones con atracciones cercanas.
- **Ponderación de atracciones**: Meetro asigna ponderaciones a las atracciones. Los lugares comunes reciben una puntuación de 1, mientras que las atracciones populares (como parques de diversiones, centros comerciales) reciben una puntuación de 3, brindando preferencia a los sitios de alta demanda.
- **Puntuación de la estación**: Cada estación de metro cerca del punto medio recibe una puntuación basada en la proximidad y la ponderación de la atracción. Las estaciones más alejadas del punto medio tienen puntuaciones reducidas, mientras que las estaciones con atracciones populares reciben un impulso.
- **Recomendaciones optimizadas**: Meetro presenta a los usuarios la estación de metro con la puntuación más alta dentro del rango del punto medio, asegurando una combinación equilibrada de accesibilidad y disfrute.

### Diferenciación: ¿Qué hace único a Meetro?
| Característica                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **Cálculo del punto medio**           | Punto medio fijo                          | Punto medio con atracciones populares         |
| **Información sobre atracciones**         | Limitada o desactualizada                     | Atracciones de moda y actualizadas           |
| **Volumen de datos**                    | Pequeño                                   | Datos extensos que cubren más atracciones   |
| **Opciones del usuario**                   | Limitadas                                 | Flexibles, basadas en popularidad y ubicación |

Al aprovechar los datos actuales y proporcionar opciones basadas en la popularidad de las atracciones, Meetro mejora la experiencia de planificación de reuniones más allá de lo disponible actualmente.

## Herramientas y lenguajes de desarrollo
Meetro se desarrolla con una pila tecnológica robusta para asegurar rendimiento eficiente, escalabilidad y una interfaz fácil de usar.

- **Lenguajes y marcos**:
  - **JavaScript (Node.js)**: Maneja la lógica de backend e integraciones de API.
  - **Python**: Usado para procesamiento de datos, ponderación de atracciones e integración de mapas.
  - **HTML/CSS**: Define la estructura y diseño de la interfaz de usuario.
  - **JavaScript (React)**: Crea un frontend dinámico y responsivo.
- **Herramientas**:
  - **GitHub**: Control de versiones para rastrear el progreso y permitir la colaboración en equipo.
  - **OpenStreetMap (OSM)**: Proporciona datos de mapas de código abierto comprensivos.
  - **Google Maps API**: Soporta visualización de mapas, cálculo de puntos medios y recuperación de datos de atracciones.
  - **Figma**: Una herramienta colaborativa para diseño de UI/UX, asegurando consistencia en la experiencia del usuario.

## Responsabilidades del equipo
Para asegurar la ejecución fluida del proyecto, cada miembro del equipo tiene un rol claramente definido:

- **Líder del proyecto**: Soo-bin Yoon – Supervisa el desarrollo y la coordinación general del proyecto.
- **Administrador de código**: Ye-eun Yeom – Administra el repositorio y la integración del código.
- **Recolector de datos**: Yeon-jin Kim – Recolecta y procesa datos, asegurando la precisión de la información de atracciones.
- **Creador de la página web**: Yeo-jin Kim – Diseña y desarrolla la interfaz web para brindar una experiencia sin interrupciones al usuario.

## Inicio rápido
Para comenzar a usar Meetro, simplemente haz clic en el enlace a continuación para visitar el sitio web:

[Visitar Meetro](http://localhost:3000)

## Uso
1. **Ingresar ubicaciones**: Introduce las ubicaciones de cada persona en tu grupo.
2. **Encontrar punto medio**: La aplicación calcula un rango de punto medio y presenta estaciones de metro cercanas.
3. **Ver recomendaciones**: Las estaciones con las puntuaciones más altas en función de la proximidad y la popularidad de las atracciones son sugeridas como lugares de encuentro.
Meetro facilita la planificación del lugar de encuentro proporcionando funcionalidad amigable y recomendaciones relevantes.

## Contribuir
Agradecemos las contribuciones para mejorar Meetro. Para contribuir, sigue nuestras pautas en CONTRIBUTING.md. Las contribuciones pueden incluir mejoras en el código, nuevas funcionalidades o actualizaciones en los datos de atracciones.

## Licencia
Este proyecto está licenciado bajo la Licencia Apache 2.0. Consulta el archivo [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) para más detalles.

## Demos y ejemplos en línea
Además de las funcionalidades principales, proporcionamos las siguientes demos para mostrar las capacidades de Meetro:

1. Demo de cálculo de punto medio: Demuestra cómo Meetro calcula un punto medio dentro de un rango flexible y sugiere estaciones.
2. Ponderación de atracciones: Muestra cómo se priorizan las ubicaciones populares según las preferencias del usuario.
3. Recorrido de usuario: Sigue a un grupo de ejemplo navegando en la interfaz de Meetro, encontrando el lugar de reunión óptimo.
¡Explora Meetro hoy y descubre una forma más inteligente de encontrarse!
