# Aula 07

## RESTful APIs[^1]

[^1]: Materiais utilizados como fonte: [1](https://www.redhat.com/en/topics/api/what-is-a-rest-api), [2](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [3](https://restapitutorial.com/introduction).

**REST** (*REpresentational State Transfer* - Transferência de Estado Representacional) é um conjunto de **restrições**/**princípios de desing** **arquiteturais**. Uma API que emprega essas restrições (ou princípios) é chamada de **RESTful API**.

### Restrições

Para que uma API seja considerada verdadeiramente RESTful, ela deve seguir seis restrições fundamentais:

1. **Interface uniforme**: essa restrição define uma interface entre cliente e servidor, o que simplifica a arquitetura do sistema, permitindo às partes evoluírem de forma independente. Os quatro princípios guias da interface uniforme são:
   1. **Baseado em recurso**: recursos individuais são identificados nas requisições através de URIs (*Uniform Resource Identifier*). Quando um cliente faz uma requisição através de uma **RESTful API**, ela responde com/transfere uma **representação do estado do recurso**. Essa representação pode ser um HTML, XML, JSON, texto, etc.
   2. **Manipulação de recursos através de representações**: através da representação de um recurso um cliente possui informações suficientes para modificar ou excluir o recurso do servidor (com as devidas permissões, obviamente).
   3. **Mensagens autodescritivas**: cada mensagem inclui informações suficientes para descrever como processar a mensagem. Por exemplo, o *parser* a ser utilizado pode ser especificado por um *Internet media type* (conhecido também por *MIME type*). As respostas também podem indicar explicitamente a "cacheabilidade" do recurso.
   4. **Hipermídia como Motor do Estado da Aplicação**: ou HATEOAS (*Hypermedia as the Engine of Application State*). As requisições enviadas, e respostas recebidas são compostas por corpo de conteúdo, cabeçalhos de requisição/resposta, URI, etc. Isso é referido como hipermídia. Além disso, também faz parte do HATEOAS que, quando necessário, links devam estar contidos nas respostas para permitir a consulta do recurso em si, ou de recursos relacionados.
2. **Stateless**: todas as informações necessárias para que uma requisição possa ser processada estão contidas na própria requisição, como parte da URI, ou de parâmetros, cabeçalho, etc.
3. **Cacheabilidade:** os dados devem ser marcados como cacheáveis ou não para otimizar as interações.
4. **Cliente-Servidor**: separação de preocupações entre a interface do usuário e o armazenamento de dados.
5. **Sistema em Camadas:** o cliente não consegue saber se está conectado diretamente ao servidor final ou a intermediários (como balanceadores de carga).
6. **Código sob Demanda (opcional):** capacidade do servidor de enviar código executável para o cliente.

### Métodos

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

Valores de retorno recomendados para cada método HTTP primário: https://restapitutorial.com/introduction/httpmethods#overview ou https://restapitutorial.com/introduction/httpmethods#overview

Métodos assíncronos: https://restapitutorial.com/introduction/httpmethods#overview

### Convenções para nomeamento de URI

https://restapitutorial.com/introduction/httpmethods#overview

### Paginação e filtragem

https://restapitutorial.com/introduction/httpmethods#overview

### Versionamento

https://restapitutorial.com/introduction/httpmethods#overview

### OpenAPI

https://restapitutorial.com/introduction/httpmethods#overview

## Atividades

1. Pesquisar sobre OAS (*OpenAPI Specification*)