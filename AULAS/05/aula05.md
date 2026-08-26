# Aula 05

## [RFC 9110: STD 97: HTTP Semantics](https://www.rfc-editor.org/info/rfc9110):

TODO: Finalizar de montar o gráfico de roteamento, com detalhes

### 7. [Routing HTTP Messages](https://www.rfc-editor.org/info/rfc9110/#section-7)

A seção 7 trata de como uma mensagem de requisição é direcionada até o recurso-alvo e como a resposta correspondente retorna.

O roteamento de uma mensagem de requisição é determinada por cada cliente baseada em: determinação do recurso-alvo, configuração de proxy do cliente e estabelecimento ou reúso de uma conexão ***inbound***

1. Determinação do recurso-alvo: 
   1. Uma referência [URI](https://www.rfc-editor.org/info/rfc9110/#uri.references) é resolvida em sua forma absoluta para a obtenção do URI alvo.
   2. O cliente envia uma mensagem de requisição contendo componentes suficientes de URI para permitir ao recipiente identificar o mesmo recurso.
      - Esses componentes são enviados dentro dos dados de controle da mensagem, e do campo de cabeçalho `Host`.
      - Ao receber a requisição, o servidor reconstrói a URI a partir do componentes recebidos, e de acordo com sua configuração local e contexto de conexão de entrada. Essa reconstrução é específica para cada versão principal do protocolo. Por exemplo, para o HTTP 1.1, isso é definido na [seção 3.3](https://www.rfc-editor.org/info/rfc9112/#section-3.3).
      - O campo de cabeçalho `Host` fornece informações do *host* e da porta do URI, permitindo ao servidor fazer distinção entre os recursos enquanto atende às requisições para vários nomes de *host*.
      - No HTTP/2 e HTTP/3 o campo de cabeçalho `Host` algumas vezes é suplantado pelo campo de pseudo-cabeçalho `":authority"`.
      - Essa informação da autoridade é crítica para lidar com uma requisição. Um agente de usuário deve obrigatoriamente gerar um campo de cabeçalho `Host` em uma requisição, exceto quando enviar essa informação como um campo de pseudo-cabeçalho `":authority"`.
2. Configuração de proxy do cliente: uma vez que o URI-alvo e sua origem são determinados, um cliente decide se uma requisição de rede é necessária e, caso positivo, para onde a requisição deve ser direcionada
   1. Se o usuário possui um cache e a requisição pode ser satisfeita, então a requisição é direcionada para o cache primeiro.
   2. Caso a requisição não tenha sido satisfeita pelo cache, então o cliente verifica sua configuração para determinar se o proxy deve ser usado. 
     - A configuração do proxy é geralmente baseada na correspondência de prefixos de URI, na correspondência de autoridade seletiva ou em ambos, e o próprio proxy geralmente é identificado por um URI "http" ou "https".
     - Se um proxy "http" ou "https" é aplicável, o cliente realiza uma conexão ***inbound*** ao estabelecer (ou reutilizar) uma conexão com esse proxy e, então envia uma mensagem de requisição HTTP contendo o alvo da requisição que corresponde ao seu URI alvo.
3. Estabelecimento ou reúso de uma conexão ***inbound***
   1. Se não houver proxy aplicável, o clinte invocará um *handler routine* (específico ao esquema do URI alvo) para obter acesso ao recurso identificado. 
      - A [Seção 4.3.2](https://www.rfc-editor.org/info/rfc9110/#http.origin) define como obter acesso a um recurso "http" ao estabelecer (ou reutilizar) uma conexão ***inbound*** com o servidor de origem identificado e então enviá-lo uma mensagem de requisição contendo um alvo da requisição que corresponda ao URI de destino do cliente.
      - A [Seção 4.3.3](https://www.rfc-editor.org/info/rfc9110/#https.origin) define como obter acesso a um recurso "https" ao estabelecer (ou reutilizar) uma conexão ***inbound*** segura com o servidor de origem que seja autoritativo para a origem identificada e então enviá-lo uma mensagem de requisição HTTP contendo o alvo da requisição que corresponda ao URI de destino do cliente.

#### Rejeição de mensagens mal direcionadas

Assim que uma solicitação é recebida por um servidor e analisada o suficiente para determinar seu URI de destino, o servidor decide se:

- Processará a requisição; 
- Encaminhará a requisição para outro servidor; 
- Redirecionará o cliente a um recurso diferente;
- Responderá com um erro;
- Encerrará a conexão.

Essa decisão pode ser influenciada por qualquer fator relacionado à solicitação ou ao contexto da conexão, mas se concentra especificamente em verificar se o servidor foi configurado para processar solicitações para esse URI de destino e se o contexto da conexão é apropriado para essa solicitação. Por exemplo:

- Uma requisição foi má direcionada (deliberadamente, ou por acidente) de forma que o conteúdo do campo de cabeçalho `Host` difere do *host* ou da porta da conexão.
- Se a conexão for proveniente de um *gateway* confiável, essa inconsistência pode ser esperada; caso contrário, pode indicar uma tentativa de burlar os filtros de segurança, enganar o servidor para que entregue conteúdo não público ou corromper o cache.

Portanto, exceto se a conexão seja de um *gateway* confiável, um servidor de origem **deve obrigatoriamente** rejeitar uma requisição se qualquer exigência específica para o URI de destino não seja cumprida, preferencialmente com o status 421 (*Misdirected Request*).

#### Encaminhamento de mensagens

Intermediários devem encaminhar mensagens preservando a semântica, mesmo quando elementos do protocolo não são reconhecidos, para preservar a extensibilidade para demais recipientes. Se não estiver agindo como um ***tunnel***, precisa obrigatoriamente implementar o campo de cabeçalho `Connection`, excluir os campos que são usados apenas para as conexões de entrada (*hop-by-hop*), e registrar o caminho no campo de cabeçalho `Via`.

#### Transformações de mensagem

Transformações de mensagem (conversão de formato etc.) são permitidas sob condições restritas e devem ser sinalizadas (status 203).

O mecanismo `Upgrade` permite negociar mudança de protocolo na mesma conexão.

#### Atividade

- Estudar o papel dos intermediários na seção de arquitetura (Seção 3) e as regras de segurança relacionadas a request smuggling.
- **Responder:** por que um servidor de origem deve verificar a consistência entre Host/:authority e o contexto da conexão, e qual o risco de não fazê-lo?