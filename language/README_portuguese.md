<!---
Direitos autorais 2020 The HuggingFace Team. Todos os direitos reservados.

Este documento está licenciado sob a Licença Apache, Versão 2.0 (a "Licença"). Exceto conforme permitido pela Licença, você não pode usar este arquivo. Você pode obter uma cópia da Licença no link abaixo:

    http://www.apache.org/licenses/LICENSE-2.0

Salvo quando exigido pela lei aplicável ou acordado por escrito, o software distribuído sob a Licença é distribuído "TAL COMO ESTÁ", SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressas ou implícitas. Consulte a Licença para obter informações sobre permissões e limitações de uso.
-->

<h1 align="center">
    <p>Meetro🚇: Planejamento fácil de encontros em estações de metrô</p>
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
    <p>Clique na imagem abaixo para acessar a página da web.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Clique na imagem para acessar a página da web">
    </a>
</h3>

<h2 align="center">
    <p>A solução ideal para encontrar o ponto de encontro central!</p>
</h2>

## Visão geral
Meetro é um serviço web inovador, projetado para simplificar o processo de encontrar um local de encontro central, especialmente para amigos ou grupos espalhados por uma área metropolitana. Nossa solução não apenas calcula a estação de metrô mais conveniente, mas também recomenda atrações próximas, levando em conta a popularidade dos locais para criar uma experiência de encontro mais agradável.

## Identificação e Análise do Problema
Para amigos que vivem em locais diferentes, encontrar um ponto de encontro central pode ser um desafio. Plataformas existentes, como [WeMeetPlace](https://wemeetplace.com) e [Ya-manna](https://ya-manna.com), tentam encontrar pontos centrais, mas frequentemente carecem de atrações atualizadas ou interessantes. O Meetro combina o cálculo do ponto central com dados de atrações atuais para oferecer locais práticos e atrativos para encontros.

### Oportunidades de Pesquisa e Melhoria
1. **WeMeetPlace** ([Site](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace foca na localização de pontos centrais, mas falta de atrações próximas a muitas estações e, muitas vezes, utiliza dados desatualizados. Nosso objetivo é garantir que o Meetro proporcione uma experiência relevante baseada em atrações atualizadas.

2. **Ya-manna** ([Site](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Embora o Ya-manna inclua opções de entretenimento, ele prioriza pontos centrais exatos, que podem não ter destinos populares. Pretendemos resolver isso atribuindo uma prioridade maior a atrações populares, mesmo que estejam ligeiramente fora do ponto central.

Ao abordar essas limitações, o Meetro oferece uma experiência adaptada para usuários que buscam mais do que um simples ponto de encontro, permitindo acesso fácil a locais interessantes com dados atualizados de atrações.

## Nome e Marca do Projeto
**Meetro** é derivado de “Meet” e “Metro”, representando a ideia de encontros em estações de metrô. O nome enfatiza nosso foco em áreas metropolitanas e em encontrar locais de encontro convenientes e agradáveis.

## Declaração de Missão
"Nosso objetivo é ajudar amigos a encontrarem a estação de metrô mais conveniente e atrações próximas para aproveitar. Seja para encontros casuais ou ocasiões especiais, simplificamos o processo de escolher o ponto de encontro ideal."

- **Objetivo**: Desenvolver um serviço web que localize a estação de metrô ideal e forneça recomendações de atrações populares próximas.
- **Público-Alvo**: Meetro foi projetado para amigos, famílias ou grupos que desejam uma maneira conveniente, agradável e eficiente de planejar encontros em locais centrais de metrô.

## Funcionalidades e Características
O sistema único de pontuação do Meetro combina cálculos do ponto central com classificações de atrações, garantindo que os usuários recebam recomendações de uma estação central de metrô equipada com locais populares para um encontro memorável.

### Principais Características
- **Cálculo do ponto central com alcance flexível**: Em vez de um ponto central exato, o Meetro calcula uma área central que permite que os usuários priorizem estações com atrações próximas.
- **Ponderação de Atrações**: Meetro atribui pesos às atrações. Lugares comuns têm pontuação 1, enquanto atrações populares (como parques de diversões, shoppings) têm pontuação 3, dando preferência a locais de grande apelo.
- **Pontuação de Estações**: Cada estação de metrô próxima ao ponto central recebe uma pontuação com base na proximidade e na ponderação das atrações. Estações mais distantes do ponto central têm pontuações reduzidas, enquanto estações com atrações populares recebem um impulso.
- **Recomendações Otimizadas**: Meetro apresenta aos usuários a estação de metrô com a pontuação mais alta dentro do alcance central, garantindo uma mistura equilibrada de acessibilidade e diversão.

### Diferencial: Por que o Meetro se destaca
| Característica                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **Cálculo do ponto central**           | Ponto central fixo                          | Ponto central com atrações populares         |
| **Informações de atrações**         | Limitadas ou desatualizadas                   | Atrações atuais e populares                 |
| **Volume de dados**                    | Pequeno                                   | Dados extensivos cobrindo mais atrações     |
| **Escolhas dos usuários**                   | Limitadas                                 | Flexíveis, baseadas em popularidade e localização |

Usando dados atuais e fornecendo opções baseadas na popularidade das atrações, o Meetro melhora a experiência de planejamento de encontros além do que está atualmente disponível.

## Ferramentas e Linguagens de Desenvolvimento
O Meetro foi desenvolvido com uma pilha tecnológica robusta para garantir desempenho eficiente, escalabilidade e uma interface amigável.

- **Linguagens e Frameworks**:
  - **JavaScript (Node.js)**: Gerencia a lógica de backend e integrações de API.
  - **Python**: Usado para processamento de dados, ponderação de atrações e integração de mapas.
  - **HTML/CSS**: Define a estrutura e o design da interface do usuário.
  - **JavaScript (React)**: Cria um frontend dinâmico e responsivo.
- **Ferramentas**:
  - **GitHub**: Controle de versão para acompanhar o progresso e permitir a colaboração em equipe.
  - **OpenStreetMap (OSM)**: Fornece dados de mapas de código aberto abrangentes.
  - **Google Maps API**: Suporta visualização de mapas, cálculos do ponto central e recuperação de dados de atrações.
  - **Figma**: Ferramenta colaborativa para design de UI/UX, garantindo consistência na experiência do usuário.

## Responsabilidades da Equipe
Para garantir a execução tranquila do projeto, cada membro da equipe possui uma função claramente definida:

- **Líder do Projeto**: Soo-bin Yoon – Supervisiona o desenvolvimento e coordenação do projeto.
- **Gerente de Código**: Ye-eun Yeom – Gerencia o repositório e a integração de código.
- **Coletor de Dados**: Yeon-jin Kim – Coleta e processa dados, garantindo a precisão das informações de atrações.
- **Criador do Site**: Yeo-jin Kim – Desenha e desenvolve a interface do site para fornecer uma experiência de usuário tranquila.

## Começando
Para começar a usar o Meetro, clique no link abaixo para acessar o site:

[Visitar Meetro](http://localhost:3000)

## Como Usar
1. **Inserir Localizações**: Insira as localizações de cada pessoa no seu grupo.
2. **Encontrar o Ponto Central**: O aplicativo calcula uma área central e mostra as estações de metrô próximas.
3. **Ver Recomendações**: As estações com as maiores pontuações, com base na proximidade e popularidade das atrações, são sugeridas como locais de encontro.
O Meetro facilita a escolha de um ponto de encontro ao oferecer funcionalidades amigáveis e recomendações relevantes.

## Contribuição
Agradecemos contribuições para melhorar o Meetro. Para contribuir, siga nossas diretrizes em CONTRIBUTING.md. As contribuições podem incluir melhorias no código, novas funcionalidades ou atualizações nos dados de atrações.

## Licença
Este projeto está licenciado sob a Licença Apache 2.0. Consulte o arquivo [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) para mais detalhes.

## Demos e Exemplos Online
Além das funcionalidades principais, oferecemos as seguintes demonstrações para mostrar as capacidades do Meetro:

1. Demonstração de Cálculo do Ponto Central: Mostra como o Meetro calcula um ponto central dentro de um alcance flexível e sugere estações.
2. Ponderação de Atrações: Demonstra como locais populares são priorizados com base nas preferências dos usuários.
3. Jornada do Usuário: Acompanhe um grupo exemplo navegando pela interface do Meetro, encontrando o local ideal para o encontro.
Explore o Meetro hoje para experimentar uma maneira mais inteligente de se encontrar!
