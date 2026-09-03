# Aula 08

## RESTful APIs

**REST** (*REpresentational State Transfer* - Transferência de Estado Representacional) é um estilo arquitetural originalmente proposto por [Roy T. Fielding](https://ics.uci.edu/~fielding/), em sua tese [Architectural Styles and the Design of Network-based Software Architectures](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm).

Grosso modo, é um conjunto de **restrições**/**princípios de desing** **arquiteturais**. Uma API que emprega essas restrições (teoricamente em ordem) é chamada de **RESTful API**.

### Restrições

Para que uma API seja considerada verdadeiramente RESTful, ela deve seguir seis restrições fundamentais:

1. **Interface uniforme**: essa restrição define uma interface entre cliente e servidor, o que simplifica e desacopla a arquitetura do sistema, permitindo às partes evoluírem de forma independente. Os quatro princípios guias da interface uniforme são:
   1. **Baseado em recurso**: recursos individuais são identificados nas requisições através de URIs (*Uniform Resource Identifier*). Quando um cliente faz uma requisição através de uma **RESTful API**, ela responde com/transfere uma **representação do estado do recurso**. Essa representação pode ser um HTML, XML, JSON, texto, etc.
   2. **Manipulação de recursos através de representações**: através da representação de um recurso um cliente possui informações suficientes para modificar ou excluir o recurso do servidor (com as devidas permissões, obviamente).
   3. **Mensagens autodescritivas**: cada mensagem inclui informações suficientes para descrever como processar a mensagem. Por exemplo, o *parser* a ser utilizado pode ser especificado por um *Internet media type* (conhecido também por *MIME type*). As respostas também podem indicar explicitamente a "cacheabilidade" do recurso.
   4. **Hipermídia como Motor do Estado da Aplicação**: ou HATEOAS (*Hypermedia as the Engine of Application State*). As requisições enviadas, e respostas recebidas são compostas por corpo de conteúdo, cabeçalhos de requisição/resposta, URI, etc. Isso é referido como hipermídia. Além disso, também faz parte do HATEOAS que, quando necessário, links devam estar contidos nas respostas para permitir a consulta do recurso em si, ou de recursos relacionados.
2. **Stateless**: todas as informações necessárias para que uma requisição possa ser processada estão contidas na própria requisição, como parte da URI, ou de parâmetros, cabeçalho, etc.
3. **Cacheabilidade:** os dados devem ser marcados como cacheáveis ou não para otimizar as interações.
4. **Cliente-Servidor**: separação de preocupações entre a interface do usuário e o armazenamento de dados.
5. **Sistema em Camadas:** o cliente não consegue saber se está conectado diretamente ao servidor final ou a intermediários (como balanceadores de carga).
6. **Código sob Demanda (opcional):** capacidade do servidor de enviar código executável para o cliente.

### Convenções / Melhores práticas

- [Nomeação de recursos](https://restapitutorial.com/introduction/restquicktips#provide-sensible-resource-names)
- [Métodos](https://restapitutorial.com/introduction/restquicktips#provide-sensible-resource-names)

  Os métodos para uma **RESTful API** devem se alinhar aos métodos de requisição HTTP.

  | **Recurso** | **POST** | **GET** | **PUT** | **DELETE** |
  |---|---|---|---|---|
  | /clientes | Cria um novo cliente | Retorna todos os clientes | Atualização de todos os clientes | Exclui todos os clientes |
  | /clientes/1 | Erro | Retorna os detalhes do cliente 1 | Atualiza os detalhes do cliente 1 (se existir) | Exclui o cliente 1 |
  | /clientes/1/pedidos | Cria um novo pedido para o cliente 1 | Retorna todos os pedidos do cliente 1 | Atualização de todos os pedidos do cliente 1 | Exclui todos os pedidos do cliente 1 |

  Exemplo:

  ```
  POST https://api.padaria.com/clientes/5/pedidos
  Content-Type: application/json; charset=utf-8
  Content-Length: ...

  {"Id":1,"Nome":"Filé à Parmegiana","Preço":25.9}
  ```

  - [Valores de retorno recomendados para cada método HTTP primário](https://restapitutorial.com/introduction/httpmethods#overview).
- [Implementar métodos assíncronos](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-asynchronous-methods)
- [Implementar paginação de dados e filtragem](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-data-pagination-and-filtering)
- [Ter suporte a respostas parciais](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#support-partial-responses)
- [Implementar HATEOAS](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-hateoas)
- [Implementar versionamento](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-versioning)
- etc.

### OpenAPI

A [Iniciativa OpenAPI](https://www.openapis.org/) foi criada por um consórcio da indústria para padronizar as descrições de APIs REST entre diferentes fornecedores. A especificação de padronização era chamada de `Swagger` antes de ser incorporada à iniciativa OpenAPI e renomeada para [OpenAPI *Specification* (OAS)](https://spec.openapis.org/oas/latest.html).

- [Documentação](https://learn.openapis.org/).

## Atividade da semana

Considere as seguintes listas de paradigmas de API:

- RPC, GraphQL.
- WebHooks, WebSockets, HTTP Streaming.

1. Cada dupla deve escolher um paradigma de cada lista e implementar uma API simples de cada paradigma escolhido. O que deve ser implementado:
   1. **Consultas a dados coletados (escrita/leitura)**. Por exemplo, o uso do seu hardware (CPU, RAM), ou algum outro tipo de métrica de uso em algum site.
   2. Os dados coletados devem ficar armazenados em um servidor simulado.
      1. [WebHooks, WebSockets, HTTP Streaming]: transmissão dos dados coletados em tempo real, ou em um intervalo fixo (ex.: a cada 5 minutos).
      2. [RPC, GraphQL]: consulta ao histórico gravado das métricas (ex.: média de uso da CPU nos últimos 10 minutos).
2. A dupla criará um relatório sobre a implementação. 
   1. O que deve ser inserido no relatório:
      1. Os paradigmas de APIs escolhidos.
      2. Descrição das APIs desenvolvidas.
      3. Um breve estudo comparando o comportamento das APIs. Por exemplo: qual o impacto de cada uma no consumo de memória, ou no uso de CPU; em qual API houve maior facilidade de extração de subconjuntos de dados (sem que tenha vindo *payloads* desnecessários), etc.
   2. O relatório deve ser entregue no formato PDF.