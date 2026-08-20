# Aula 03

## [RFC 9110: STD 97: HTTP Semantics](https://www.rfc-editor.org/info/rfc9110)

### 1. [Introduction](https://www.rfc-editor.org/info/rfc9110/#section-1)

#### 1.1 Propósito

O HTTP é uma família de protocolos *stateless*, *application-level* e *request/response* que compartilham uma **interface genérica**, **semântica extensível** ([Seção 16: Extending HTTP](https://www.rfc-editor.org/info/rfc9110/#section-16)) e **mensagens auto-descritivas** para permitir a interação flexível com sistemas de informação de hipertexto baseado em rede.
  
- **Interface genérica:** uma interface uniforme para clientes que esconde os detalhes de como um serviço é implementado, e independe dos tipos de recursos fornecidos.
  - Por causa disso, o protocolo **não pode ser definido** em termos de o que acontece por detrás da interface.
- ***Stateless*:** servidores não precisam estar cientes da finalidade de cada cliente. Uma requisição (*request*) pode ser considerada de forma isolada.

O HTTP também foi projetado para ser usado como um protocolo de **intermediação**, no qual *proxies* e *gateways* podem traduzir sistemas de informação não HTTP em uma interface mais genérica (provavelmente [seção 7.3](https://www.rfc-editor.org/info/rfc9110/#section-7.3)).

### 3. [Terminology and Core Concepts](https://www.rfc-editor.org/info/rfc9110/#section-3)

#### 3.1. Recursos

- Um recurso é o alvo/objetivo de uma requisição HTTP.
- A natureza do recurso não é limitada. O HTTP define meramente uma interface que pode ser usada para interagir com os recursos.
- A maioria dos recursos é identificado por um URI (*Unified Resource Identifier*).
- Objetivo de design: **separar** a **identificação** do recurso da **semântica de requisição**
  - **Identificação:** URI.
  - **Semântica de requisição:** método e campos de cabeçalho.

#### 3.2 Representações

- Uma representação é uma informação que visa refletir um **estado** passado, atual ou desejado de um determinado `recurso`, em um formato que possa ser facilmente comunicado por meio do protocolo.
- Uma representação consiste em um **conjunto de metadados de representação** e um **fluxo potencialmente ilimitado de dados de representação**.
- Maiores detalhes: [Seção 8 - *Representation Data and Metadata*](https://www.rfc-editor.org/info/rfc9110/#representation.data.and.metadata).

O HTTP permite o "ocultamento de informações" por trás de sua interface uniforme, **definindo a comunicação** em relação a uma **representação transferível do estado do recurso**, em vez de transferir o próprio recurso. Exemplo dado:

- O recurso é uma função temporal "clima atual de cidade X". O resultado dessa função seria sua representação, o que é de fato transmitido.
- Ou seja, o recurso desejado pode ser fornecido atraveś de (ou ser capaz de gerar) múltiplas representações, cada uma com o intuito de refletir o estado atual do recurso.
  - A escolha de qual representação será transmitida é feita por um algoritmo específico ([seção 12](https://www.rfc-editor.org/info/rfc9110/#content.negotiation)). A representação escolhida fornece dados e metadados para a [avaliação de requisições condicionais](https://www.rfc-editor.org/info/rfc9110/#conditional.requests) e a construção do conteúdo da resposta HTTP para o método `GET` com os códigos de status 200 (OK), 206 (Partial Content), 304 (Not Modified).

#### 3.3 Conexões, Clientes e Servidores

- Um cliente HTTP é um **programa** que **estabelece uma conexão com um servidor** com o propósito de enviar uma ou mais **requisições HTTP**.
- Um servidor HTTP é um **programa** que **aceita conexões** para **responder requisições HTTP** ao enviar **respostas HTTP**.
  - Um servidor **NÃO PODE** presumir que duas requisições na mesma conexão são do mesmo agente de usuário, exceto se for uma conexão segura e específica para um determinado agente.
- Os termos cliente e servidor se referem aos papéis dos programas em uma conexão em particular.
  - Ou seja, um mesmo programa pode ser um cliente em uma conexão, e servidor em outra conexão.

#### 3.4 Mensagens

O HTTP troca mensagens através de uma conexão:

- *sender* (remetente): uma implementação que envia mensagens.
- *recipient* (recipiente/recebedor): uma implementação que recebe mensagens.

Um cliente envia requisições a um servidor na forma de uma mensagem de requisição contendo: 

- Um método;
- Um recurso desejado;
- E opcionalmente: 
  - Campos de cabeçalho para modificar a requisição;
  - Informações do cliente;
  - Metadados de representação; 
  - Conteúdo destinado ao processamento de acordo com o método;
  - Cabeçalhos de "rodapé" (*trailer fields*) - [seção 6.5](https://www.rfc-editor.org/info/rfc9110/#trailer.fields).

Um servidor responde à requisição do cliente enviando uma ou mais mensagens de resposta contendo:

- Código de status;
- E opcionalmente:
  - Campos de cabeçalho, para informações do servidor;
  - Metadados do recurso;
  - Metadados de representação;
  - Conteúdo a ser interpretado de acordo com o código de status;
  - Cabeçalhos de "rodapé" (*trailer fields*).

#### 3.5 Agentes de usuário

Um agente de usuário consiste em um **programa que inicia uma requisição**:

- Navegador web (mais comum);
- *Spiders* (ou *web crawlers*);
- Ferramentas de linha de comando;
- Painéis de outdoors;
- Eletrodomésticos;
- Balanças;
- Lâmpadas;
- Scripts de atualização de *firmware*;
- Aplicativos móveis;
- Dispositivos de comunicação;
- etc.

#### 3.6 Servidor de origem

Um servidor de origem consiste em um **programa que pode originar respostas autoritativas** para um dado recurso desejado:

- Sites (mais comum);
- Unidades de automação residencial;
- Componentes configuráveis de rede;
- Máquinas de escritório;
- Robôs autônomos;
- Feeds de notícia;
- Câmeras de tráfego;
- Seletores de anúncio em tempo real;
- Plataformas de vídeo sob demanda;
- etc.

#### 3.7 Intermediários

O HTTP permite o uso de intermediários para atender solicitações por meio de uma cadeia de conexões:

- Tipos: proxy, gateway e túnel.
- Um único intermediário pode agir como servidor de origem, proxy, gateway ou túnel ao mudar seu comportamento baseado na natureza de cada requisição.

```
         >             >             >             >
    UA =========== A =========== B =========== C =========== O
               <             <             <             <
```

- Legenda:
  - UA: agente de usuário (*user agent*).
  - O: servidor de origem.
  - A, B e C: intermediários.
- Uma mensagem que passa por toda essa cadeia vai passar por quatro **conexões separadas**.
- Opções de comunicação do HTTP podem ser aplicados:
  - Apenas para a conexão com o vizinho não-túnel mais próximo;
  - Apenas para os dispositivos periféricos (*endpoints*) da cadeia;
  - Ou para todas conexões ao longo da cadeia.
- As comunicações não são necessariamente lineares, ou seja: 
  - Cada participante do diagrama acima pode estar engajado em conexões múltiplas e simultâneas.
  - E também, requisições posteriores podem ser enviadas por um caminho de conexões diferente, geralmente com base em uma configuração dinâmica para balanceamento de carga.
- Termos importantes:
  - *upstream* e *downstream*: são usados para descrever requisições direcionais em relação ao fluxo da mensagem.
    - Fluxo é sempre: *upstream* -> *downstream*
  - *inbound* e *outbound*: são usados para descrever requisições direcionais em relação à rota da requisição.
    - *inbound*: para (*towards*) o servidor de origem.
    - *outbound*: para (*towards*) o agente de usuário.

Um ***proxy*** é agente de encaminhamento de mensagens (*message-forwarding*) escolhido pelo cliente, normalmente através de **regras de configurações locais**, para receber requisições de algum(ns) tipo(s) de URI absoluto e tentar satisfazer essas requisições por meio de tradução através da interface HTTP.
    - São frequentemente usados para agrupar requisições HTTP de uma organização através de um intermediário comum para fins de serviços de segurança, serviços de anotação ou cache compartilhado.

Um ***gateway*** (também conhecido como proxy reverso) é um intermediário que atua como um servidor de origem para conexão *outbound*, mas traduz requisições recebidas e as encaminha (*inbound*) para outro(s) servidor(es).
    - São frequentemente usados para encapsular serviços de informação legados ou não confiáveis, para melhorar o desempenho do servidor através do cache "acelerador" e para permitir o particionamento ou balanceamento de carga de serviços HTTP em várias máquinas.
    - Todas as exigências do HTTP a um servidor de origem também são aplicadas à comunicação *outbound* de um gateway.

Um ***tunnel*** (túnel) funciona como um relé cego entre duas conexões, sem alterar as mensagens. Uma vez ativo, um túnel não considerado um participante (ou uma parte) para a comunicação HTTP, mesmo que o túnel tenha sido inicializado por uma requisição HTTP. Ele deixa de existir quando ambas as pontas da "conexão com relé" são fechadas.

Os túneis são usados para estender uma conexão virtual através de um intermediário, como quando o TLS (*Transport Layer Security*) é usado para estabelecer comunicação confidencial através de um proxy firewall compartilhado.

#### 3.8 Caches

Um **cache** é um armazenamento local de mensagens de resposta anteriores e o subsistema que controla o armazenamento, recuperação e exclusão dessas mensagens. Um cache armazena respostas "cacheáveis" para reduzir o tempo de resposta e o consumo de largura de banda em requisições futuras equivalentes.
    - Qualquer cliente ou servidor pode utilizar um cache, apesar dele não poder ser usado enquanto estiver funcionando como um túnel.

O efeito do cache consiste no encurtamento da cadeia de requisição/resposta se um dos participantes ao longo da cadeia tenha uma resposta cacheada aplicável àquela requisição. Exemplo:

```
            >             >
       UA =========== A =========== B - - - - - - C - - - - - - O
                  <             <
```

Uma resposta é cacheável se é permitido ao cache armazenar uma cópia da mensagem de resposta para responder requisições subsequentes.

### 9. [Methods](https://www.rfc-editor.org/info/rfc9110/#section-9)

O token de método de requisição é a fonte primária da semântica de requisição. Ele indica:
    - O propósito pelo qual o cliente fez essa requisição, e
    - O que é esperado pelo cliente como um resultado bem sucedido.

```
method = token
```

O token é *case-sensitive* 
    - Porque pode ser usado como porta de entrada para sistemas orientados a objetos com nomes de métodos que também são *case-sensitive*.
    - Por convenção, **os métodos padronizados são definidos em letras maiúsculas** do padrão ASCII americano.

| **Método** | **Descrição** |
| --- | --- |
| GET | Transfere a representação atual do recurso desejado |
| HEAD | O mesmo que GET, mas não transfere o conteúdo de resposta |
| POST | Executa processamento específico ao recurso no conteúdo da requisição |
| PUT | Substitui todas representações atuais de um recurso desejado pelo conteúdo da requisição |
| DELETE | Exclui todas as representações atuais do recurso desejado (indicado) |
| CONNECT | Estabelece um túnel para o servidor identificado pelo recurso indicado |
| OPTIONS | Descrece as opções de comunicação para o recurso indicado |
| TRACE | Executa um teste *loop-back* de mensagens ao longo do caminho até o recurso indicado |


Algumas regras:
- Todos os servidores de propósito geral DEVEM OBRIGATORIAMENTE ter suporte aos métodos GET e HEAD. Os demais métodos são opcionais.
- O conjunto de métodos permitidos por um recurso desejado/indicado pode ser listado um campo de cabeçalho *Allow*. Entretanto, o conjunto de métodos permitidos pode ser modificado dinamicamente.
- Um servidor de origem que recebe um método de requisição não reconhecido ou não implementado DEVE responder com o código de status 501 (Not Implemented).
- Um servidor de origem que recebe um método que é reconhecido e implementado, mas não permitido pelo recurso indicado, DEVE responder com o código de status 405 (Method Not Allowed).

Métodos adicionas foram especificados para o uso no HTTP. Todos esses métodos devem ser registrados dentro do HTTP Method Registry ([Seção 16.1](https://www.rfc-editor.org/info/rfc9110/#method.extensibility)).

#### 9.2 Propriedades Comuns dos Métodos

### [Status Codes](https://www.rfc-editor.org/info/rfc9110/#section-15)