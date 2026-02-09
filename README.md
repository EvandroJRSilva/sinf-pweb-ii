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

- HAVERBEKE, Marijn. **Eloquent JavaScript**. 4 ed. No starch press. Disponível em [https://eloquentjavascript.net/](https://eloquentjavascript.net/). Acesso em 21 ago. 2025.
- GRINBERG, Miguel. **Flask Web Development: Developing Web Applications with Python**. 2 ed. O'Reilly Media, 2018.
- **Mozilla Developer Network (MDN Web Docs)**. Disponível em [https://developer.mozilla.org/pt-BR/](https://developer.mozilla.org/pt-BR/). Acesso em 21 ago. 2025.
- roadmap.sh. **Backend Developer**. Developer Roadmaps, 2026. Disponível em: https://roadmap.sh/backend. Acesso em: 07 fev. 2026.

### Complementar

#### PPC

- CRANE, D.; PASCARELLO, E.; DARREN, J. **Ajax em Ação**. 1 ed. São Paulo: Pearson, 2007.
- BURKE, B.; MONSON, R. **Enterprise JavaBeans 3.0**. 5 ed. São Paulo: Pearson, 2007.
- JENDROCK, E.; GOLLAPUDI, H.; SRIVATHSA. **JAVA EE 6 Tutorial: The Basic Concepts**. 4 ed. São Paulo: Pearson, 2011.
- FELKE-MORRIS, T. **Basic of Web HTML5 Design & CSS3**. São Paulo: Prentice-hall, 2012.
- GRAHAM, S. **Building WebService with Java**. 2 ed. Pearson, 2005.

#### Atualizada

- PILGRIM, Mark. **Dive into HTML5 with illustrations from the public domain**. Disponível em [https://mislav.github.io/diveintohtml5/](https://mislav.github.io/diveintohtml5/) (HTML, contéudo em Inglês), ou [https://www.jesusda.com/docs/ebooks/ebook_manual_en_dive-into-html5.pdf](https://www.jesusda.com/docs/ebooks/ebook_manual_en_dive-into-html5.pdf) (PDF), ou [https://github.com/zenorocha/diveintohtml5](https://github.com/zenorocha/diveintohtml5) (conteúdo traduzido). Acesso a todas as páginas citadas em 20 ago. 2025.
- **OWASP Application Security Verification Standard (ASVS)**. Disponível em [https://owasp.org/www-project-application-security-verification-standard/](https://owasp.org/www-project-application-security-verification-standard/). Acesso em 21 ago. 2025.
- **SQL Tutorial**. Disponível em [https://www.sqltutorial.org/](https://www.sqltutorial.org/). Acesso em 21 ago. 2025.

## Conteúdo Programático

### Unidade 1 - Bancos de Dados e Comunicação Síncrona vs. Assíncrona

- Bancos de Dados Relacionais
	- Conceitos
		- Transações
		- ACID
		- Normalização
	- SQLite
	- PostgreSQL
	- ORMs
- Comunicação síncrona vs. assíncrona
	- XMLHttpResquest API
	- Fetch API
	- Cookie Store API

### Unidade 2 - APIs, Autenticação, Segurança, Caching, Servidores e Integração

- APIs
	- REST
	- JSON APIs
- Autenticação
	- Basic Authentication
	- Token Authentication
	- Cookie Based Authentication
	- Web Authentication API
	- JWT
	- OAuth
- Segurança
	- HTTPs
	- OWASP Risks
	- CORS
	- SSL/TLS
	- CSP
	- Server Security
	- API Security Best Practices
	- Hashing Algorithms
		- MD5
		- SHA
		- scrypt
		- bcrypt
- Caching
	- HTTP Caching
	- Redis
- Web Servers
	- Nginx
	- Apache
- Padrões de integração
	- Streaming
	- Structured Outputs
	- Function Calling

### Unidade 3 - Tópicos

- CI/CD
- Testes
	- Teste de unidade
	- Teste funcional
	- Teste de integração
- Containerização
	- Docker
	- Kubernetes
- Padrões de arquitetura
	- Monolítico
	- Microserviços
	- MVC
	- SOA
	- Serverless
- Escalando Bancos de Dados
	- Database Indexes
- Bancos de Dados NoSQL
	- Firebase (realtime)
	- MongoDB (documents)
	- Redis (key-value)
	- ClickHouse/Cassandra (column)
	- Neo4j (graph)
	- Influx DB (time series)

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

<link rel="stylesheet" href="calendario.css">

<span class="badge aula">AULA</span>
<span class="badge feriado">FERIADO</span>
<span class="badge prova">PROVA</span>

<div class="tabelas">
    <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Março</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>02</td>
  			<td>03</td>
  			<td>04</td>
  			<td>05</td>
  			<td>06</td>
  		</tr>
  		<tr>
  			<td>09</td>
  			<td>10</td>
  			<td class="aula" conteudo="Apresentação da disciplina; BDs Relacionais: Transações e ACID.">11</td>
  			<td class="aula" conteudo="Normalização.">12</td>
  			<td>13</td>
  		</tr>
  		<tr>
  			<td>16</td>
  			<td>17</td>
  			<td class="aula" conteudo="SQLite e PostgreSQL.">18</td>
  			<td class="aula" conteudo="Comunicação síncrona vs. assícrona. AJAX. Fetch API.">19</td>
  			<td>20</td>
  		</tr>
  		<tr>
  			<td>23</td>
  			<td>24</td>
  			<td class="aula" conteudo="Fetch API (continuação)">25</td>
  			<td class="aula" conteudo="Cookie Store API">26</td>
  			<td>27</td>
  		</tr>
  		<tr>
  			<td>30</td>
  			<td>31</td>
  			<td></td>
  			<td></td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Abril</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td class="aula" conteudo="Revisão">01</td>
  			<td class="prova" conteudo="AV1">02</td>
  			<td class="feriado" conteudo="Sexta-feira da paixão">03</td>
  		</tr>
  		<tr>
  			<td>06</td>
  			<td>07</td>
  			<td class="aula" conteudo="REST APIs. JSON APIs.">08</td>
  			<td class="aula" conteudo="Autenticação: Básica e Token.">09</td>
  			<td>10</td>
  		</tr>
  		<tr>
  			<td>13</td>
  			<td>14</td>
  			<td class="aula" conteudo="Autenticação: Cookie e Web Authentication API.">15</td>
  			<td class="aula" conteudo="Autenticação: JWT e OAuth.">16</td>
  			<td>17</td>
  		</tr>
  		<tr>
  			<td>20</td>
  			<td class="feriado" conteudo="Tiradentes">21</td>
  			<td class="aula" conteudo="Segurança: HTTPs, OWASP Risks, CORS e SSL/TLS.">22</td>
  			<td class="aula" conteudo="Segurança: CSP e Server Security. Melhores práticas.">23</td>
  			<td>24</td>
  		</tr>
  		<tr>
  			<td>27</td>
  			<td>28</td>
  			<td class="aula" conteudo="Hashing algorithms: MD5 e SHA.">29</td>
  			<td class="aula" conteudo="Hashing algorithms: scrypt e bcrypt.">30</td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Maio</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td></td>
  			<td></td>
  			<td class="feriado" conteudo="Dia do Trabalho">01</td>
  		</tr>
  		<tr>
  			<td>04</td>
  			<td>05</td>
  			<td class="aula" conteudo="HTTP caching. Redis.">06</td>
  			<td class="aula" conteudo="Nginx.">07</td>
  			<td>08</td>
  		</tr>
  		<tr>
  			<td>11</td>
  			<td>12</td>
  			<td class="aula" conteudo="Apache server.">13</td>
  			<td class="aula" conteudo="Padrões de integração.">14</td>
  			<td>15</td>
  		</tr>
  		<tr>
  			<td>18</td>
  			<td>19</td>
  			<td class="prova" conteudo="AV2">20</td>
  			<td class="prova" conteudo="AV2">21</td>
  			<td>22</td>
  		</tr>
  		<tr>
  			<td>25</td>
  			<td>26</td>
  			<td class="aula" conteudo="CI/CD.">27</td>
  			<td class="aula" conteudo="Testes.">28</td>
  			<td>29</td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Junho</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>01</td>
  			<td>02</td>
  			<td class="aula" conteudo="Docker.">03</td>
  			<td class="feriado" conteudo="Corpus Christi">04</td>
			<td>05</td>
  		</tr>
  		<tr>
  			<td>08</td>
  			<td>09</td>
  			<td class="aula" conteudo="Kubernetes.">10</td>
  			<td class="aula" conteudo="Padrões de arquitetura.">11</td>
  			<td>12</td>
  		</tr>
  		<tr>
  			<td>15</td>
  			<td>16</td>
  			<td class="aula" conteudo="Database Indexes.">17</td>
  			<td class="aula" conteudo="Firebase. MongoDB.">18</td>
  			<td>19</td>
  		</tr>
  		<tr>
  			<td>22</td>
  			<td>23</td>
  			<td class="aula" conteudo="Redis. ClickHouse/Cassandra">24</td>
  			<td class="aula" conteudo="Neo4j. Influx DB.">25</td>
  			<td>26</td>
  		</tr>
  		<tr>
  			<td>29</td>
  			<td>30</td>
  			<td></td>
  			<td></td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Julho</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td class="prova" conteudo="AV3">01</td>
  			<td class="prova" conteudo="AV3">02</td>
			<td>03</td>
  		</tr>
  		<tr>
  			<td>06</td>
  			<td>07</td>
  			<td class="prova" conteudo="Avaliação Final">08</td>
  			<td>09</td>
  			<td>10</td>
  		</tr>
  		<tr>
  			<td>13</td>
  			<td>14</td>
  			<td>15</td>
  			<td>16</td>
  			<td>17</td>
  		</tr>
  		<tr>
  			<td>20</td>
  			<td>21</td>
  			<td>22</td>
  			<td>23</td>
  			<td>24</td>
  		</tr>
  		<tr>
  			<td>27</td>
  			<td>28</td>
  			<td>29</td>
  			<td>30</td>
  			<td>31</td>
  		</tr>
  	</tbody>
  </table>
</div>