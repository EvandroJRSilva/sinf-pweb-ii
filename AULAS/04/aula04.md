# Aula 04

## [RFC 9110: STD 97: HTTP Semantics](https://www.rfc-editor.org/info/rfc9110):

### 5. [Fields](https://www.rfc-editor.org/info/rfc9110/#section-5)

Essa seção formaliza o mecanismo de extensibilidade baseado em pares nome/valor (*fields*) que aparecem nas seções de *header* e *trailer*. 

- Um ***field*** name é um token case-insensitive; o valor associado carrega a semântica registrada para aquele nome. Campos não reconhecidos devem, em geral, ser ignorados pelos receptores (exceto proxies, que os encaminham, a menos que constem no header Connection).
- Os campos são transmitidos como “field lines”. Quando o mesmo nome aparece várias vezes, o valor combinado é a concatenação ordenada dos valores, separados por vírgula (quando a definição do campo for list-based). 
- A ordem entre ***fields*** de nomes distintos é insignificante; a **ordem entre linhas do mesmo nome** é significativa e deve ser preservada pelos proxies. 
- Não há limites absolutos de tamanho definidos pela especificação, mas servidores devem rejeitar campos excessivamente longos com status 4xx para evitar vulnerabilidades de smuggling.
- O valor de um ***field*** segue regras comuns de gramática (OWS, RWS, BWS, quoted-string, parâmetros, listas com a notação “#”, HTTP-date etc.). 
- Remetentes não devem gerar elementos de lista vazios; receptores devem ser robustos. Campos de trailer só podem ser usados se a definição do ***field*** permitir explicitamente.

#### Atividade

- Estudar o registro de field names da IANA e a distinção entre hop-by-hop e end-to-end (via Connection). 
- **Responder:** por que a ordem de fields de nomes diferentes não importa, mas a ordem de valores combinados do mesmo nome importa?

### 6. [Message Abstraction](https://www.rfc-editor.org/info/rfc9110/#section-6)

A seção 6 define um modelo abstrato de mensagem HTTP independente da sintaxe de qualquer versão específica. Uma mensagem consiste em:

- **Control data** (método + target + versão em requisições; status + razão + versão em respostas);
- tabela de header fields;
- um stream potencialmente ilimitado de content (corpo);
- tabela opcional de trailer fields.

A mensagem é processada de forma *streaming*: 

1. Control data e headers primeiro; 
2. Depois o content e, 
3. Por fim, trailers (quando o framing permitir). 

A mensagem é autodescritiva: após a decodificação, o receptor deve ser capaz de interpretar o conteúdo sem estado adicional do remetente (com a exceção de respostas a HEAD, que se assemelham a GET truncadas).

- ***Framing*** e completude são responsabilidade da versão concreta (Content-Length, chunked, frames HTTP/2 etc.).
- ***Trailers*** não podem alterar decisões já tomadas com base nos headers (roteamento, autenticação etc.). 
- Campos de metadata de mensagem (Date, Trailer) descrevem a origem e a expectativa de trailers.
  
Essa abstração permite que uma mensagem seja retransmitida entre versões diferentes sem alteração de significado, desde que as regras de *forwarding* sejam respeitadas.

#### Atividade

- Ler: 
  - [HTTP/2](https://www.rfc-editor.org/info/rfc9113/) - Introdutório
  - [HTTP/3](https://www.rfc-editor.org/info/rfc9114/) - Introdutório
- Comparar o modelo abstrato com as regras de framing concretas de RFC 9112 (HTTP/1.1), RFC 9113 (HTTP/2) e RFC 9114 (HTTP/3).
- **Responder:** por que trailers não podem retroativamente modificar decisões de roteamento ou autenticação?

### 8. [Representation Data and Metadata](https://www.rfc-editor.org/info/rfc9110/#section-8)

Uma representação é a informação que reflete o estado de um recurso em um determinado momento, composta por **representation data** (o *stream* de octetos) e **representation metadata** (os *fields* que descrevem como interpretar esses octetos).

Os principais ***fields*** de metadata são:

- **Content-Type:** media type e parâmetros (ex.: charset);
- **Content-Encoding:** codificações de conteúdo aplicadas em sequência (gzip, deflate etc.);
- **Content-Language:** linguagem(ns) natural(is) do conteúdo;
- **Content-Length:** número de octetos (quando conhecido e não houver Transfer-Encoding);
- **Content-Location:** URI que identifica a representação específica (pode diferir do target URI).

Os ***validator fields*** (Last-Modified e ETag) permitem validação condicional e caching. 

- Last-Modified é um carimbo de data aproximado; 
- ETag é um identificador opaco (forte ou fraco). 

Validadores fortes mudam sempre que a representação muda de forma observável; validadores fracos permitem equivalência semântica.

A relação entre data e metadata é estrita: o receptor usa a metadata para interpretar e validar o data. Ausência de Content-Type em respostas com corpo é desaconselhada (default implícito application/octet-stream).

#### Atividade

- Ler RFC 9111 (Caching) e a seção de content negotiation (Seção 12 do próprio 9110).
- **Responder:** qual a diferença prática entre um ETag forte e um fraco no contexto de If-None-Match versus If-Range?

## Atividade da semana

- Registrar pelo menos 50 mensagens de requisição e resposta a partir de variadas interações da dupla na web (sistemas diversos, portais institucionais ou de notícias, sistemas web próprios que vocês estejam desenvolvendo, redes socias, etc.), com o uso de pelo menos 5 dos métodos padronizados.
- Analisar e descrever *requests* e *responses* de forma detalhada, ou seja, dissertando sobre o contexto da requisição (i.e., o máximo de detalhes não-sensíveis possíveis), os campos de cabeçalho e seus valores, métodos, conteúdos do *body*, códigos de status, etc.