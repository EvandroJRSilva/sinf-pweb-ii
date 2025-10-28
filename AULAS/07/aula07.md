# Aula 07

`Frameworks` são uma estrutura, ou conjunto de diretrizes, que fornecem uma fundação básica para a construção de alguma coisa. No contexto de desenvolvimento de software, um `framework` é uma **coleção de códigos e ferramentas** que disponibilizam uma forma padronizada de desenvolver aplicações, permitindo aos desenvolvedores se focarem nas partes principais do sistema. Isso é possível porque o `framework` vai lidar com as partes mais genéricas e repetitivas do código.

## Lista de `frameworks`

A seguir, duas listas de `frameworks` populares.

- **Front-end**
  - [**React**](https://react.dev/)
    - Uma biblioteca JavaScript para criar interfaces de usuário, ou seja, não é um `framework` propriamente dito.
    - Seu objetivo principal é minimizar bugs que ocorrem quando desenvolvedores estão construindo interfaces de usuário (**UI** - *User Interface*). Isso é possível com o uso de componentes (pedaços de código lógicos e autocontidos que descrevem uma porção da interface de usuário).
  - [**Vue.js**](https://vuejs.org/)
    - `Framework` JavaScript moderno que fornece recursos úteis para aprimoramento progressivo. Ao contrário de muitos outros `frameworks`, o Vue pode ser usado para aprimorar o HTML da página.
  - [**Svelte**](https://svelte.dev/)
    - `Framework` UI que usa um compilador que permite o desenvolvimento de componentes concisos, "de tirar o fôlego", e que utilizam o navegador minimamente.
  - [**Angular**](https://angular.dev/)
    - É um `framework` e uma plataforma de desenvolvimento feito em `TypeScript`. É usado para a criação de aplicações web de página única. Como plataforma, o Angular inclui:
      - Um `framework` baseado em componente para a construção de aplicações web escaláveis.
      - Uma coleção de bibliotecas bem integradas que cobrem uma variadade de recursos, incluindo roteamento, gerenciamento de formulário, comunicação cliente-servidor, etc.
      - Um conjunto de ferramentas de desenvolvedor que facilitam o desenvolvimento, construção, teste e atualização do código.
- **Back-end** [^1]
  - [Django (Python)](https://www.djangoproject.com/)
    - Framework web poderoso que ajuda os desenvolvedores a construir, rapidamente, sites seguros e sustentáveis. Ele segue o princípio **DRY** (*don't repeat yourself*, não repita a si mesmo) e vem com vários recursos nativos.
    - É mais adequado para
      - Redes sociais;
      - Sistemas de gerenciamento de conteúdo (**CMS** - *Content Management Systems*), como portais de notícias ou blogs;
      - Plataformas educacionais;
      - Dashboards de empresas internacionais e painéis de administração.
    - É ideal para projetos onde:
      - Haja necessidade de se desenvolver algo rapidamente com segurança nativa;
      - Seja necessário um sistema confiável e escalável;
      - O desenvolvimento será feito com Python.
  - [Ruby on Rails (Ruby)](https://rubyonrails.org/)
    - Seu foco está sobre a satisfação do desenvolvedor e desenvolvimento rápido. É perfeito para Startups e projetos onde o tempo necessário para lançamento é importante.
    - É mais adequado para
      - Produtos viáveis mínimos (**MVPs** - *Minimum Viable Products*) e ideias de startaups;
      - Marketplaces;
      - Ferramentas de colaboração de times;
      - Plataformas de aprendizado online (*e-learning*).
    - É ideal para projetos onde:
      - Haja necessidade de um desenvolvimento rápido;
      - Haja preferência por convenção em detrimento de configuração;
      - Ferramentas consolidadas de teste e suporte de comunidade são valorizados.
  - [Laravel (PHP)](https://laravel.com/)
    - Framework PHP moderno conhecido pela sintaxe limpa e ecossistema rico. Simplifica muitas tarefas simples como roteamento, sessões e autenticação.
    - É mais adequado para
      - Sistemas CRM personalizados;
      - Aplicativos de reserva (hotéis, eventos);
      - Sites de *e-commerce* com contas de usuários e carrinhos de compra;
      - Plataformas de blog ou soluções CMS personalizadas.
    - É ideal para projetos onde:
      - Haja necessidade de desenvolvimento rápido com código de fácil leitura;
      - Haja preferência de se trabalhar com PH pacotes da comunidade;
      - Haja necessidade de uma interface de usuário bonita em conjunto com lógica de *back-end* (via Laravel Blade).
  - [Express.js (Node.js)](https://expressjs.com/)
    - É um dos frameworks mais populares para o Node.js. É minimalista, imparcial e dá aos desenvolvedores controle total sobre a estrutura de seus aplicativos.
    - É mais adequado para:
      - APIs RESTful e microserviços;
      - Aplicações de página única (**SPAs** - *Singe Page Applications*) como o Trello ou Slack (em conjunto com React ou Vue);
      - Aplicativos de chat em tempo real usando WebSockets;
      - Plataformas de *e-commerce* ou sistemas de reserva.
    - É ideal para projetos onde:
      - Haja necessidade de completa flexibilidade sem muitas restrições;
      - O JavaScript esteja sendo usando tanto no front quanto no back-end;
      - Velocidade, desempenho e modularidade são importantes.
  - [Spring/Spring Boot (Java)](https://spring.io/projects/spring-boot)
    - Simplifica o desenvolvimento com Java *enterprise* e fornece uma configuração poderosa e pronta para produção já pronta para uso. É parte de um ecosistema Spring.
    - É mais adequado para:
      - Sistemas bancários e aplicativos *fintechs*;
      - Plataforas SaaS de nível empresarial;
      - Sistemas ERP grandes para negócios;
      - Arquiteturas baseadas em microsserviços com lógica de negócio complexa.
    - É ideal para projetos onde:
      - Escalabilidade e confiabilidade são conceitos chave;
      - O desenvolvimento será feito em um ambiente corporativo;
      - Haja necessidade de alto desempenho sem que isso afete a segurança.
  - [ASP.Net (C#)](https://dotnet.microsoft.com/en-us/apps/aspnet)
    - É um framework multi-plataforma da Microsoft para o desenvolvimento de aplicativos web modernos. É estável, rápido e usado para aplicações de nível empresarial no mundo inteiro.
    - É mais adequado para:
      - Portais de Governos e Empresas;
      - Ferramentas de relatórios ou dashboards;
      - Aplicativos baseados em nuvem (especialmente com Azure);
      - Ferramentas corporativas internas com autenticação de usuários e papéis.
    - É ideal para projetos onde:
      - Haja necessidade de e estrutura de tipo forte;
      - O desenvolvimento ocorrerá com Windows ou programas da Microsoft;
      - Haja necessidade de sistemas sustentáveis de larga escala.
  - [Flask (Python)](https://flask.palletsprojects.com/en/stable/)
    - É um micro-framework que dá aos desenvolvedores controle completo sobre como desenvolverão seus aplicativos. É leve, fácil de apresender e flexível.
    - É mais adequado para:
      - APIs para aplicataivos móveis;
      - Aplicações web pequenas, ou projetos pessoais;
      - Disponibilização de modelo de Aprendizado de Máquina (AM);
      - Aplicativos de "prova de conceito", ou protótipos.
    - É ideal para projetos onde:
      - Haja necessidade de alguma ferramenta mínima e fácil de desenvolver;
      - Haja necessodade de completa flexibilidade, sem restrições;
      - Modelos de IA/AM serão disponibilizadas via API.
  - [FastAPI (Python)](https://fastapi.tiangolo.com/)
    - É um dos frameworks em Python mais rápidos entre os disponíveis e é feito para criar APIs RESTful eficientemente. Usa recursos modernos do Python e tem suporte para documentação automática OpenAPI.
    - É mais adequado para:
      - Aplicações baseadas em IA ou AM;
      - APIs de alto desempenho;
      - Plataformas de IoT e baseadas em dados;
      - APIs de Fintech e de saúde que necessitam de velocidade e validação de dados.
    - É ideia para projetos onde:
      - Haja necessidade de velocidade e desempenho;
      - Checagem de tipo e validação são importantes;
      - Serão desenvolvidos serviços com muitos dados ou baseados em IA.
  - [Phoenix (Elixir)](https://phoenixframework.org/)
    - É um framework web feito com Elixir e é conhecido por sua comunicação em tempo real e tolerância a falhas. É baseado na Máquina Virtual Erlang, usada em sistemas de telecomunicação.
    - É mais adequada para:
      - Aplicativos em tempo real, como plataforma de chats ou jogos multiplayer;
      - Plataformas de negócios com atualizações ao vivo;
      - Aplicações IoT que demandem alta concorrência;
      - Dashboards ao vivo e ferramentas colaborativas.
    - É ideal para projetos onde:
      - Haja necessidade de alta concorrência e baixa latência;
      - Será desenvolvido algo que funcione em tempo real e interativo;
      - Confiabilidade e tolerância a falhas são críticos.


[^1]: Fonte principal: [Top 10 Backend Frameworks to Learn in 2025 (With Project Examples)](https://mahabub-r.medium.com/top-10-backend-frameworks-to-learn-in-2025-with-project-examples-9a68cacedf3d).

Alguns links:

- https://roadmap.sh/frontend/frameworks
- https://roadmap.sh/backend/frameworks
- https://mahabub-r.medium.com/top-10-backend-frameworks-to-learn-in-2025-with-project-examples-9a68cacedf3d
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks