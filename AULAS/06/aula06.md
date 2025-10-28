# Aula 06

## HTTP vs. HTTPS [^1]

[^1]: [Wikipedia - HTTPS](https://en.wikipedia.org/wiki/HTTPS).

### HTTP (*Hypertext Transfer Protocol*)

- RFCs
  - [1945 - HTTP/1.0](https://www.rfc-editor.org/rfc/rfc1945).
  - [9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html).
  - [9112 - HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112).
  - [9113 - HTTP/2](https://www.rfc-editor.org/rfc/rfc9113).
  - [9114 - HTTP/3](https://www.rfc-editor.org/rfc/rfc9114).
- **Porta padrão**: 80.
  
<!-- O HTTP consiste em uma **família** de **protocolos sem estado**, de **requisição/resposta**, e da **Camada de Aplicação**, que compartilham uma interface genérica, semântica extensível e mensagens auto-descritivas para permitir uma interação flexível com sistemas de informação com hipertexto e baseado na rede.

O HTTP oculta os detalhes de como um serviço é implementado ao apresentar uma interface uniforme a clientes, a qual é independente dos tipos de recurso providos. Da mesma forma, os servidores não precisam estar cientes do contexto do cliente: uma requisição pode ser considerada de forma isolada em vez de ser associada com um tipo específico de cliente ou uma sequência predeterminada de etapas de uma aplicação. Isso permite que implementações de propósito geral sejam usadas eficazmente em variados contextos, a complexidade de interação seja reduzida, e permite evolução indepentente ao logo do tempo.

O HTTP foi também planejado para ser usado como protocolo de intermediação, no qual proxies e gateways podem traduzir sistemas de informação além do HTTP em uma interface mais genérica.

Uma consequência dessa flexibilidade é que o protocolo não pode ser definido em termos de o que acontece atrás da interface. Em vez disso, sua conceituação é limitada em definição da sintaxe de comunicação, a intenção da comunicação recebida e o comportamente esperado dos recipientes. Se a comunicação é considerada de forma isolada, então ações bem sucedidas devem refletir-se em mudanças correspondentes na interface observável fornecida pelos servidores. Entretanto, uma vez que clientes podem agir em paralalo e, talvez, com propósitos opostos, não é possível exigir que tais mudanças sejam observáveis alpem do escopo de uma única resposta. -->

O HTTP é um protocolo da camada de aplicação do modelo TCP/IP (Internet) para sistemas de informação colaborativos, distribuídos e hipermídia.

Seu desenvolvimento foi iniciado por Tim Berners-Lee em 1989, no CERN, e resumido em um documento simples com a descrição de um cliente e um servidor usando a primeira versão, 0.9, do HTTP.

Em 1996 o HTTP/1 é finalizado e documentado, mas continha a desvantagem de necessitar de um conexão TCP separada para cada requisição de recurso. A nova versão, HTTP/1.1 permitiu o reuso de uma mesma conexão TCP para múltiplas requisições de recursos. Essa versão foi sendo atualizada ao longo do tempo.

Em 2015 foi apresentado o HTTP/2, uma revisão da versão anterior, com as seguintes diferenças:

- Representação binária e comprimida dos metadados (ou seja, do cabeçalho).
- Utilização de uma única conexão (normalmente criptografada) TCP por domínio de servidor, em vez de 2 a 8, como era antes.
- Uso de um ou mais fluxos bidirecionais por conexão TCP, no qual requisições e respostas HTTP são divididas e transmitidas em pacotes pequenos.
- Capacidade de aplicações no lado do servidor enviarem dados aos clientes sempre que novos dados estejam disponíveis, evitando forçar os clientes a requisitarem novos dados periodicamente.

Mais recentemente, em 2022, foi disponibilizado o HTTP/3, cuja principal diferença se dá no uso dos protocolos QUIC + UDP na camada de transporte, no lugar do TCP que é utilizado por padrão nas versões anteriores.

### HTTPS (*HTTP Secure*)

- RFCs
  - [2818 - HTTP Over TLS](https://datatracker.ietf.org/doc/html/rfc2818).
  - [9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html).
- **Porta padrão**: 443.

O HTTPS (*HTTP Secure*) é uma extensão do HTTP que fornece segurança na comunicação com o uso de criptografia através dos protocolos **SSL** (*Secure Sockets Layer*) ou **TLS** (*Transport Layer Security*).

Os principais motivos para o uso do HTTPS são a **autenticação do site acessado** e a **proteção da privacidade e integridade dos dados transmitidos**, enquanto estão em trânsito. A autenticação de um site/servidor requer um certificado digital de um terceiro confiável. De início, obter essa autenticação era uma operação cara e, por causa disso, somente sites que envolviam transações financeiras tinham conexões HTTPS. Hoje em dia é possível obter o certificado de forma gratuita (exemplo: [AWS Certificate Manager](https://aws.amazon.com/pt/certificate-manager/)).

## Certificados digitais [^2]

[^2]: [Wikipedia - TLS + SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) e [AWS - O que é um certificado SSL/TSL](https://aws.amazon.com/what-is/ssl-certificate/)?.

- RFCs
  - [6101 - Secure Sockets Layer (SSL) Protocol Version 3.0](https://datatracker.ietf.org/doc/rfc6101/).
  - [6176 - Prohibiting Secure Sockets Layer (SSL) Version 2.0](https://datatracker.ietf.org/doc/rfc6176/).
  - [7568 - Deprecating Secure Sockets Layer Version 3.0](https://datatracker.ietf.org/doc/rfc7568/).
  - [2246 - The TLS Protocol](https://datatracker.ietf.org/doc/html/rfc2246).
  - [4346 - The Transport Layer Security (TLS) Protocol Version 1.1](https://datatracker.ietf.org/doc/html/rfc4346).
  - [5246 - he Transport Layer Security (TLS) Protocol Version 1.2](https://datatracker.ietf.org/doc/html/rfc5246).
  - [8446 - The Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446).

Um **certificado SSL/TLS** é um **objeto digital** que permite que os sistemas verifiquem a identidade e, posteriormente, estabeleçam uma conexão de rede criptografada com outro sistema usando o protocolo *Secure Sockets Layer*/*Transport Layer Security* (SSL/TLS). 

Os certificados são usados em um sistema de criptografia conhecido como *Public Key Infrastructure* (**PKI** – Infraestrutura de chave pública). O sistema **PKI** permite que uma parte estabeleça a identidade de outra usando certificados, se ambas confiarem em um terceiro, conhecido como **autoridade de certificado**. Os certificados SSL/TLS atuam, portanto, como cartões de identidade digital para proteger as comunicações de rede e estabelecer a identidade de sites na Internet e de recursos em redes privadas.

As características de uma página da Web protegida por SSL/TLS são:

- Um prefixo **https** no endereço do site no navegador.
- Um ícone de cadeado e uma barra de endereço verde no navegador da Web.
  - É possível verificar se o certificado SSL/TLS é válido clicando e expandindo o ícone de cadeado na barra de endereço URL.

### Criptografia

A criptografia SSL/TLS possui duas chaves diferentes para criptografar e descriptografar uma mensagem: 

- **Chave pública**: é uma chave criptográfica que o servidor Web fornece ao navegador no certificado SSL/TLS. O navegador usa a chave para criptografar as informações antes de enviá-las ao servidor Web.
- **Chave privada**: Somente o servidor Web tem a chave privada. Um arquivo criptografado pela chave privada só pode ser descriptografado pela chave pública, e vice-versa. Se a chave pública puder descriptografar apenas o arquivo que foi criptografado pela chave privada, a capacidade de descriptografar esse arquivo garante que o destinatário e o remetente pretendidos sejam quem afirmam ser.

### Autenticação

O servidor envia a chave pública no certificado SSL/TLS ao navegador. O navegador verifica o certificado de um terceiro confiável. Consequentemente, ele consegue verificar se o servidor Web é quem afirma ser.

### Assinatura digital

A assinatura digital é um número exclusivo para cada certificado SSL/TLS. O destinatário gera uma nova assinatura digital e a compara à assinatura original para verificar se terceiros não adulteraram o certificado enquanto ele percorria a rede.

### Autoridades de certificação

A **autoridade de certificação** (**CA** - *Certificate authority*) é uma organização que vende certificados SSL/TLS para proprietários da Web, empresas de hospedagem na Web ou empresas. 

A CA valida os detalhes do domínio e do proprietário antes de emitir o certificado SSL/TLS. **Para ser uma CA**, a organização **deve atender** a: 

- Requisitos específicos definidos pelo sistema operacional, pelos navegadores ou pela empresa de dispositivos móveis; e
- Se inscrever para ser listada como uma autoridade de certificação raiz. 
 
Algumas autoridades (CAs), e como está no mercado ([levantamento feito pela w3techs](https://w3techs.com/technologies/overview/ssl_certificate)):

| Empresa | Uso | Market share |
|---------|-----|--------------|
| Let's Encrypt | 60,1% | 63,6% |
| GlobalSign | 22% | 23,3% |
| Sectigo | 6,3% | 6,7% |
| GoDaddy Group | 3,8% | 4% |
| DigiCert Group | 1,9% | 2% |
| Actalls | 0,6% | 0,7 % |
| Certum | 0,5 % | 0,6 % |
| Secom Trust | 0,3% | 0,3 % |
| SSL.com | 0,1% | 0,1% |

### Validade

Um certificado SSL/TLS tem um período de validade máximo de 13 meses, valor esse que foi sendo reduzido gradualmente ao longo dos anos para reduzir riscos de segurança.

Quando o certificado SSL/TLS expira, os visitantes da Web recebem um aviso no navegador informando que o site não é seguro.

### Informações incluídas em um certificado SSL/TLS

- Nome de domínio.
- Autoridade de certificação.
- Assinatura digital da autoridade de certificação.
- Data de emissão.
- Data de validade.
- Chave pública.
- Versão SSL/TLS.

TLS significa segurança da camada de transporte. É um sucessor e uma continuação do protocolo SSL/TLS versão 3.0. Existem apenas pequenas diferenças técnicas entre o SSL/TLS e o TLS. Como o SSL/TLS, o TLS fornece um canal de transmissão de dados criptografados entre um navegador e o servidor Web. Os certificados SSL/TLS modernos usam o protocolo TLS em vez de SSL/TLS, mas SSL/TLS continua sendo um acrônimo bastante usado pelos especialistas em segurança. Embora não seja exatamente o mesmo, os termos SSL e TLS são comumente usados para se referir à mesma coisa. Também podem se referir ao protocolo de criptografia criptográfica como SSL/TLS.

### Como funciona o certificado

Os navegadores usam o certificado SSL/TLS para iniciar uma conexão segura com o servidor Web por meio do handshake SSL/TLS. O handshake SSL/TLS faz parte da tecnologia de comunicação do protocolo seguro de transferência de hipertexto (HTTPS). É uma combinação de HTTP e SSL/TLS. O HTTP é um protocolo que os navegadores da Web usam para enviar informações em texto simples a um servidor Web. O HTTP transmite dados não criptografados, ou seja, as informações enviadas de um navegador podem ser interceptadas e lidas por terceiros. Os navegadores usam HTTP com SSL/TLS ou HTTPS para proporcionar uma comunicação totalmente segura.

#### *Handshake*

1. O navegador abre um site seguro por SSL/TLS e se conecta ao servidor da web.
2. O navegador tenta verificar a autenticidade do servidor web solicitando informações identificáveis. 
3. O servidor Web envia o certificado SSL/TLS que contém uma chave pública como resposta.
4. O navegador verifica o certificado SSL/TLS, garantindo que ele seja válido e corresponda ao domínio do site. Quando o navegador estiver satisfeito com o certificado SSL/TLS, ele usará a chave pública para criptografar e enviar uma mensagem que contenha uma chave de sessão secreta.
5. O servidor web usa sua chave privada para descriptografar a mensagem e recuperar a chave de sessão. Em seguida, ele usa a chave de sessão para criptografar e enviar uma mensagem de confirmação para o navegador.
6. Agora, o navegador e o servidor da Web mudam para usar a mesma chave de sessão para trocar mensagens com segurança. 

#### Chave de sessão

Uma chave de sessão mantém a comunicação criptografada entre o navegador e o servidor Web após a conclusão da autenticação SSL/TLS inicial. A chave de sessão é uma chave de cifra para criptografia simétrica. A criptografia simétrica usa a mesma chave para criptografia e descriptografia. A criptografia assimétrica ocupa imenso poder de computação. Portanto, o servidor web alterna para criptografia simétrica que requer menos cálculos para manter uma conexão SSL/TLS.

### Tipos de certificados SSL/TLS

Os certificados SSL/TLS diferem conforme a validação e o domínio. Certificados com diferentes níveis de validação são classificados como:

- Certificados de validação estendida
- Certificados validados pela organização
- Certificados validados por domínio

Os certificados SSL/TLS compatíveis com diferentes tipos de domínio são:

- Certificado de domínio único
- Certificado curinga
- Certificado de vários domínios

#### Certificados de validação estendida

O certificado de validação estendida (EV SSL/TLS) é um certificado digital que tem o mais alto nível de criptografia, validação e confiança. Ao solicitar um EV SSL/TLS, uma organização ou proprietário da Web é submetido a verificações rigorosas feitas por autoridades de certificação. Isso inclui a verificação do endereço comercial físico, o pedido de certificado adequado e os direitos exclusivos de uso do domínio.

As empresas usam o EV SSL/TLS para proteger os usuários contra terceiros não autorizados. Isso é importante quando a empresa processa dados confidenciais no site, como transações financeiras e prontuários médicos. Um certificado EV SSL/TLS contém detalhes da organização comercial, que podem ser visualizados em um navegador.

#### Certificados de validação da organização

Os certificados de validação da organização (OV SSL/TLS) são inferiores aos EV SSL/TLS em termos de validação e confiança. Como os EV SSL/TLSs, as empresas devem passar por um processo de verificação ao solicitar o OV SSL/TLS. Embora o processo de verificação seja menos rigoroso, os candidatos devem provar a propriedade do domínio às autoridades de certificação.

O certificado OV SSL/TLS contém informações comerciais validadas e pode ser inspecionado no navegador. Empresas comerciais e com atendimento direto ao público usam o certificado OV SSL/TLS para criar confiança entre os clientes. O OV SSL/TLS fornece criptografia robusta para proteger a privacidade dos clientes durante a navegação na Web.

#### Certificados de validação de domínio

Os certificados de validação de domínio (DV SSL/TLS) são certificados digitais que têm a validação mais baixa. Solicitá-los também custa menos. Diferentemente dos EV SLLs e dos OV SSL/TLSs, os solicitantes de certificados DV passam por um processo de verificação menos rigoroso. O solicitante comprova a propriedade do domínio respondendo a um e-mail de verificação ou telefonema.

Um certificado DV não contém informações completas da organização ou empresa do solicitante. Portanto, não oferece total garantia aos usuários. Os certificados DV são adequados para sites informativos, como blogs. Não são ideais para gateways de pagamento, empresas de assistência médica ou outros sites que lidam com dados sigilosos.

#### Certificados SSL/TLS de domínio único

O certificado SSL/TLS de domínio único é um certificado SSL/TLS que protege apenas um domínio ou subdomínio. Um domínio é a URL ou endereço principal de um site, como amazon.com. Um subdomínio é um endereço da Web com uma extensão de texto que precede o domínio principal, como aws.amazon.com.

Por exemplo, você pode usar um certificado SSL/TLS de domínio único em http://exemplo.com. No entanto, não é possível usar o certificado para http://exemplo.com e sub.example.com simultaneamente.

#### Certificados SSL/TLS curinga

O certificado SSL/TLS curinga é um certificado SSL/TLS que protege um domínio e todos os seus subdomínios. Por exemplo, você pode usar um certificado SSL/TLS curinga para proteger http://exemplo.com, blog.exemplo.com e shop.exemplo.com.

#### Certificados SSL/TLS de vários domínios

Os certificados de vários domínios também são conhecidos como certificados de comunicações unificadas. Um certificado SSL/TLS de vários domínios oferece proteção SSL/TLS para vários nomes de domínio hospedados no mesmo servidor ou em servidores diferentes com a mesma propriedade. Por exemplo, você compra um certificado de vários domínios para http://example1.com, domain2.co.uk,shop.business3.com e chat.message.au.

### Acrescentando ao projeto

Em uma pesquisa rápida no Google, são sugeridas [3 formas](https://www.google.com/search?q=how+to+use+ssl%2Ftls+encryption+for+a+college+work&client=ubuntu-sn&hs=fZL&sca_esv=f0ead55d09cdc2fd&channel=fs&sxsrf=AE3TifOIPhAo0XWxdWa8F8tasc1elH6luA%3A1761228664696&ei=eDf6aPOhKsbx1sQP-IDloA0&ved=0ahUKEwjzvbWHwLqQAxXGuJUCHXhAGdQQ4dUDCBA&uact=5&oq=how+to+use+ssl%2Ftls+encryption+for+a+college+work&gs_lp=Egxnd3Mtd2l6LXNlcnAiMGhvdyB0byB1c2Ugc3NsL3RscyBlbmNyeXB0aW9uIGZvciBhIGNvbGxlZ2Ugd29yazIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAFIoIoBULUKWPRYcAF4AZABAZgBxgOgAY0hqgEKMC4xMC43LjEuMbgBA8gBAPgBAZgCE6AC3R_CAgoQABiwAxjWBBhHwgIHEAAYgAQYE8ICCBAAGBMYFhgewgIIEAAYgAQYogTCAgUQABjvBcICBhAAGBYYHsICCBAAGBYYChgemAMAiAYBkAYIkgcKMS4xMC41LjIuMaAH81myBwowLjEwLjUuMi4xuAfXH8IHBjAuMTIuN8gHNg&sclient=gws-wiz-serp) de utilizar a criptografia SSL/TLS no projeto da disciplina.