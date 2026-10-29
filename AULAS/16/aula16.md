# Aula 16: Design de APIs --- boas práticas

**Sumário**

- [Aula 16: Design de APIs --- boas práticas](#aula-16-design-de-apis-----boas-práticas)
  - [1 - Introdução](#1---introdução)
    - [1.1 - API First](#11---api-first)
    - [1.2 - Consistência (*common look and feel*)](#12---consistência-common-look-and-feel)
      - [1.2.1 - Recursos bem modelados](#121---recursos-bem-modelados)
      - [1.2.2 - Métodos HTTP e códigos de status](#122---métodos-http-e-códigos-de-status)
    - [1.3 - Não quebrar a compatibilidade retroativa](#13---não-quebrar-a-compatibilidade-retroativa)
      - [1.3.1 - Preferência por extensões compatíveis](#131---preferência-por-extensões-compatíveis)
      - [1.3.2 - Versionamento (apenas quando necessário)](#132---versionamento-apenas-quando-necessário)
      - [1.3.3 - Depreciação](#133---depreciação)
    - [1.4 - *API as a Product*](#14---api-as-a-product)
      - [1.4.1 - Paginação, filtros e ordenação](#141---paginação-filtros-e-ordenação)
      - [1.4.2 - Robustez operacional](#142---robustez-operacional)
  - [2 - *Designing Web APIs Building APIs that Developers Love*](#2---designing-web-apis-building-apis-that-developers-love)
    - [2.1 - *Make it fast and easy to get started*](#21---make-it-fast-and-easy-to-get-started)
    - [2.2 - *Work toward consistency*](#22---work-toward-consistency)
    - [2.3 - *Make troubleshooting easy*](#23---make-troubleshooting-easy)
      - [2.3.1 - *Meaningful errors*](#231---meaningful-errors)
    - [2.4 - *Make your API Extensible*](#24---make-your-api-extensible)
  - [Exercícios para discussão](#exercícios-para-discussão)


## 1 - Introdução

As diretrizes modernas ([Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/), [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines), [Google API Design Guide](https://cloud.google.com/apis/design) / [AIPs](https://google.aip.dev/), e práticas de empresas como Stripe[[1](https://stripe.com/docs/api/versioning)][[2](https://stripe.com/docs/api)] e GitHub[[3](https://docs.github.com/en/rest/overview/api-versions)][[4](https://docs.github.com/en/rest)]) convergem em quatro princípios que orientam o design de APIs:

1. **API First**
2. **Consistência (*common look and feel*)**
3. **Não quebrar a compatibilidade retroativa**
4. ***API as a Product***

### 1.1 - API First

**A especificação precede o código**. A especificação (OpenAPI) é definida antes da implementação e constitui o contrato e a fonte da verdade, isso permite revisão precoce, desenvolvimento paralelo (frontend/backend) e evita drift entre implementação e documentação.

- Escreva o OpenAPI (3.1+) como artefato primário.
- A spec deve conter: endpoints, parâmetros, schemas de request/response, exemplos, códigos de status e schemas de erro.
- Gere stubs, clients, mocks e documentação a partir da spec.
- Valide o contrato em CI para garantir que a implementação não diverge da especificação.
- Inclua sempre os casos de erro (preferencialmente no formato RFC 9457 — Problem Details).

**Prática recomendada:** *design-first* com revisão por pares antes de iniciar a implementação.

**Exemplo** (ruim):

```yaml
# openapi.yaml (incompleto, sem erros, sem exemplos)
paths:
  /books:
    get:
      responses:
        '200':
          description: OK
```

**Exemplo** (bom - contrato completo e explícito desde o início):

```yaml
openapi: 3.1.0
info:
  title: Books API
  version: 1.0.0
paths:
  /books:
    get:
      summary: List books
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BookList'
              examples:
                default:
                  value:
                    data: []
                    pagination:
                      has_more: false
        '400':
          description: Invalid query parameters
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/Problem'
components:
  schemas:
    Problem:
      type: object
      required: [type, title, status]
      properties:
        type:
          type: string
          format: uri
        title:
          type: string
        status:
          type: integer
        detail:
          type: string
        instance:
          type: string
```

### 1.2 - Consistência (*common look and feel*)

As APIs devem ter aparência e comportamento uniformes, como se tivessem sido projetadas pelo mesmo time. A previsibilidade reduz a carga cognitiva e facilita a adoção. Consumidores devem conseguir adivinhar o comportamento da API.

#### 1.2.1 - Recursos bem modelados

- Modele em torno de recursos de domínio (substantivos), não de operações.
- Coleções no plural: `/users`, `/orders`, `/books`.
- Identificadores: `/users/{id}`.
- Aninhamento limitado (máximo 2–3 níveis).
- URLs livres de verbos — o método HTTP carrega a semântica.
- Convenções de nomenclatura consistentes (kebab-case em paths; snake_case ou camelCase em propriedades e query parameters — escolha uma e mantenha em toda a API).

**Exemplo**

```
# Ruim — estilo RPC, verbos na URL, nomenclatura inconsistente
POST /createBook
GET  /getBookById?id=123
GET  /books/123/getLoans
POST /updateBook

# Bom — recursos, plural, métodos HTTP corretos, aninhamento limitado
POST   /books
GET    /books
GET    /books/{book_id}
PATCH  /books/{book_id}
DELETE /books/{book_id}
GET    /books/{book_id}/loans
```

#### 1.2.2 - Métodos HTTP e códigos de status

Use a semântica padrão (RFC 9110):

| **Método** | **Uso principal** | **Seguro** | **Idempotente** |
|---|---|---|---|
| `GET` | Leitura | Sim | Sim |
| `POST` | Criação / ações | Não | Não |
| `PUT` | Substituição completa | Não | Sim |
| `PATCH` | Atualização parcial | Não | Não |
| `DELETE` | Remoção | Não | Sim |

Retorne códigos de status corretos (201 + `Location` na criação; 204 quando não há corpo; nunca 200 com erro no body). Padronize erros com RFC 9457 (`application/problem+json`).

**Exemplos**

Ruim — erro ad hoc, status 200 com falha no body

```json
HTTP/1.1 200 OK
{
  "success": false,
  "error": "ISBN inválido",
  "code": 1001
}
```

Bom — RFC 9457 + status HTTP correto

```json
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json

{
  "type": "https://api.exemplo.com/problems/validation-error",
  "title": "Validation failed",
  "status": 422,
  "detail": "The field 'isbn' must be a valid ISBN-13.",
  "instance": "/books"
}
```

### 1.3 - Não quebrar a compatibilidade retroativa

APIs são contratos. Consumidores têm ciclos de vida independentes. Mudanças devem preservar os consumidores existentes. Prefira extensões compatíveis; use versionamento apenas quando for inevitável.

#### 1.3.1 - Preferência por extensões compatíveis

- Adicione campos opcionais, novos endpoints ou novos valores de enumeração aberta. 
- Nunca altere a semântica de campos existentes, remova campos ou torne opcionais em obrigatórios sem versionamento. 
- Clientes devem ignorar campos desconhecidos (extensibilidade).

#### 1.3.2 - Versionamento (apenas quando necessário)

Quando uma mudança incompatível for inevitável:

| **Estratégia** | **Exemplo** | **Observação** |
|---|---|---|
| URI path | `/v1/users` | Mais comum e visível |
| Header | `X-API-Version: 2025-06-15` | URLs limpas |
| Media type | `Accept: application/vnd.myapi.v2+json` | Preferido por Zalando |
| Date-based | Header ou transformação por data | Estilo Stripe |

Escolha uma estratégia e aplique-a consistentemente. Zalando recomenda **evitar versionamento** sempre que possível e, quando necessário, preferir media type.

**Exemplo**

Ruim — mudança incompatível silenciosa

```json
// Antes
{ "id": "123", "title": "DDD", "author": "Eric Evans" }

// Depois (quebra clientes que esperam "author")
{ "id": "123", "title": "DDD", "authors": ["Eric Evans"] }
```

Bom — extensão compatível (campo novo opcional)

```json
// Antes
{ "id": "123", "title": "DDD", "author": "Eric Evans" }

// Depois (clientes antigos continuam funcionando)
{
  "id": "123",
  "title": "DDD",
  "author": "Eric Evans",
  "published_year": 2003
}
``` 

#### 1.3.3 - Depreciação

- Suporte mínimo de 6–12 meses.
- Use headers `Deprecation` e `Sunset`.
- Forneça guia de migração e monitore o uso antes do desligamento.

**Exemplo**

Ruim — depreciação sem aviso

```
# Endpoint antigo simplesmente some ou retorna 410 sem comunicação prévia
GET /v1/books  → 410 Gone
```

Bom — depreciação comunicada

```
HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 01 Oct 2026 00:00:00 GMT
Link: <https://api.exemplo.com/docs/migration-v2>; rel="deprecation"
```

### 1.4 - *API as a Product*

Tratar a API como um produto. Priorizar simplicidade, compreensibilidade, usabilidade para os engenheiros clientes e robustez operacional. A API deve ser simples, compreensível e robusta para seus consumidores.

#### 1.4.1 - Paginação, filtros e ordenação

Toda coleção potencialmente grande **deve** ser paginada desde o primeiro dia (adicionar depois é *breaking change*).

- **Offset** / **page-based**: simples, permite “ir para página X”, ruim em datasets grandes ou mutáveis.
- **Cursor-based** (recomendado para feeds e dados dinâmicos): performance constante e estável. Cursor deve ser opaco.
- Ordenação: `?sort=created_at` ou `?sort=-created_at` (múltiplos campos separados por vírgula). Defina ordenação padrão estável.
- Filtros: query parameters simples ou estilo `filter[...]`. Documente campos e operadores.
- Inclua links de navegação (`self`, `next`, `prev`) na resposta.

**Exemplo**

Ruim — coleção sem paginação (ou só offset em dataset grande)

```
GET /books          # pode retornar milhares de itens
GET /books?page=500 # OFFSET 10000 → lento e instável
```

Bom — cursor-based com links

```
GET /books?sort=-published_year&filter[genre]=fiction&cursor=eyJpZCI6IjEyMyJ9&limit=20
```

```json
{
  "data": [
    { "id": "456", "title": "Clean Architecture", "published_year": 2017 }
  ],
  "pagination": {
    "next_cursor": "eyJpZCI6IjQ1NiJ9",
    "has_more": true
  },
  "links": {
    "self": "https://api.exemplo.com/books?cursor=eyJpZCI6IjEyMyJ9&limit=20",
    "next": "https://api.exemplo.com/books?cursor=eyJpZCI6IjQ1NiJ9&limit=20"
  }
}
```

#### 1.4.2 - Robustez operacional

- **Idempotência:** use header `Idempotency-Key` em POSTs críticos.
- **Rate limiting:** retorne 429 + `Retry-After`.
- **Segurança básica:** HTTPS, autenticação adequada, não exponha stack traces.
- Documentação clara, exemplos reais e guias de uso (a documentação faz parte do produto).

**Exemplo**

Ruim — POST sem proteção contra retentativas

```
POST /books
Content-Type: application/json

{ "title": "DDD", "isbn": "978-0321125217" }
# Retentativa pode criar duplicatas
```

Bom — Idempotency-Key

```
POST /books
Idempotency-Key: 7f3e9c2a-1b4d-4e8f-9a0c-5d6e7f8a9b0c
Content-Type: application/json

{
  "title": "Domain-Driven Design",
  "author": "Eric Evans",
  "isbn": "978-0321125217"
}
```

## 2 - *Designing Web APIs Building APIs that Developers Love*

Livro de Brenda Jin, Saurabh Sahni & Amir Shevat, de 2018. O quanto dessas práticas se mantiveram atuais/relevantes?

### 2.1 - *Make it fast and easy to get started*

**É importante que os desenvolvedores consigam entender sua API e começar a usá-la rapidamente**. Eles podem estar usando sua API para evitar ter que desenvolver um conjunto de produtos secundários para dar suporte ao produto principal. Não os faça se arrepender dessa decisão com uma API opaca e difícil de usar.

**A documentação pode ser de grande ajuda** para os desenvolvedores começarem a usar a API. Além de documentos que descrevem as especificações de uma API, **tutoriais ou guias de primeiros passos podem ser muito úteis**. Um tutorial é uma interface interativa para ensinar os desenvolvedores sobre a sua API. Nele, os desenvolvedores podem responder a perguntas ou inserir código em uma área de entrada. Um guia, por sua vez, é um documento mais contextual do que uma especificação. Ele fornece informações para os desenvolvedores em um determinado momento — geralmente no início, mas também durante atualizações ou conversões de uma versão ou recurso para outro.

Em alguns casos, você pode **complementar a facilidade de uso fornecendo documentação interativa online, onde os desenvolvedores têm um ambiente de teste para experimentar sua API**. Muitas vezes, os desenvolvedores podem usar essas interfaces para testar o código e visualizar os resultados sem precisar implementar autenticação.

Além da documentação interativa, **ferramentas como kits de desenvolvimento de software (SDKs) podem ser de grande ajuda para os desenvolvedores utilizarem sua API**. Esses pacotes de código são projetados para auxiliar os desenvolvedores a iniciarem seus projetos rapidamente, simplificando algumas das camadas transacionais e a configuração de um aplicativo.

Para uma experiência ideal, **os desenvolvedores devem poder testar suas APIs sem precisar fazer login ou se cadastrar**. Se isso for inevitável, você deve fornecer um fluxo de cadastro ou criação de aplicativo simples que colete as informações mínimas necessárias. Se sua API for protegida por OAuth, você deve oferecer aos desenvolvedores uma maneira de gerar tokens de acesso na interface do usuário. Implementar o OAuth é trabalhoso para os desenvolvedores e, na ausência de maneiras fáceis de gerar esses tokens, você verá uma taxa de abandono significativa nesse ponto.

### 2.2 - *Work toward consistency*

Você quer que sua API seja **intuitivamente consistente**. Isso deve se refletir nos **nomes dos seus endpoints, parâmetros de entrada e respostas de saída**. **Os desenvolvedores devem ser capazes de deduzir partes da sua API mesmo sem ler a documentação**. A menos que você esteja fazendo uma atualização de versão significativa ou um grande lançamento, é melhor trabalhar em prol da consistência ao projetar novos aspectos de uma API existente.

Por exemplo, você pode ter nomeado anteriormente um grupo de recursos como "usuários" e nomeado seus endpoints de API de acordo, mas agora percebe que faz mais sentido chamá-los de "membros". Pode ser muito tentador trabalhar em prol da "correção" do novo modelo em vez de se concentrar na consistência com o antigo. Mas se os objetos são os mesmos, pode ser muito confuso para os desenvolvedores se referirem a eles ora como "usuários", ora como "membros" em componentes de URI, parâmetros de requisição e outros locais. Para a maioria das mudanças incrementais, a consistência com os padrões de design existentes será a melhor opção para seus usuários.

Como outro exemplo, se em alguns lugares você tiver um campo de resposta chamado `user` e, às vezes, seu tipo for um ID inteiro e, outras vezes, um objeto, cada desenvolvedor que receber essas duas respostas precisará verificar se o usuário é um ID inteiro ou um objeto. Essa lógica leva ao inchaço do código nas bases de código dos desenvolvedores, o que resulta em uma experiência ruim.

Isso também pode aparecer no seu próprio código. Se você mantém SDKs, precisará adicionar cada vez mais lógica para lidar com essas inconsistências e criar uma interface perfeita para os desenvolvedores. É melhor fazer isso no nível da API, mantendo a consistência em vez de introduzir novos nomes para as mesmas coisas.

**Consistência geralmente significa que existem diversos padrões e convenções repetidos em toda a sua API, de forma que os desenvolvedores consigam prever como usá-la sem consultar a documentação**. Isso pode incluir desde padrões de acesso a dados e tratamento de erros até nomenclatura. A consistência é importante porque reduz a carga cognitiva dos desenvolvedores que estão tentando entender a sua API. Ela ajuda os desenvolvedores existentes a se adaptarem a novos recursos, reduzindo a necessidade de ramificações no código, e permite que novos desenvolvedores comecem a usar imediatamente tudo o que você construiu na sua API. Em contrapartida, com menos consistência, diferentes desenvolvedores precisarão reimplementar a mesma lógica repetidamente.

### 2.3 - *Make troubleshooting easy*

Outra boa prática para o design de APIs é facilitar a resolução de problemas para os desenvolvedores. Isso pode ser feito retornando mensagens de erro significativas, bem como criando ferramentas para isso.

#### 2.3.1 - *Meaningful errors*

O que significa um erro? Um erro pode ocorrer em vários pontos do seu código, desde um erro de autorização durante uma requisição à API, até um erro de lógica de negócios quando uma entidade específica não existe, ou mesmo um erro de conexão com o banco de dados em um nível mais baixo. Ao projetar uma API, é útil facilitar ao máximo a resolução de problemas, organizando e categorizando sistematicamente os erros e a forma como são retornados. Erros incorretos ou pouco claros são frustrantes e podem afetar negativamente a adoção das suas APIs. Os desenvolvedores podem ficar presos e simplesmente desistir.

**Erros significativos são fáceis de entender, inequívocos e permitem ações concretas. Eles ajudam os desenvolvedores a compreender o problema e a resolvê-lo**. Fornecer detalhes sobre esses erros resulta em uma melhor experiência para o desenvolvedor. Códigos de erro que são strings legíveis por máquina permitem que os desenvolvedores lidem com erros em suas bases de código de forma programática.

Além dessas strings, é útil adicionar erros mais longos, seja na documentação ou em outro lugar no payload. Esses erros são às vezes chamados de erros legíveis para humanos. Melhor ainda, personalize esses erros para cada desenvolvedor. Por exemplo, com a API do Stripe, ao usar uma chave de teste no ambiente de produção, ela retorna um erro como:

> No such token tok_test_60neARX2. A similar objetct exists in test mode, but a live mode key was used to make this request.

<!--**Para começar a projetar seu sistema de erros, você pode mapear a arquitetura do seu backend ao longo do fluxo de código de uma requisição de API**. O objetivo não é expor a arquitetura do backend, mas sim categorizar os erros que ocorrem e identificar quais devem ser expostos aos desenvolvedores. A partir do momento em que uma requisição de API é feita, quais são as ações críticas executadas para atendê-la? Mapeie as diversas categorias de erros de alto nível que ocorrem durante o processamento de uma requisição de API, desde o início da requisição até os limites de serviço dentro da sua arquitetura.

Após agrupar as categorias de erros ao longo do seu código, pense em qual nível de comunicação é significativo para esses erros. Algumas opções incluem códigos de status HTTP e cabeçalhos, bem como "códigos" legíveis por máquina ou mensagens de erro mais detalhadas e legíveis por humanos, retornadas no payload da resposta. Lembre-se de que você deve retornar uma resposta de erro em um formato consistente com suas respostas normais. Por exemplo, se você retornar uma resposta JSON em uma requisição bem-sucedida, certifique-se de que o erro seja retornado no mesmo formato.

**Você também pode querer um mecanismo para propagar erros de um limite de serviço para um formato consistente na saída da sua API**. Por exemplo, um serviço do qual você depende pode apresentar diversos erros de conexão. Você informaria ao desenvolvedor que algo deu errado e que ele deve tentar novamente.

**Na maioria dos casos, você deseja ser o mais específico possível para ajudar seus desenvolvedores a tomarem a decisão correta. Em outras ocasiões, porém, pode ser interessante ocultar o problema original retornando algo mais genérico. Isso pode ser por motivos de segurança**. Por exemplo, provavelmente você não quer expor seus erros de banco de dados para o mundo externo e revelar muitas informações sobre suas conexões com o banco.

**Ao começar a organizar seus erros, você poderá reconhecer padrões que podem ser usados ​​para criar mensagens automáticas**. Por exemplo, você pode definir o esquema da sua API para exigir parâmetros específicos e ter uma biblioteca que os verifique automaticamente no início da requisição. Essa mesma biblioteca poderia formatar a mensagem de erro detalhada na resposta.

#### 2.3.2 - *Build tooling*
-->

### 2.4 - *Make your API Extensible*

Por melhor que seja o design da sua API, **sempre haverá necessidade de mudanças e crescimento à medida que seu produto evolui e a adoção por desenvolvedores aumenta**. Isso significa que **você precisa tornar sua API extensível, criando uma estratégia para sua evolução**. Isso permite que você, como provedor da API, e seu ecossistema de desenvolvedores inovem. Além disso, pode fornecer um mecanismo para lidar com alterações que quebrem a compatibilidade.

## Exercícios para discussão

Cada questão deverá ser abordada por um grupo diferente, e depois apresentado à turma.

1. Análise crítica de design (Consistência + API as a Product)

```
POST /createOrder
GET  /getOrderDetails?orderId=123
POST /orders/123/cancelOrder
GET  /userOrders?user=456
PATCH /updateOrderStatus
```

O grupo deve:

- Identificar as violações de consistência.
- Propor uma remodelagem completa dos endpoints.
- Discutir e registrar: em quais casos (se houver) um endpoint de ação ainda seria justificável?

2. Debate de evolução (Não quebrar a compatibilidade retroativa)

Suponha uma API de biblioteca.

```json
// Contrato atual (criação de livro)
{
  "title": "string (obrigatório)",
  "author": "string (obrigatório)",
  "isbn": "string (opcional)"
}
```

Nova necessidade: o campo `isbn` passa a ser obrigatório por exigência de um sistema externo. O grupo deve:

- Propor duas estratégias (uma com versionamento e uma tentando evitar versionamento).
- Para cada estratégia, definir:
  - Impacto nos consumidores atuais
  - Tempo de suporte à versão antiga
  - Forma de comunicação da mudança (headers, documentação, etc.)
  
3. Trade-off de paginação (API as a Product)

| **Contexto A** | **Contexto B** |
|---|---|
| 2.000 registros estáveis | Dezenas de milhares de eventos |
| Baixa taxa de inserção/atualização | Alta taxa de inserção |
| Usuário precisa navegar diretamente para a página 15 | Consumo típico: "carregar mais"/*infinite scroll* |

O grupo deve:

- Escolher a estratégia de paginação mais adequada para cada contexto (offset vs. cursor).
- Justificar a escolha considerando performance, consistência e experiência do consumidor.
- Mostrar um exemplo de request/response para o contexto escolhido como mais crítico.

4. Revisão de contrato em tempo real (API First)

```yaml
openapi: 3.0.0
info:
  title: Books API
  version: 1.0.0
paths:
  /books:
    get:
      parameters:
        - name: page
          in: query
          schema:
            type: integer
        - name: size
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
    post:
      responses:
        '200':
          description: Created
```

O grupo deve:

- Identificar os problemas do contrato em relação aos princípios (especialmente API First e Consistência).
- Produzir uma versão revisada do trecho, incluindo pelo menos:
  - Schema de resposta mais adequado
  - Tratamento de erro (RFC 9457)
  - Parâmetros de paginação/filtro/ordenação melhor documentados
- Justificar as principais alterações.

5. Crítica de API real (integração dos quatro princípios) --- Tarefa de casa

- Escolher uma das APIs abaixo (ou outra pública conhecida):
  - GitHub REST API
  - Stripe API
  - Spotify Web API
- Selecionar um recurso ou conjunto pequeno de endpoints da API escolhida.
- Identificar:
  - Pelo menos uma prática bem alinhada a cada um dos quatro princípios
  - Pelo menos uma violação ou trade-off discutível