---
tags:
  - ufpi/picos
  - ufpi/disciplina/programação_para_web_2
  - principal
código: SINF/CSHNB032
---
<table><thead>
  <tr>
    <th style="font-size:16px;text-align:center;vertical-align:middle" rowspan="2">Período</th>
    <th style="font-size:16px;text-align:center;vertical-align:middle" rowspan="2">Pré-requisitos</th>
    <th style="font-size:16px;text-align:center;vertical-align:middle" colspan="2">Créditos</th>
    <th style="font-size:16px;text-align:center;vertical-align:middle" rowspan="2">Carga Horária</th>
  </tr>
  <tr>
    <th style="text-align:center;">Teórica</th>
    <th style="text-align:center;">Prática</th>
  </tr></thead>
<tbody>
  <tr>
    <td style="text-align:center;">5</td>
    <td style="text-align:center;">Programação para a Web I</td>
    <td style="text-align:center;">2</td>
    <td style="text-align:center;">2</td>
    <td style="text-align:center;">60h</td>
  </tr>
</tbody>
</table>

## Ementa

- Comunicação entre navegador e servidor: Assíncrono e Síncrona.
- Segurança.
- Frameworks e ferramentas de desenvolvimento de aplicações web.
- Controle de sessão.
- Esquema de funcionamento de uma página web com acesso a banco de dados.

## Bibliografia Básica

- DEITEL, H. M; DEITEL, P. J; et al. **Java TM: como programar**. 8 ed. São Paulo: Pearson, 2010.
- HORTMAN, C. S.; CORNELL, G. **Core Java: Volume 1**. 8 ed. São Paulo: Pearson, 2010.
- HORTMAN, C. S.; CORNELL, G. **Core Java: Volume 2**. 8 ed. São Paulo: Pearson, 2010.

### Atualizada

- Haverbeke, Marijn. **Eloquent JavaScript**. 4 ed. No starch press. Disponível em <https://eloquentjavascript.net/>. Acesso em 21 ago. 2025.
- Grinberg, Miguel. **Flask Web Development: Developing Web Applications with Python**. 2 ed. O'Reilly Media, 2018.
- **Mozilla Developer Network (MDN Web Docs)**. Disponível em <https://developer.mozilla.org/pt-BR/>. Acesso em 21 ago. 2025.

## Bibliografia Complementar

- CRANE, D.; PASCARELLO, E.; DARREN, J. **Ajax em Ação**. 1 ed. São Paulo: Pearson, 2007.
- BURKE, B.; MONSON, R. **Enterprise JavaBeans 3.0**. 5 ed. São Paulo: Pearson, 2007.
- JENDROCK, E.; GOLLAPUDI, H.; SRIVATHSA. **JAVA EE 6 Tutorial: The Basic Concepts**. 4 ed. São Paulo: Pearson, 2011.
- FELKE-MORRIS, T. **Basic of Web HTML5 Design & CSS3**. São Paulo: Prentice-hall, 2012.
- GRAHAM, S. **Building WebService with Java**. 2 ed. Pearson, 2005.

### Atualizada

- Pilgrim, Mark. **Dive into HTML5 with illustrations from the public domain**. Disponível em <https://mislav.github.io/diveintohtml5/> (HTML, contéudo em Inglês), ou <https://www.jesusda.com/docs/ebooks/ebook_manual_en_dive-into-html5.pdf> (PDF), ou <https://github.com/zenorocha/diveintohtml5> (conteúdo traduzido). Acesso a todas as páginas citadas em 20 ago. 2025.
- **OWASP Application Security Verification Standard (ASVS)**. Disponível em <https://owasp.org/www-project-application-security-verification-standard/>. Acesso em 21 ago. 2025.
- **SQL Tutorial**. Disponível em <https://www.sqltutorial.org/>. Acesso em 21 ago. 2025.

## Organização da disciplina

### Parte I - Fundamentos de Comunicação Web e Sessões

- **Objetivo geral**
	- Compreender como ocorre a comunicação entre navegador e servidor, diferenciando os modos síncrono e assíncrono, e aplicar mecanismos de controle de sessão em aplicações web.
- **Objetivos específicos**
	- Identificar a arquitetura cliente-servidor e os protocolos básicos da Web. 
	- Diferenciar requisições síncronas e assíncronas, entendendo suas aplicações práticas.
	- Utilizar Ajax e Fetch API para implementar páginas dinâmicas.
	- Compreender conceitos de sessão, cookies, local storage e session storage.
	- Implementar um sistema simples de autenticação de usuários com controle de sessão.


1. **Arquitetura da Web**: Navegador, servidor, protocolos HTTP/HTTPS.
	- Estrutura cliente-servidor.
	- Funcionamento básico do navegador.
	- Servidores web (Apache, Nginx, etc.).
	- Protocolo HTTP e evolução para HTTPS.
	- Ciclo de requisição e resposta.
2. **Comunicação síncrona e assíncrona**: conceitos, exemplos práticos com requisições HTTP.
	- Diferença entre síncrono e assíncrono.
	- O problema da espera em aplicações síncronas.
	- Exemplos práticos no contexto web.
	- Introdução ao conceito de callbacks.
3. **Ajax e Fetch API**: diferenças, aplicações em páginas dinâmicas.
	- História e conceito de Ajax.
	- Uso de XMLHttpRequest vs Fetch API.
	- Diferenças entre os dois métodos.
	- Aplicações em páginas dinâmicas.
	- Conceito de APIs RESTful.
4. **Controle de sessão – fundamentos**: cookies, session storage, local storage.
	- Sessão e estado na Web (stateless).
	- Cookies: definição, usos e limitações.
	- sessionStorage e localStorage.
	- Comparação entre os mecanismos.
5. **Autenticação e gerenciamento de usuários**: login, logout, persistência de sessão.
	- Mecanismos básicos de autenticação (usuário/senha).
	- Fluxo de login e logout.
	- Armazenamento de credenciais (boas práticas).
	- Exemplo conceitual de autenticação em aplicações web.
6. Laboratório: Implementando uma página simples que se comunica com servidor via HTTP.
7. Laboratório: Aplicação prática de requisições síncronas e assíncronas.
8. Laboratório: Implementação de controle de sessão com cookies.
9. Projeto guiado: Criação de um sistema simples de login/logout.

### Parte II - Segurança e Desenvolvimento Estruturado

- **Objetivo geral**
	- Conhecer os principais riscos de segurança em aplicações web e aplicar boas práticas de desenvolvimento, utilizando frameworks e ferramentas de apoio para estruturar aplicações seguras.
- **Objetivos específicos**
	- Reconhecer ameaças comuns de segurança (XSS, CSRF, SQL Injection).
	- Aplicar HTTPS e certificados digitais para comunicação segura.
	- Adotar boas práticas de segurança na validação de dados em formulários.
	- Entender o papel dos frameworks no desenvolvimento de aplicações web.
	- Utilizar ferramentas de apoio (IDEs, controle de versão, bibliotecas) no processo de desenvolvimento.
	- Implementar aplicações seguras com frameworks modernos (ex.: Flask, Django, Express).


1. **Conceitos de segurança na Web**: ameaças comuns (XSS, CSRF, SQL Injection).
	- Principais ameaças: XSS, CSRF, SQL Injection.
	- O papel da validação de dados.
	- Princípio do menor privilégio.
	- Conceito de segurança por camadas.
2. **HTTPS e certificados digitais**: funcionamento e importância.
	- Diferença entre HTTP e HTTPS.
	- Criptografia de chave pública e privada.
	- Funcionamento dos certificados digitais.
	- Autoridades certificadoras.
	- Importância para autenticação e segurança.
3. **Boas práticas de segurança em formulários**: validação no cliente e no servidor.
	- Validação no lado do cliente (JavaScript).
	- Validação no lado do servidor.
	- Tratamento de entradas do usuário.
	- Prevenção contra ataques de injeção.
	- Exemplo de formulário seguro.
4. **Introdução a frameworks de desenvolvimento**: o papel dos frameworks, vantagens.
	- O que são frameworks?
	- Vantagens e desvantagens.
	- Exemplo de frameworks populares (Flask, Django, Express).
	- Estrutura típica de um projeto com framework.
	- Conceito de MVC (Model–View–Controller).
5. **Ferramentas de apoio ao desenvolvimento**: IDEs, sistemas de versionamento, bibliotecas auxiliares.
	- IDEs e editores de texto (VS Code, PyCharm, etc.).
	- Sistemas de versionamento (Git e GitHub/GitLab).
	- Gerenciadores de pacotes (npm, pip).
	- Automação de tarefas (build, testes, deploy).
	- Uso de bibliotecas auxiliares.
6. Laboratório: Detectando e corrigindo falhas de segurança em exemplos de código.
7. Laboratório: Implementando HTTPS em servidor local (exemplo com certificado autoassinado).
8. Laboratório: Criando uma aplicação básica usando framework web (ex: Flask/Django ou Node.js/Express).
9. Projeto guiado: Aplicação com autenticação segura e tratamento de erros.

### Parte III - Integração com Banco de Dados e Projeto Final

- **Objetivo geral**
	- Desenvolver aplicações web completas, capazes de se comunicar com bancos de dados relacionais, aplicando conceitos de modelagem, consultas SQL e boas práticas de integração.
- **Objetivos específicos**
	- Entender o funcionamento de uma aplicação cliente-servidor com acesso a banco de dados.
	- Realizar a modelagem básica de dados com entidades e relacionamentos.
	- Conectar aplicações web a bancos de dados relacionais.
	- Executar consultas SQL (CRUD) a partir de aplicações web.
	- Aplicar boas práticas de segurança e eficiência no acesso a bancos de dados.
	- Desenvolver um projeto final integrando **frontend + backend + banco de dados**, aplicando os conhecimentos adquiridos durante a disciplina.


1. **Funcionamento de uma aplicação com banco de dados**: modelo cliente-servidor.
	- Papel do banco de dados em aplicações web.
	- Modelo cliente-servidor com persistência.
	- Interação entre navegador, servidor e banco.
	- Exemplos de fluxos de requisições com dados.
2. **Modelagem básica de dados**: entidades, atributos e relacionamentos.
	- Conceito de entidade, atributo e relacionamento.
	- Chaves primárias e estrangeiras.
	- Normalização de dados (conceito básico).
	- Exemplo de diagrama entidade-relacionamento (DER).
3. **Conexão servidor–banco de dados**: drivers, bibliotecas de acesso.
	- Drivers de conexão (ex.: psycopg2, sqlite3, mysqlclient).
	- Bibliotecas de abstração (SQLAlchemy, Sequelize).
	- Diferença entre conexão persistente e temporária.
	- Erros comuns e boas práticas na conexão.
4. **Consultas SQL em aplicações web**: SELECT, INSERT, UPDATE, DELETE.
	- Comandos básicos: SELECT, INSERT, UPDATE, DELETE.
	- Filtros com WHERE.
	- Ordenação e paginação de resultados.
	- Inserção de dados via formulários web.
	- Prevenção contra SQL Injection.
5. **Boas práticas na integração banco de dados – servidor web**: segurança e desempenho.
	- Separação entre lógica de negócio e acesso a dados.
	- Uso de ORM (Object-Relational Mapping).
	- Tratamento de erros e exceções em consultas.
	- Estratégias para otimização de consultas.
	- Segurança e desempenho no acesso ao banco.
6. Laboratório: Configuração de banco de dados relacional (MySQL/PostgreSQL/SQLite).
7. Laboratório: Implementando inserção e recuperação de dados em aplicação web.
8. Laboratório: Integração completa página–servidor–banco de dados.
9. Projeto final: Construção de uma aplicação CRUD completa (cadastro e consulta de usuários).

## Materiais por semestre

- [[P. Web II - 2025.2|2025.2]]