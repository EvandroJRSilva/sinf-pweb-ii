# Programação para a Web II

Repositório para os materiais da disciplina P. Web II.

| Código | Período | Créditos teóricos | Créditos práticos | Carga horária |
|--------|---------|-------------------|-------------------|---------------|
| SINF/CSHNB032 | 5 | 2 | 2 | 60 |

## Ementa

- Comunicação entre navegador e servidor: Assíncrona e Síncrona.
- Segurança.
- Frameworks e ferramentas de desenvolvimento de aplicações web.
- Controle de sessão.
- Esquema de funcionamento de uma página web com acesso a banco de dados.

## Bibliografia

### Básica

#### PPC

- DEITEL, H. M; DEITEL, P. J; et al. **Java TM: como programar**. 8 ed. São Paulo: Pearson, 2010.
- HORTMAN, C. S.; CORNELL, G. **Core Java: Volume 1**. 8 ed. São Paulo: Pearson, 2010.
- HORTMAN, C. S.; CORNELL, G. **Core Java: Volume 2**. 8 ed. São Paulo: Pearson, 2010.

#### Atualizada

- CONNOLLY, Randy; HOAR, Ricardo. **Fundamentals of Web Development**. 3.ed. [S.l.]: Pearson: 2022.
- KLEPPMANN, Martin. **Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintanable Systems**. 1.ed. Sebastopol, CA: O'Reilly Media, 2017.
- JIN, Brenda; SAHNI, Saurabh; SHEVAT, Amir. **Designing Web APIs - Building APIs that Developers Love**. 1.ed. Sebastopol, CA: O'Reilly Media, 2018.
- EJSMONT, Artur. **Web Scalability for Startup Engineers - Tips & Techniques for Scaling Your Web Application**. 1. ed. [S.l.]: McGraw-Hill Education, 2015.
- FIELDING, Roy T.; NOTTINGHAM, Mark; RESCHEKE, Julian. **RFC 9110: STD 97: HTTP Semantics**. IETF, 2022. Disponível em: [https://www.rfc-editor.org/info/rfc9110/](https://www.rfc-editor.org/info/rfc9110/). Acesso em: 03 ago. 2026.
- FIELDING, Roy T.; NOTTINGHAM, Mark; RESCHEKE, Julian. **RFC 9111: STD 98: HTTP Caching**. IETF, 2022. Disponível em: [https://www.rfc-editor.org/info/rfc9111/](https://www.rfc-editor.org/info/rfc9111/). Acesso em: 03 ago. 2026.
- BERNERS-LEE, Tim; FIELDING, Roy T.; MASINTER, Larry M. **RFC 3986: STD 66: Uniform Resource Identifier (URI): Generic Syntax**. IETF, 2005. Disponível em: [https://www.rfc-editor.org/info/rfc3986/](https://www.rfc-editor.org/info/rfc3986/). Acesso em: 03 ago. 2026.


### Complementar

#### PPC

- CRANE, D.; PASCARELLO, E.; DARREN, J. **Ajax em Ação**. 1 ed. São Paulo: Pearson, 2007.
- BURKE, B.; MONSON, R. **Enterprise JavaBeans 3.0**. 5 ed. São Paulo: Pearson, 2007.
- JENDROCK, E.; GOLLAPUDI, H.; SRIVATHSA. **JAVA EE 6 Tutorial: The Basic Concepts**. 4 ed. São Paulo: Pearson, 2011.
- FELKE-MORRIS, T. **Basic of Web HTML5 Design & CSS3**. São Paulo: Prentice-hall, 2012.
- GRAHAM, S. **Building WebService with Java**. 2 ed. Pearson, 2005.

#### Atualizada

- FIELDING, Roy T.; NOTTINGHAM, Mark; RESCHEKE, Julian. **RFC 9112: STD 99: HTTP/1.1**. IETF, 2022. Disponível em: [https://www.rfc-editor.org/info/rfc9112/](https://www.rfc-editor.org/info/rfc9112/). Acesso em: 03 ago. 2026.
- THOMSON, Martin; BENFIELD, Cory. **RFC 9113: HTTP/2**. IETF, 2022. Disponível em: [https://www.rfc-editor.org/info/rfc9113/](https://www.rfc-editor.org/info/rfc9113/). Acesso em: 03 ago. 2026.
- BISHOP, Mike. **RFC 9114: HTTP/3**. IETF, 2022. Disponível em: [https://www.rfc-editor.org/info/rfc9114/](https://www.rfc-editor.org/info/rfc9114/). Acesso em: 03 ago. 2026.
- **OWASP Application Security Verification Standard (ASVS)**. Disponível em [https://owasp.org/www-project-application-security-verification-standard/](https://owasp.org/www-project-application-security-verification-standard/). Acesso em 21 ago. 2025.
- ROADMAP.SH. **Backend Developer**. Developer Roadmaps, 2026. Disponível em: https://roadmap.sh/backend. Acesso em: 07 fev. 2026.
- **SQL Tutorial**. Disponível em [https://www.sqltutorial.org/](https://www.sqltutorial.org/). Acesso em 21 ago. 2025.
- HAVERBEKE, Marijn. **Eloquent JavaScript**. 4 ed. No starch press. Disponível em [https://eloquentjavascript.net/](https://eloquentjavascript.net/). Acesso em 21 ago. 2025.
- PILGRIM, Mark. **Dive into HTML5 with illustrations from the public domain**. Disponível em [https://mislav.github.io/diveintohtml5/](https://mislav.github.io/diveintohtml5/) (HTML, contéudo em Inglês), ou [https://www.jesusda.com/docs/ebooks/ebook_manual_en_dive-into-html5.pdf](https://www.jesusda.com/docs/ebooks/ebook_manual_en_dive-into-html5.pdf) (PDF), ou [https://github.com/zenorocha/diveintohtml5](https://github.com/zenorocha/diveintohtml5) (conteúdo traduzido). Acesso a todas as páginas citadas em 20 ago. 2025.
- GRINBERG, Miguel. **Flask Web Development: Developing Web Applications with Python**. 2 ed. O'Reilly Media, 2018.
- **Mozilla Developer Network (MDN Web Docs)**. Disponível em [https://developer.mozilla.org/pt-BR/](https://developer.mozilla.org/pt-BR/). Acesso em 21 ago. 2025.

## Conteúdo Programático

### Unidade 1 - Fundamentos da Comunicação Web e o Papel do Backend

- O que é Backend e seu lugar no ecossistema web
  - Frontend × Backend × Full-stack
  - Responsabilidades do lado servidor
  - Evolução histórica resumida da web e do servidor
- Arquitetura Cliente-Servidor
  - Modelo clássico e suas variações
  - Papéis, responsabilidades e fluxo de comunicação
  - *Stateless* vs *Stateful* (introdução)
- Protocolo HTTP em profundidade
  - Estrutura de uma mensagem HTTP
  - Métodos (GET, POST, PUT, PATCH, DELETE, etc.) e sua semântica
  - Códigos de status e categorias
  - Headers importantes
  - Corpo da mensagem e tipos de conteúdo
  - HTTP/1.1, HTTP/2 e HTTP/3 (visão conceitual de diferenças)
- Ciclo de vida de uma requisição HTTP
  - Do navegador/cliente até o servidor e de volta
  - Resolução de DNS, conexão, processamento e resposta
  - Papel dos proxies e intermediários
- Recursos, URIs e identificação
  - URI, URL e URN
  - Identificação de recursos
  - Conceito de hipermídia (HATEOAS em nível introdutório)
- Introdução a APIs e Serviços Web
  - O que é uma API e por que existe
  - APIs como contrato
  - Diferença entre API e aplicação web tradicional
- Princípios REST
  - Recursos, verbos e representações
  - Características principais do estilo REST
  - Quando REST faz sentido (e quando não)

### Unidade 2 - Processamento no Servidor, Estado e Segurança Básica

- Processamento de requisições no servidor
  - Conceito de handler / controller / endpoint
  - Roteamento (mapeamento de URL + método → lógica)
- *Pipeline* de processamento e *middlewares* 
  - Fluxo de passagem da requisição
  - Pontos de interceptação (autenticação, logging, validação etc.)
- Gerenciamento de Estado
  - Por que a web é naturalmente stateless
  - Cookies, sessões e tokens (conceitos e trade-offs)
  - Quando manter estado e quando evitar
- Autenticação e Autorização (fundamentos)
  - Diferença clara entre os dois conceitos
  - Modelos básicos (sessão, token, basic)
  - Princípios de identidade e controle de acesso
- Validação e sanitização de entradas
  - Por que validar no backend é obrigatório
  - Tipos de validação (sintática, semântica, de negócio)
  - Conceito de confiança zero nas entradas do cliente
- Tratamento de erros e design de respostas
  - Erros esperados vs inesperados
  - Códigos de status adequados
  - Mensagens de erro úteis e seguras
- Persistência de dados
  - Por que o backend precisa persistir dados
  - Tipos gerais de armazenamento (relacional, documento, chave-valor — apenas conceitos)
  - Separação entre lógica de negócio e armazenamento
- Logging, auditoria e observabilidade básica
  - O que registrar e por quê
  - Níveis de log
  - Conceitos iniciais de rastreabilidade de requisições

### Unidade 3 - Design de Sistemas Backend, Escalabilidade e Boas Práticas

- Design de APIs — boas práticas
  - Recursos bem modelados
  - Versionamento
  - Paginação, filtros e ordenação (conceitos)
  - Documentação como contrato
- Segurança no Backend
  - Principais categorias de riscos (baseado no pensamento do OWASP Top 10, sem aprofundar exploits)
  - HTTPS / TLS
  - Princípios de proteção de dados e de endpoints
- Escalabilidade
  - Escala vertical × horizontal
  - Gargalos comuns
  - *Load balancing* (visão conceitual)
- *Caching* e performance
  - Onde e por que cachear
  - Cache no servidor, em intermediários e no cliente
  - Invalidação de cache (problema clássico)
- Idempotência, consistência e tolerância a falhas (introdução)
  - Operações idempotentes
  - Consistência eventual (conceito)
  - O que significa um sistema tolerante a falhas em nível introdutório
- Estilos arquiteturais (visão geral e *trade-offs*)
  - Monólito
  - Orientado a serviços
  - Microserviços (apenas visão de alto nível e quando considerar)
  - Critérios de escolha
- Ambientes, ciclo de vida e deploy
  - Desenvolvimento, homologação e produção
  - O que muda entre ambientes
  - Conceito de pipeline e entrega contínua (visão de princípios)

## Avaliação

Ao **fim de cada unidade**, será realizada uma **avaliação parcial** dos conteúdos ministrados durante o curso da unidade, <span style="color:red;font-weight: bold;">totalizando em 03 (três) avaliações</span>.

A **nota de cada avaliação** poderá ser **composta por um ou mais instrumentos de avaliação**, de acordo com um dos seguintes casos:

1. Uma prova escrita.
2. Um ou mais trabalhos (individuais ou em grupo).
3. Um ou mais trabalhos, mais uma prova escrita.

Nos casos em que a **avaliação** seja **composta por mais de um instrumento**, será realizado o **somatório** ou a **média ponderada** das **notas obtidas em cada instrumento** para compor a **nota final** de uma **avaliação parcial**.

Os instrumentos a serem utilizados em cada avaliação serão definidos e informados no decorrer do curso.

As **notas** obedecem a uma escala de **0,0 (zero)** a **10,0 (dez)**, contando até a primeira ordem decimal com possı́veis arredondamentos.

Considerar-se-á **aprovado** na disciplina o aluno que obtiver **assiduidade igual ou superior a 75%** e a média **aritmética igual ou superior a 7,0 (sete)** nas <u>avaliações parciais (média parcial)</u>, ou que se submeta a exame final e obtenha média aritmética (média final) entre a média parcial e exame final igual ou superior a 6,0 (seis).

Terá direito de realizar exame final o aluno que satisfaça os requisitos de assiduidade e que obtenha média parcial maior ou igual a 4,0 (quatro) e menor que 7,0 (sete).

### Faltas

As faltas poderão ser justificadas a partir de algum documento que comprove o motivo da falta. Os motivos incluem, mas não se limitam a:

- Choques de horário com outra atividade acadêmica.
- Choques de horário com atividade remunerada (trabalho).
- Questões de saúde.

O documento deve ser enviado para o e-mail <a href="mailto:evandro.silva@ufpi.edu.br">evandro.silva@ufpi.edu.br</a>. O campo **assunto** deverá ser preenchido da seguinte forma: `POO 2 - [Atestado|Declaração] para falta no dia DD/MM`. <span style="color:red;font-weight: bold;">O abono da falta ocorrerá somente ao fim do semestre letivo</span>.

## Calendário

| **AULA** | **Data** | **Dia da semana** | **CONTEÚDO** |
|---|---|---|---|
| 01 | 12/08/26 | Quarta | Apresentação da disciplina <br> O que é Backend e seu lugar no ecossistema web |
| 02 | 13/08/26 | Quinta | Arquitetura Cliente-Servidor |
| 03 | 19/08/26 | Quarta | Protocolo HTTP em profundidade (parte 1) |
| 04 | 20/08/26 | Quinta | Protocolo HTTP em profundidade (parte 2) |
| 05 | 26/08/26 | Quarta | Ciclo de vida de uma requisição HTTP | 
| 06 | 27/08/26 | Quinta | Recursos, URIs e identificação |
| 07 | 02/09/26 | Quarta | Introdução a APIs e Serviços Web |
| 08 | 03/09/26 | Quinta | Princípios REST |
| 09 | 09/09/26 | Quarta | Revisão |
| 10 | 10/09/26 | Quinta | Primeira Avaliação |
| 11 | 16/09/26 | Quarta | Processamento de requisições no servidor |
| 12 | 17/09/26 | Quinta | Pipeline de processamento e middlewares |
| 13 | 23/09/26 | Quarta | Gerenciamento de Estado |
| 14 | 24/09/26 | Quinta | Autenticação e Autorização |
|    | 30/09/26 | Quarta | **SINFO** |
| 15 | 01/10/26 | Quinta | Validação e sanitização de entradas |
| 16 | 07/10/26 | Quarta | Tratamento de erros e design de respostas |
| 17 | 08/10/26 | Quinta | Persistência de dados |
| 18 | 14/10/26 | Quarta | Logging, auditoria e observabilidade básica |
| 	 | 15/10/26 | Quinta | Recesso acadêmico |
| 	 | 21/10/26 | Quarta | **BRACIS** |
| 	 | 22/10/26 | Quinta | **BRACIS** |
| 	 | 28/10/26 | Quarta | Feriado: Dia do Servidor Público |
| 19 | 29/10/26 | Quinta | Revisão |
| 20 | 04/11/26 | Quarta | Segunda Avaliação |
| 21 | 05/11/26 | Quinta | Design de APIs — boas práticas |
| 22 | 11/11/26 | Quarta | Segurança no Backend |
| 23 | 12/11/26 | Quinta | Escalabilidade |
| 24 | 18/11/26 | Quarta | Caching e performance |
| 25 | 19/11/26 | Quinta | Idempotência, consistência e tolerância a falhas (introdução) |
| 26 | 25/11/26 | Quarta | Estilos arquiteturais (visão geral e *trade-offs*) |
| 27 | 26/11/26 | Quinta | Ambientes, ciclo de vida e deploy |
| 28 | 02/12/26 | Quarta | Projeto integrado |
| 29 | 03/12/23 | Quinta | Projeto integrado |
| 30 | 09/12/26 | Quarta | Terceira Avaliação |
| 31 | 10/12/26 | Quinta | Terceira Avaliação |
|    | 16/12/26 | Quarta | Prova Final |
|    | 17/12/26 | Quinta | |