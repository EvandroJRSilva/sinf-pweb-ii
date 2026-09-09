# Exercícios para AV1

## 1 

Sobre a arquitetura *3-tier*  e suas variações, analise as afirmações e indique a que descreve uma característica correta e distintiva desse modelo em relação ao *2-tier*.

A) Na arquitetura 3-tier, a camada de apresentação é responsável pela lógica de negócios, enquanto a camada de dados gerencia a interface com o usuário.

B) A camada intermediária (lógica de negócios) em uma arquitetura 3-tier é frequentemente implementada como uma aplicação *stateful*, garantindo alta disponibilidade.

C) A principal desvantagem do modelo 3-tier é a centralização do processamento, o que reduz a segurança e a capacidade de auditoria das transações.

D) A separação entre a lógica de negócios e a lógica de apresentação no modelo 3-tier permite que a camada de negócios seja reutilizada por diferentes interfaces (web, mobile, desktop), promovendo a manutenibilidade.

E) No modelo 3-tier, a comunicação entre o cliente e a camada de negócios é necessariamente realizada via *Remote Procedure Call* (RPC), o que limita a interoperabilidade.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 2

Considere as definições da seção 3 do RFC 9110, que estabelece a terminologia e os conceitos centrais do HTTP. O protocolo HTTP é baseado em uma arquitetura cliente-servidor e utiliza o conceito de "recursos". Sobre este conceito, é correto afirmar:

A) Um recurso é qualquer arquivo ou documento estático armazenado no servidor, como imagens, HTML e CSS.

B) A identificação de um recurso é feita exclusivamente por seu nome de arquivo no sistema de arquivos do servidor.

C) Recursos são entidades imutáveis, e sua representação nunca se altera, independentemente do contexto ou da negociação de conteúdo.

D) O conceito de recurso no HTTP está estritamente ligado à localização física do dado no servidor, sendo a URI uma referência direta a esse local.

E) Recurso é um conceito abstrato mapeado por uma URI, podendo ser qualquer coisa que tenha identidade, como um documento, uma imagem, um serviço ou uma coleção de outros recursos.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 3

Em sistemas distribuídos, a escolha entre uma arquitetura *stateful* e *stateless* impacta diretamente o design da aplicação. Um exemplo clássico onde a adoção de uma abordagem *stateless* é preferível em detrimento da *stateful* é:

A) Um sistema de carrinho de compras em um e-commerce, onde o estado da seleção de itens do usuário deve ser mantido entre as requisições.

B) Uma aplicação bancária de transferências, onde a consistência transacional e a confiabilidade são críticas.

C) Um editor de texto colaborativo em tempo real, onde múltiplos usuários editam o mesmo documento simultaneamente.

D) Um serviço de disponibilização de conteúdo estático (como imagens, CSS e JavaScript), onde a ausência de estado do servidor permite o uso eficiente de *caches* e *load balancers*.

E) Uma aplicação de chat onde o servidor precisa manter o histórico de mensagens não lidas para cada usuário.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 4

A seção 8 do RFC 9110 é dedicada aos dados de representação e metadados (*Representation Data and Metadata*). A representação de um recurso é a informação que reflete seu estado atual ou desejado. Sobre os metadados de representação, analise a alternativa correta.

A) Os metadados de representação são transmitidos exclusivamente no corpo da mensagem HTTP, não tendo relação com os cabeçalhos.

B) O cabeçalho `Content-Language` é um metadado que descreve a linguagem natural do corpo da mensagem, e sua presença é obrigatória para qualquer recurso que não seja em inglês.

C) O metadado `Content-Length` é um exemplo de metadado de representação que descreve o tamanho dos dados, mas sua inclusão é opcional e não recomendada para melhorar a performance.

D) A negociação de conteúdo (*Content Negotiation*) é o processo de selecionar a melhor representação para um dado recurso, e os metadados de representação, como `Content-Type`, são irrelevantes nesse processo.

E) Os cabeçalhos `Content-Type` e `Content-Encoding` são exemplos de metadados de representação que informam ao receptor como interpretar e decodificar o corpo da mensagem, respectivamente.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 5

A API WebSocket é amplamente utilizada para criar aplicações interativas em tempo real. Em comparação com as requisições HTTP tradicionais e com HTTP Streaming, assinale a alternativa que descreve corretamente uma vantagem específica da utilização de WebSockets.

A) WebSockets opera sobre o protocolo UDP, o que garante menor latência e maior confiabilidade na entrega de pacotes.

B) WebSockets estabelecem uma conexão full-duplex e persistente entre cliente e servidor, permitindo que ambos os lados enviem mensagens a qualquer momento, sem o *overhead* de uma nova conexão HTTP para cada mensagem.

C) A comunicação via WebSockets é baseada em um modelo *request-response* assíncrono, onde o cliente sempre inicia a comunicação.

D) Diferentemente do HTTP Streaming, WebSockets não possuem suporte a *headers* ou metadados, o que simplifica a mensagem.

E) WebSockets são limitados a mensagens de texto (UTF-8), não suportando dados binários, ao contrário do HTTP Streaming.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 6

De acordo com a seção 9 do RFC 9110, os métodos HTTP definem a operação desejada a ser executada em um recurso. Sobre a semântica dos métodos, é incorreto afirmar:

A) O método GET é utilizado para recuperar uma representação de um recurso e é considerado seguro e idempotente.

B) O método POST é utilizado para submeter uma entidade a um recurso, frequentemente causando uma mudança de estado ou efeitos colaterais no servidor.

C) O método DELETE é seguro, pois não causa efeitos colaterais no servidor além da remoção do recurso, podendo ser repetido inúmeras vezes sem consequências adversas.

D) O método PUT solicita que o estado do recurso de destino seja criado ou substituído pela representação contida na mensagem de requisição.

E) O método HEAD é idêntico ao GET, exceto que o servidor não deve retornar um corpo de mensagem na resposta, sendo útil para obter metadados.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 7

A arquitetura orientada a recursos do REST, aliada à semântica dos métodos HTTP, estabelece um padrão para operações CRUD. Considerando uma API RESTful para gerenciamento de usuários, mapeie as operações para os métodos HTTP e assinale a alternativa que segue corretamente as boas práticas do REST.

A) Para substituir completamente um usuário existente, utiliza-se o método PUT no recurso `/users/{id}` com a nova representação no corpo da requisição.

B) Para deletar um usuário, utiliza-se o método POST no recurso `/users/{id}/delete`.

C) Para criar um novo usuário, utiliza-se o método GET no recurso `/users/new` com os dados no corpo da requisição.

D) Para listar todos os usuários, utiliza-se o método GET no recurso `/users/list` com parâmetros de paginação na URI.

E) Para atualizar parcialmente um usuário, utiliza-se o método PUT no recurso `/users/{id}`.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 8

No contexto de APIs, o padrão de comunicação conhecido como WebHooks é frequentemente descrito como uma "API reversa". Essa denominação se deve ao fato de que:

A) No WebHooks, a API é chamada pelo cliente, que aguarda a resposta do servidor, invertendo o fluxo tradicional de dados.

B) O WebHook é uma técnica de *proxy* reverso, onde o cliente se conecta ao servidor através de um intermediário que inverte a direção dos pacotes.

C) Diferentemente das APIs tradicionais, o WebHook não utiliza o protocolo HTTP, mas sim um protocolo próprio e reverso.

D) No WebHooks, o provedor do serviço (servidor) faz uma requisição HTTP para uma URL fornecida pelo cliente (`callback`), notificando-o sobre um evento, invertendo os papéis tradicionais de cliente e servidor na comunicação.

E) O termo "API reversa" refere-se à capacidade do WebHook de reverter uma transação, funcionando como um *rollback* para operações de dados.
\end{choices}

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 9

A seção 4 do RFC 9110 aborda os Identificadores em HTTP, detalhando o papel fundamental das URIs (*Uniform Resource Identifiers*). Sobre a sintaxe e a semântica das URIs em HTTP, assinale a afirmação verdadeira.

A) A parte da *query* em uma URI (`?key=value`) é utilizada para identificar um recurso dentro de uma hierarquia, sendo parte essencial do caminho (*path*) do recurso.

B) O componente de *fragment* em uma URI (ex: `\#section-2`) é enviado ao servidor, que o utiliza para retornar apenas a parte específica do recurso.

C) O esquema `https` na URI indica que o protocolo a ser usado é HTTP sobre TLS, mas isso não implica que a conexão seja segura, apenas que o servidor entende o protocolo.

D) A URI de destino em uma requisição HTTP é composta pelo esquema, autoridade (host e porta), caminho e, opcionalmente, *query*, sendo o \textit{fragment} processado apenas pelo agente usuário (cliente) e não enviado ao servidor.

E) URIs são opcionais em requisições HTTP, podendo o servidor inferir o recurso desejado a partir de outros cabeçalhos, como `Host`.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 10

Ao projetar uma API GraphQL, os desenvolvedores definem um esquema (*schema*) que descreve os tipos de dados e as operações disponíveis. Sobre a natureza e o uso desse esquema, é correto afirmar:

A) O esquema GraphQL é dinâmico e pode ser alterado em tempo de execução sem a necessidade de reiniciar o servidor.

B) O esquema GraphQL atua como um contrato forte entre o cliente e o servidor, definindo quais dados podem ser solicitados e de que forma, permitindo validação em tempo de compilação do lado do cliente.

C) A principal função do esquema é otimizar o desempenho do banco de dados, definindo índices e chaves estrangeiras para as entidades do sistema.

D) O esquema GraphQL não impõe restrições de tipo, permitindo que o cliente envie qualquer estrutura de dados nas operações, desde que seja um JSON válido.

E) O esquema é definido utilizando a linguagem de definição de interface (IDL) do GraphQL, e o servidor expõe apenas as consultas (*queries*) definidas no esquema, não as mutações.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 11

Sobre os métodos HTTP definidos na seção 9 do RFC 9110, a propriedade da **idempotência** é fundamental para a confiabilidade de sistemas distribuídos. Qual das seguintes sequências de métodos é composta exclusivamente por métodos considerados idempotentes?

A) GET, POST, PUT, DELETE
B) GET, PUT, DELETE, HEAD, OPTIONS
C) GET, PUT, POST, TRACE
D) GET, POST, HEAD, OPTIONS
E) POST, PATCH, DELETE, CONNECT

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 12

Em arquiteturas *n-tier*, a separação de responsabilidades entre as camadas de apresentação, negócios e dados é um princípio consolidado. Uma desvantagem comum desse modelo, especialmente quando comparado a uma arquitetura *2-tier*, é:

A) A menor segurança, devido ao maior número de pontos de entrada para a aplicação.

B) O aumento da complexidade e da latência devido à comunicação entre as camadas, que pode envolver chamadas de rede e serialização de objetos.

C) A redução da escalabilidade, pois a camada de negócios se torna um gargalo.

D) O aumento do acoplamento entre a lógica de negócios e a interface do usuário.

E) A dificuldade em aplicar regras de negócios centralizadas, pois elas são distribuídas entre as camadas.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 13

No contexto de APIs orientadas a eventos, o HTTP Streaming surge como uma alternativa para envio de dados em tempo real. Considerando suas características técnicas, assinale a alternativa que descreve corretamente como o HTTP Streaming viabiliza a comunicação assíncrona.

A) O servidor envia os dados em um fluxo contínuo através de uma única conexão HTTP mantida aberta, utilizando a codificação de transferência *chunked* para fragmentar a resposta, permitindo que o cliente processe os dados à medida que chegam.

B) O servidor mantém a conexão aberta e envia dados em múltiplas respostas HTTP separadas, cada uma com seu próprio código de status.

C) O HTTP Streaming é limitado ao envio de dados no formato JSON, não suportando outros *media types*.

D) O cliente envia uma requisição e o servidor fecha a conexão imediatamente, enviando um *webhook* com os dados posteriormente.

E) O HTTP Streaming utiliza o mesmo *handshake* que o WebSocket, estabelecendo uma conexão full-duplex.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 14

A arquitetura RESTful é fundamentada em seis restrições arquiteturais. Uma dessas restrições, o "Sistema de Camadas" (*Layered System*), permite que intermediários (como proxies e gateways) sejam inseridos entre o cliente e o servidor. Qual o principal benefício arquitetural obtido com essa restrição?

A) Aumentar a segurança, criptografando as mensagens em cada camada.

B) Reduzir a latência, eliminando a necessidade de *handshakes* TCP.

C) Promover o desacoplamento, abstraindo a localização do servidor e permitindo balanceamento de carga e *caching* sem que o cliente precise saber.

D) Permitir a execução de código no cliente (*Code on Demand*), melhorando a performance.

E) Garantir a consistência transacional através de *two-phase commits* entre as camadas.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 15

O RFC 9110 especifica que o HTTP é um protocolo *stateless*. Isso significa que o servidor não mantém informações sobre requisições anteriores. Para superar essa limitação e criar aplicações com sessões, utilizam-se *cookies*. Sobre o funcionamento dos *cookies* no HTTP, é correto afirmar que:

A) O *cookie* é enviado pelo servidor ao cliente através do cabeçalho `Set-Cookie` e é automaticamente incluído pelo cliente em todas as requisições subsequentes para o mesmo domínio, por meio do cabeçalho `Cookie`.

B) O servidor armazena o estado da sessão no *cookie* que é enviado ao cliente, e o cliente é responsável por manter a integridade desse estado.

C) O *cookie* é um mecanismo de estado no lado do cliente, onde o servidor envia dados (via `Set-Cookie`) para serem armazenados pelo cliente, que os envia de volta em requisições futuras (via `Cookie`), permitindo a manutenção de sessões.

D) Os *cookies* de sessão são armazenados no servidor, e o cliente recebe apenas uma chave de referência (*session ID*) que é enviada via `Cookie`.

E) *Cookies* são a única forma de gerenciar sessões em aplicações web, e seu uso é obrigatório mesmo em APIs RESTful.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 16

Em uma API RESTful, a utilização de *hypermedia* como o motor do estado da aplicação (HATEOAS) é um princípio fundamental. O que o HATEOAS proporciona a uma API REST?

A) A capacidade de retornar dados em múltiplos formatos, como JSON e XML.

B) Aumento da performance, reduzindo o número de requisições necessárias para completar uma tarefa.

C) Um mecanismo de autenticação mais seguro, baseado em tokens gerados dinamicamente.

D) A eliminação da necessidade de documentação, já que a API se auto-descreve.

E) O desacoplamento entre cliente e servidor, onde o servidor fornece *links* dinâmicos que indicam quais ações são possíveis a partir do estado atual do recurso, guiando o cliente pela aplicação.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 17

As APIs RPC modernas, como o gRPC, apresentam vantagens significativas em cenários de microserviços e alta performance. Uma dessas vantagens em relação a APIs REST baseadas em JSON é:


A) A utilização de JSON como formato de serialização, que é mais leve e rápido que o XML.

B) A simplicidade de depuração, pois as mensagens são texto puro e legíveis por humanos.

C) O suporte nativo a transações distribuídas e *rollback* automático.

D) O uso de Protocol Buffers como formato de serialização binária, que gera mensagens menores e mais rápidas de serializar/deserializar, além de suportar *streaming* bidirecional nativamente.

E) A facilidade de integração com navegadores, já que o gRPC utiliza HTTP/2 e é suportado por todas as bibliotecas JavaScript.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 18

De acordo com a seção 5 do RFC 9110, o cabeçalho `Accept` é utilizado para negociação de conteúdo. Assinale a alternativa que descreve corretamente o seu uso e propósito.

A) O cabeçalho `Accept` é enviado pelo servidor para informar ao cliente quais *media types* ele é capaz de gerar.

B)  O cliente utiliza o cabeçalho `Accept` para informar ao servidor qual o *charset* dos dados que ele está enviando no corpo da requisição.

C) O cabeçalho `Accept` especifica a linguagem preferida do cliente para a representação do recurso, como `Accept-Language: pt-BR`.

D) O cabeçalho `Accept` é utilizado pelo cliente para listar os *media types* (ex: `application/json`}, `text/xml`) que ele é capaz de processar, permitindo ao servidor selecionar a representação mais adequada do recurso.

E) O servidor ignora o cabeçalho `Accept` em APIs RESTful, retornando sempre o formato JSON, que é o padrão da indústria.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 19

Uma diferença crucial entre APIs REST e GraphQL reside na forma como lidam com a versão e a evolução da API. Sobre essa diferença, assinale a alternativa correta.

A) GraphQL permite a evolução da API sem a necessidade de versionamento, pois novos campos podem ser adicionados ao esquema sem quebrar consultas existentes, enquanto campos depreciados podem ser marcados e removidos gradualmente.

B) GraphQL não suporta versionamento, sendo necessário criar uma nova API para cada versão.

C) REST é mais flexível para evolução, pois o cliente pode solicitar campos arbitrários, independentemente do servidor.

D) REST exige versionamento explícito na URL (ex: \texttt{/v2/users}) para qualquer mudança, enquanto GraphQL é imune a mudanças quebradas.

E) Tanto REST quanto GraphQL utilizam o mesmo mecanismo de versionamento baseado em cabeçalhos HTTP (\texttt{Accept-Version}).

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 20

A arquitetura *2-tier*, frequentemente associada a aplicações cliente-servidor tradicionais, apresenta um desafio significativo em relação à manutenção e escalabilidade. Esse desafio é mais pronunciado quando comparado a uma arquitetura *3-tier*, especificamente devido a:

A) A necessidade de instalar o cliente em cada máquina, o que aumenta a complexidade de distribuição.

B) A comunicação direta entre o cliente e o servidor de banco de dados, que pode expor a estrutura do banco e aumentar a superfície de ataque.

C) A impossibilidade de utilizar *load balancers* para distribuir a carga entre múltiplos servidores.

D) A falta de suporte a transações, o que compromete a integridade dos dados.

E) A presença da lógica de negócios frequentemente embutida na interface do usuário (cliente) ou em *stored procedures* no banco de dados, tornando a manutenção e evolução do sistema mais difícil e acoplada.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 21

No contexto de arquitetura de sistemas, um exemplo típico de aplicação que se beneficia mais de um design *stateful* do que *stateless* é:

A) Uma API de listagem de produtos de um e-commerce.

B) Uma aplicação de *e-commerce* com um carrinho de compras, onde o estado do carrinho precisa ser mantido entre as interações do usuário antes da finalização da compra.

C) Um sistema de monitoramento de logs de servidores.

D) Um serviço de resolução de DNS.

E) Um serviço de tradução de texto em tempo real.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 22

O modelo de APIs baseado em GraphQL apresenta desafios, como a complexidade na implementação de *caching* e a exposição de *endpoints* que podem ser alvo de ataques de negação de serviço (DoS) através de consultas aninhadas profundas (*deeply nested queries*). Para mitigar esse risco, uma prática comum de segurança é:

A) Utilizar tokens JWT com tempo de expiração curto.

B) Restringir o acesso à API apenas por IPs confiáveis.

C) Utilizar HTTPS (TLS) para criptografar todas as requisições.

D) Implementar limites de complexidade nas consultas, como profundidade máxima, número de campos e custo estimado de execução, para evitar consultas maliciosas que sobrecarreguem o servidor.

E) Utilizar o método HTTP POST em vez de GET para todas as operações.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 23

A seção 9 do RFC 9110 define os métodos HTTP. O método PATCH é utilizado para aplicar modificações parciais a um recurso. Qual a principal diferença semântica entre o PATCH e o PUT?

A) PUT e PATCH são sinônimos e podem ser usados de forma intercambiável para atualizações parciais.

B) PATCH é idempotente, enquanto PUT não é.

C) PUT é usado apenas para criar recursos, enquanto PATCH é usado para atualizar.

D) PUT requer que o cliente envie a representação completa do recurso, enquanto PATCH envia apenas as diferenças, mas ambos têm a mesma semântica de substituição.

E) PUT substitui a representação completa do recurso, exigindo que o cliente envie o estado final desejado, enquanto PATCH aplica um conjunto de instruções de mudança, sendo não necessariamente idempotente, embora possa ser.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 24

Na arquitetura REST, a utilização da interface uniforme, uma de suas restrições, é composta por quatro aspectos: identificação de recursos; manipulação de recursos através de representações; mensagens auto-descritivas; e *hypermedia* como motor do estado da aplicação (HATEOAS). O aspecto de "mensagens auto-descritivas" é alcançado principalmente através:

A) Do uso de metadados, como os cabeçalhos HTTP (`Content-Type`, `Accept`, etc.) e a própria semântica dos métodos HTTP, para que cada mensagem contenha informações suficientes para que o receptor entenda como processá-la, sem depender de contexto externo.

B) Da inclusão de documentação extensiva no corpo das respostas.

C) Do uso de *schemas* JSON para validar as mensagens.

D) Da padronização dos códigos de status HTTP e da exigência de que o cliente mantenha o estado da sessão.

E) Da utilização de URIs amigáveis e verbos HTTP no corpo da mensagem.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 25

A arquitetura de APIs orientadas a eventos, como WebHooks e WebSockets, contrasta com o modelo tradicional de requisição-resposta (REST, RPC, GraphQL) na forma como a comunicação é iniciada e mantida. Sobre as características e aplicações desses modelos, considere as seguintes afirmativas e assinale a alternativa correta.

A) WebHooks são mais adequados para cenários que exigem comunicação bidirecional contínua e de baixa latência, como jogos multiplayer, enquanto WebSockets são ideais para notificações esporádicas de sistemas externos.

B) Em WebHooks, o cliente precisa manter uma conexão persistente com o servidor para receber as notificações, o que consome recursos significativos do lado do cliente.

C) O padrão REST é inerentemente orientado a eventos, pois cada requisição GET pode ser interpretada como um evento de consulta que o servidor processa de forma assíncrona.

D) GraphQL, por suportar subscriptions, pode ser considerado um híbrido entre requisição-resposta e orientação a eventos, mas ainda assim requer polling constante do cliente para verificar novas atualizações.

E) WebHooks são apropriados para integrações entre sistemas onde um serviço precisa notificar outro sobre a ocorrência de eventos específicos (ex: pagamento processado, novo usuário registrado), sem a necessidade de manter uma conexão ativa, enquanto WebSockets são mais adequados para interfaces de usuário que exigem atualizações em tempo real e interação contínua entre cliente e servidor.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 26

No desenvolvimento de sistemas corporativos, a escolha da arquitetura de software desempenha um papel fundamental na manutenibilidade, escalabilidade e distribuição de responsabilidades. A arquitetura cliente-servidor tradicional evoluiu ao longo das décadas para atender a diferentes demandas operacionais. Quando analisamos a variante de três camadas (*3-tier*), é correto afirmar que a sua principal característica estrutural é:

A) A execução do banco de dados, da lógica de negócios e da interface gráfica dentro de um mesmo processo único na máquina do cliente.

B) A separação clara das responsabilidades em três camadas distintas: apresentação (interface do usuário), lógica de aplicação (negócios) e gestão de dados (banco de dados).

C) O uso exclusivo do protocolo HTTP para a comunicação direta entre a interface de usuário e os arquivos físicos do banco de dados.

D) A eliminação completa do servidor de aplicação, permitindo que o cliente se conecte diretamente ao banco de dados sem intermediários.

E) O acoplamento rígido entre a interface gráfica e os procedimentos armazenados (*stored procedures*) diretamente na camada de armazenamento.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 27

Em aplicações web modernas, a gestão do estado entre requisições consecutivas é uma consideração central de design. As arquiteturas podem ser classificadas genericamente em *stateful* ou *stateless*. Qual das seguintes alternativas descreve corretamente o comportamento essencial de uma arquitetura *stateless*?

A) O servidor mantém uma sessão ativa em memória para cada cliente, exigindo que requisições subsequentes do mesmo cliente sejam direcionadas ao mesmo nó.

B) Cada requisição enviada pelo cliente deve conter todas as informações necessárias para ser processada, sem dependência de contexto mantido no servidor.

C) O banco de dados é proibido de armazenar dados persistentes, delegando ao cliente a responsabilidade de guardar todo o histórico da aplicação.

D) A comunicação entre cliente e servidor é realizada sem o envio de cabeçalhos de autenticação ou metadados de protocolo.

E) O servidor é incapaz de processar requisições concorrentes, devendo responder a um cliente por vez em ordem estritamente sequencial.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 28

A RFC 9110 define o núcleo do protocolo HTTP e estabelece a terminologia essencial utilizada para descrever seus componentes. Na Seção 3 da referida especificação, o termo *User Agent* (Agente do Usuário) refere-se a:

A) Um servidor intermediário que retransmite mensagens HTTP entre clientes e servidores de origem sem alterar o conteúdo.

B) O administrador de rede responsável por configurar os certificados SSL/TLS nos servidores web corporativos.

C) Qualquer programa de computador que inicia uma requisição HTTP, como um navegador web, um leitor RSS ou um cliente de linha de comando.

D) Um processo em segundo plano no servidor responsável por encerrar conexões inativas ou expiradas.

E) O módulo do sistema operacional encarregado do roteamento IP e da resolução de nomes via DNS.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 29

No protocolo HTTP (RFC 9110, Seção 4), os identificadores de recursos desempenham um papel central para que clientes possam localizar e interagir com objetos ou serviços em um servidor. O termo URI (*Uniform Resource Identifier*) abrange tanto URLs quanto URNs. Em relação às URLs, é correto afirmar que elas:

A) Identificam um recurso por meio do seu nome único e persistente, independentemente de sua localização geográfica ou de rede.

B) Exigem que todos os caminhos (*paths*) sejam codificados em formato binário base64 antes do envio.

C) São utilizadas exclusivamente no cabeçalho de resposta para indicar a versão do protocolo suportada pelo servidor.

D) Fornecem o meio de localização primário do recurso, especificando o mecanismo de acesso (como o esquema `http`) e sua localização na rede.

E) Têm como única função definir o tipo MIME do conteúdo que será retornado no corpo da resposta HTTP.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 30

A especificação do HTTP detalha a estrutura das mensagens trocadas entre clientes e servidores. Conforme a RFC 9110 (Seção 5), os campos de cabeçalho (*Fields*) servem para:

A) Armazenar exclusivamente a carga útil (*payload*) de dados codificados em formato JSON ou XML.

B) Substituir a linha de requisição (*request line*) quando a mensagem for transmitida via conexões seguras HTTPS.

C) Criptografar automaticamente o corpo da requisição utilizando chaves de sessão simétricas.

D) Definir os nomes de tabelas e colunas que devem ser consultados no banco de dados relacional subjacente.

E) Transmitir metadados sobre a mensagem, o recurso de origem ou as preferências de comunicação entre as partes.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 31

O estilo arquitetural REST (*Representational State Transfer*) fundamenta-se em um conjunto de restrições para a criação de serviços web flexíveis e escaláveis. Uma das restrições centrais da arquitetura REST é:

A) A obrigatoriedade do uso de tabelas de banco de dados estritamente relacionais para manter a consistência ACID.

B) A exigência de manter uma conexão TCP persistente em aberto durante todo o ciclo de vida do cliente.

C) A interface uniforme, que simplifica e desacopla a arquitetura permitindo que cada parte evolua independentemente.

D) A proibição absoluta de utilizar mecanismos de cache em qualquer camada intermediária da rede.

E) A necessidade de compilar os contratos de interface em arquivos de definição binários do tipo WSDL antes da execução.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 32

A abordagem RPC (*Remote Procedure Call*) é um paradigma de comunicação cliente-servidor utilizado na construção de APIs. A principal ideia conceitual por trás do modelo RPC é:

A) Tratar todos os pontos de extremidade como coleções de recursos manipulados via verbos padronizados.

B) Fazer com que a chamada a um serviço remoto pareça, para o programador, a invocação de uma função ou procedimento local.

C) Enviar dados do servidor para o cliente de forma contínua através de um canal totalmente assíncrono via eventos.

D) Permitir que o cliente defina dinamicamente no formato da requisição a estrutura exata do JSON que deseja receber na resposta.

E) Utilizar o navegador como um nó intermediário que processa e valida a lógica de negócios antes do envio ao servidor.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 33

Em arquiteturas orientadas a eventos e integração de sistemas web, o mecanismo de WebHooks é amplamente utilizado. A forma básica de funcionamento de um Webhook consiste em:

A) O servidor do provedor realizar uma requisição HTTP POST para uma URL pré-configurada no sistema do cliente sempre que um evento de interesse ocorrer.

B) O cliente estabelecer um \textit{polling} contínuo no servidor por meio de requisições GET a cada segundo.

C) A abertura de uma tomada (\textit{socket}) bidirecional full-duplex sobre um único canal TCP duradouro.

D) O envio de mensagens via protocolo SMTP para a caixa de correio do administrador do sistema consumidor.

E) A execução de chamadas procedurais remotas codificadas estritamente em binário nativo de máquina.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 34

O protocolo WebSockets estabelece um padrão moderno para comunicação em tempo real na web. Ao contrário do padrão HTTP de requisição e resposta isoladas, o WebSocket oferece:

A) Uma comunicação bidirecional e *full-duplex* através de uma única conexão TCP mantida por longo período após um *handshake* inicial.

B) Um canal de comunicação unidirecional estrito, onde apenas o servidor pode iniciar o envio de quadros de dados.

C) A obrigatoriedade de reenviar os cabeçalhos HTTP completos a cada mensagem trocada entre cliente e servidor.

D) O encerramento automático da conexão TCP logo após a entrega do primeiro quadro de dados no cliente.

E) Uma camada que dispensa o uso do protocolo IP para o transporte das mensagens pela rede mundial de computadores.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 35

No paradigma de APIs GraphQL, a abordagem de consulta difere substancialmente das APIs REST tradicionais. Qual é a principal característica operacional de uma consulta GraphQL?

A) Cada tipo de dado exige um \textit{endpoint} URL dedicado e exclusivo no servidor para ser retornado.

B) O servidor retorna sempre o documento inteiro do banco de dados, cabendo ao cliente filtrar os campos necessários localmente.

C) O cliente envia uma instrução especificando exatamente quais campos e dados correlacionados necessita, recebendo uma resposta estruturada de forma correspondente.

D) As mensagens de consulta devem ser obrigatoriamente formatadas em XML e validadas por um esquema XSD.

E) A comunicação limita-se a métodos HTTP PUT para atualizar o estado interno do grafo de dados.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 36

Considere o problema do dimensionamento e escalabilidade horizontal de uma fazenda de servidores (*server farm*) de aplicação web. Ao comparar o uso de sessões *stateful* em memória com a adoção de um modelo *stateless*, qual é o impacto direto da arquitetura na camada de balanceamento de carga (*Load Balancer*)?

A) A arquitetura *stateful* exige o uso de técnicas como *sticky sessions* (afinidade de sessão) ou sincronização de memória entre nós, dificultando a distribuição uniforme do tráfego e a remoção transparente de nós com falhas.
    
B) A arquitetura *stateless* invalida o uso de qualquer tipo de balanceador de carga, obrigando o cliente a implementar algoritmos de *Round-Robin* diretamente no seu código.

C) A arquitetura *stateful* garante que qualquer nó da fazenda de servidores possa responder a qualquer requisição sem necessidade de consultar recursos externos ou manter contexto prévio.

D) A arquitetura *stateless* torna imutáveis os registros de banco de dados, impedindo operações de gravação (operações de escrita) no sistema.

E) Ambas as abordagens possuem exatamente o mesmo impacto na camada de balanceamento, sendo indiferente para a infraestrutura o local onde o estado da aplicação reside.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 37

Análise as seguintes afirmativas sobre a evolução da arquitetura de 3 camadas (*3-tier*) para arquiteturas *n-tier* (múltiplas camadas) em ambientes de microsserviços modernos:

**I.**  A inclusão de camadas adicionais, como *API Gateways*, caches distribuídos (ex: Redis) e filas de mensageria (ex: RabbitMQ), caracteriza a transição para um modelo *n-tier*.
    
**II.** Adicionar mais camadas em uma arquitetura *n-tier* reduz linearmente a latência de rede total de cada transação, tornando a resposta sempre mais rápida do que em sistemas *1-tier*.

**III.** A arquitetura *n-tier* permite o desacoplamento e a implantação independente de componentes, permitindo que diferentes sub-sistemas sejam escalados isoladamente conforme a demanda.

Está(ão) correta(s) apenas a(s) afirmativa(s):

A) I.

B) II.

C) I e III.

D) II e III.

E) I, II e III.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 38

A RFC 9110 (Seção 9.2.2) trata do conceito de **Idempotência** dos métodos HTTP. Um método é considerado idempotente quando os efeitos colaterais no servidor provocados por múltiplas requisições idênticas são os mesmos que os de uma única requisição. Com base nessa definição, analise os métodos HTTP e assinale a alternativa correta:

A) O método `POST` é idempotente, pois reenviar o mesmo formulário dez vezes garante que apenas um registro será inserido no banco de dados.

B) Os métodos `GET`, `HEAD`, `PUT` e `DELETE` são idempotentes pela especificação.

C) Nenhum método que altere dados no servidor pode ser classificado como idempotente.

D) O método `PATCH` é nativamente garantido como idempotente pela RFC 9110, independentemente da implementação da sua carga útil.

E) A idempotência refere-se unicamente ao tamanho em bytes do corpo da resposta retornado pelo servidor, que deve permanecer inalterado.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 39

Na Seção 8 da RFC 9110, descreve-se o mecanismo de **Negociação de Conteúdo** (*Content Negotiation*). Suponha que um cliente HTTP deseje receber a resposta preferencialmente em formato JSON, mas aceite XML caso o primeiro não esteja disponível. Qual par de cabeçalhos de requisição e resposta é utilizado para realizar essa negociação proativa?

A) Requisição: `Content-Type: application/json` | Resposta: `Accept: text/xml`.

B) Requisição: `User-Agent: JSON-Client` | Resposta: `Server: Apache-XML`.

C) Requisição: `Accept: application/json, text/xml;q=0.8` | Resposta: `Content-Type: application/json`.

D) Requisição: `Host: api.exemplo.com` | Resposta: `Location: /v1/json`.

E) Requisição: `Transfer-Encoding: chunked` | Resposta: `Content-Encoding: gzip`.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 40

A manipulação de estado e o desacoplamento são determinantes no projeto de Request-Response APIs. Ao comparar as abordagens REST e GraphQL em relação ao problema de transmissão excessiva de dados (*Over-fetching*) ou escassez de dados (*Under-fetching*), é correto afirmar que:

A) REST resolve completamente o *over-fetching* ao forçar a criação de um único *endpoint* genérico para toda a aplicação.

B) GraphQL mitiga o *over-fetching* e o *under-fetching* ao permitir que a requisição especifique de maneira declarativa a estrutura exata dos campos necessários na resposta.

C) O problema de *under-fetching* ocorre em GraphQL quando o esquema inclui tipos de dados aninhados ou conexões em grafo.

D) Tanto REST quanto GraphQL sofrem identicamente dos mesmos problemas de otimização de payload, sem diferenças arquiteturais relevantes.

E) O *over-fetching* é uma funcionalidade desejável do REST criada para pré-carregar o armazenamento em cache do navegador com dados irrelevantes.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 41

No ecossistema de APIs baseadas em RPC, o protocolo gRPC ganhou ampla adoção em arquiteturas de microsserviços. O gRPC diferencia-se de abordagens REST/JSON tradicionais principalmente por utilizar:

A) O formato de serialização binário *Protocol Buffers* (Protobuf) executado nativamente sobre o protocolo HTTP/2.

B) O formato textual XML para transporte de dados sobre o protocolo HTTP/1.0.

C) Exclusivamente conexões baseadas no protocolo UDP para garantir que nenhuma mensagem seja retransmitteda.

D) Consultas escritas em sintaxe SQL pura enviadas no corpo do cabeçalho da mensagem HTTP.

E) Documentos HTML renderizados no lado do servidor com scripts de validação incorporados.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 42

Considere uma aplicação de negociação de ativos financeiros em tempo real que exige o envio constante de atualizações de cotações do servidor para milhares de navegadores web conectados, com baixa latência e sobrecarga de rede reduzida. Avaliando as tecnologias de Event-Driven APIs, a solução mais adequada e eficiente para este cenário é:

A) WebHooks, pois o navegador cliente pode abrir uma porta estática e expor uma URL pública para receber requisições POST do servidor.

B) *Polling* HTTP tradicional usando o método `POST` com intervalos de 10 milissegundos.

C) WebSockets, que mantêm um canal bidirecional full-duplex de baixo \textit{overhead} através de uma única conexão TCP persistente.

D) Chamadas RPC baseadas em arquivos XML trafegados por e-mail de segundo em segundo.

E) Requisições HTTP \texttt{HEAD} para verificar se o tamanho do arquivo do banco de dados mudou.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 43

A RFC 9110 (Seção 7) conceitua o comportamento de **Gateways** e **Proxies**. Qual é a diferença fundamental no papel desempenhado por um *Forward Proxy* em comparação a um *Gateway* (ou *Reverse Proxy*) no fluxo de mensagens HTTP?

A) O *Forward Proxy* atua como representante do cliente, interceptando requisições genéricas enviadas para qualquer servidor na internet; o *Gateway* atua como representante do servidor de origem de destino.

B) O *Forward Proxy* processa apenas conexões criptografadas HTTPS, enquanto o \textit{Gateway} só é capaz de manipular tráfego de texto puro HTTP.

C) O *Gateway* reside obrigatoriamente na mesma máquina do navegador do usuário cliente, enquanto o *Forward Proxy* fica no banco de dados.

D) Não há qualquer diferença funcional ou conceitual; a RFC 9110 utiliza ambos os termos como sinônimos perfeitos.

E) O *Forward Proxy* altera dinamicamente os códigos de status de resposta HTTP de 200 para 500 para forçar tentativas de reconexão.

<details>
    <summary><b>Resposta:</b></summary>
    A
</details>

## 44

Em uma aplicação web corporativa, a autenticação baseada em Tokens JWT (*JSON Web Tokens*) é amplamente utilizada para substituir o gerenciamento tradicional de sessões baseadas em memória no servidor (*Server-side Session State*). Qual das seguintes afirmações justifica essa escolha sob a perspectiva da arquitetura de software?

A) O JWT elimina a necessidade do uso de criptografia TLS na camada de transporte da rede.

B) O uso de JWT força a aplicação a executar toda a sua lógica de banco de dados diretamente dentro do navegador do cliente.

C) O uso de JWT impede que o cliente armazene qualquer tipo de dado no armazenamento local (*localStorage*) ou em cookies.

D) O token JWT expande o tamanho de todas as respostas do servidor em pelo menos 50 MB, forçando o uso de streaming HTTP.

E) O JWT permite transformar a camada de aplicação em *stateless*, pois as credenciais e declarações (*claims*) do usuário trafegam assinadas em cada requisição, dispensando consulta do estado da sessão em memória local do servidor.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 45

Sobre a semântica e utilização do método HTTP `PATCH` (definido pela RFC 5789 e incorporado às práticas do ecossistema referente à RFC 9110), assinale a opção correta:

A) O método `PATCH` exige a substituição completa de todas as propriedades do recurso, comportando-se exatamente como o `PUT`.

B) Operações executadas via `PATCH` são obrigatoriamente convertidas em comandos de remoção `DELETE` pelo servidor web.

C) O método `PATCH` é classificado rigorosamente pela RFC 9110 como um método seguro (*safe method*).

D) O uso do `PATCH` é estritamente proibido em arquiteturas RESTful por não possuir suporte em navegadores web.

E) O método `PATCH` aplica modificações parciais a um recurso existente, contendo um documento de instrução de alteração no seu corpo.

<details>
    <summary><b>Resposta:</b></summary>
    E
</details>

## 46

Em sistemas distribuídos de altíssimo desempenho, o dilema da manutenção de estado em arquiteturas de microsserviços impacta diretamente os teoremas de consistência (como o Teorema CAP). Considere um cenário em que uma aplicação de e-commerce transacional abandona o modelo de estado em sessão local (*Stateful App Server*) e migra para um modelo *Stateless App Server* suportado por um cluster de cache em memória (*Distributed Shared Cache*) e banco de dados relacional distribuído. 

Sob a ótica do isolamento de estado e falhas de rede, analise as implicações desse design e assinale a alternativa correta:


A) A migração para servidores de aplicação *stateless* transforma a aplicação em um sistema à prova de partições de rede (*Partition Tolerance* absoluta), pois os servidores deixam de utilizar placas de rede para se comunicar.

B) O desacoplamento do estado dos nós de aplicação facilita a escalabilidade horizontal irrestrita desses nós, porém transfere o ponto focal de concorrência, latência e consistência de estado para a camada de cache distribuído e persistência.

C) A utilização de aplicações *stateless* elimina a necessidade de transações atômicas (ACID) no banco de dados, visto que o estado passa a ser mantido diretamente no navegador do cliente através de cookies criptografados.

D) O balanceador de carga passa a ter a obrigação de ler o estado interno da memória RAM de cada nó antes de redirecionar um pacote TCP, aumentando significativamente a sobrecarga de CPU do balanceador.

E) A arquitetura *stateless* força a eliminação do protocolo TCP, exigindo a adoção de protocolos não conexos de camada física para evitar o armazenamento de tabelas de rotas nos roteadores.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 47

Considere a RFC 9110 no que tange às seções 5 (*Fields*) e 8 (*Representation Data and Metadata*) e o tratamento de solicitações condicionais com controle de concorrência otimista (*Optimistic Concurrency Control*). Uma aplicação cliente precisa atualizar o recurso `/produtos/42` que possui o valor de `ETag` atual igual a `"v3-a8f9"`. Para evitar o problema da "atualização perdida" (*lost update problem*), em que dois clientes alteram o mesmo objeto simultaneamente provocando a sobresscrita descontrolada de dados, qual fluxo estritamente normatizado pela RFC 9110 deve ser adotado?

A) O cliente deve enviar uma requisição `GET /produtos/42` com o cabeçalho `If-Match: "v3-a8f9"` e aguardar o servidor travar o banco de dados em modo exclusivo.

B) O cliente deve utilizar o cabeçalho `If-None-Match: *` acompanhado de um método `POST`, o que força o servidor a mesclar os arquivos automaticamente utilizando o algoritmo Git.

C) O cliente deve emitir um comando `DELETE` antes da atualização, garantindo que o recurso seja destruído e recriado com uma nova chave primária sem interferência de terceiros.

D) O cliente deve enviar uma requisição `PUT` ou `PATCH` contendo o cabeçalho `If-Match: "v3-a8f9"`; se outro cliente alterou o recurso entrementes (mudando a `ETag`), o servidor rejeitará a operação com o código de status `412 Precondition Failed`.

E) A RFC 9110 proíbe o uso de cabeçalhos condicionais em métodos de modificação de estado, delegando o controle de concorrência à camada de transporte TLS.

<details>
    <summary><b>Resposta:</b></summary>
    D
</details>

## 48

Considere a especificação do GraphQL em relação à execução de consultas complexas sobre grafos de dados e compare-a com o comportamento de APIs RESTful sob o prisma da segurança e do consumo de recursos no servidor de origem. 

Analise a seguinte vulnerabilidade/desafio arquitetural associado nativamente às APIs GraphQL:

A) O GraphQL impede o uso de autenticação via tokens JWT, forçando o envio de senhas em texto puro dentro das instruções de consulta.

B) Devido à natureza declarativa e flexível das consultas, clientes maliciosos podem construir consultas aninhadas circularmente com profundidade arbitrária (ex: \textit{author $\rightarrow$ books $\rightarrow$ author $\rightarrow$ books}), provocando negação de serviço (*DoS*) por exaustão de CPU/memória no servidor.

C) O motor do GraphQL substitui os interpretadores de código da aplicação e executa comandos de sistema diretamente no shell do SO do servidor de banco de dados.

D)  A arquitetura GraphQL elimina o suporte a conexões cifradas via HTTPS, expondo todas as requisições à interceptação em trânsito.

E) GraphQL obriga o servidor a manter conexões de Soquetes de Camada 2 abertas com todos os clientes da internet simultaneamente.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>

## 49

A RFC 9110 (Seção 7 - Routing HTTP Messages) detalha as responsabilidades e transformações permitidas por intermediários (proxies, gateways e caches) na mensagem HTTP. Suponha um cenário corporativo onde requisições trafegam por múltiplos proxies e gateways antes de atingirem o servidor de origem. Para preservar as informações originais do cliente (como o endereço IP de origem do cliente e o protocolo de conexão inicial), qual é o padrão recomendado e a prática associada aos cabeçalhos de roteamento?

A) Intermediários são estritamente proibidos de registrar ou repassar o endereço IP do cliente por violação arquitetural da RFC 9110.
    
B) O servidor de origem deve realizar um *ping* ICMP reverso para a porta 80 do cliente para descobrir seu endereço físico MAC.
    
C) Os intermediários devem injetar ou atualizar o cabeçalho padronizado `Forwarded` (ou os cabeçalhos não-padronizados legados do tipo `X-Forwarded-For` e `X-Forwarded-Proto`), permitindo ao servidor de origem rastrear a cadeia de saltos e a identidade do cliente inicial.

D) Toda a mensagem HTTP original é descartada pelo proxy e re-encapsulada em um pacote de transmissão de TV digital (ISDB-T).

E) O intermediário deve alterar o método HTTP de todas as requisições para `OPTIONS` e apagar todos os parâmetros da URI.

<details>
    <summary><b>Resposta:</b></summary>
    C
</details>

## 50

Uma arquitetura de Event-Driven APIs implementada sobre o protocolo HTTP utilizando **WebHooks** enfrenta desafios severos de confiabilidade, ordenação e idempotência quando comparada a sistemas de filas dedicados (como AMQP/RabbitMQ). 

Diante de uma falha temporária de rede na qual o receptor do Webhook fica indisponível, qual é o padrão de resiliência e design correto a ser implementado no lado do emissor do evento para garantir a entrega sem causar duplicação inconsistente de processamento no receptor?

A) O emissor deve descartar a mensagem imediatamente na primeira falha, garantindo que eventos antigos nunca sejam reprocessados.

B) O emissor deve implementar uma estratégia de retentativas com recuo exponencial (*exponential backoff*) e variação aleatória (*jitter*), enquanto o consumidor deve projetar o endpoint do Webhook para ser estritamente idempotente (utilizando um identificador único de evento para desduplicação).

C) O receptor deve manter uma conexão TCP ininterrupta com a placa de rede do emissor via cabo de par trançado dedicado.

D) O emissor deve alterar a requisição de `POST` para `DELETE` até que o servidor receptor retorne um código de erro 500.

E) A comunicação por Webhooks dispensa tratamento de erros, pois a RFC 9110 garante a entrega de pacotes HTTP sem perdas mesmo em redes desconectadas.

<details>
    <summary><b>Resposta:</b></summary>
    B
</details>