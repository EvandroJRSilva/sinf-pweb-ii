# Aula 05

## 🔒 Conceitos Fundamentais de Segurança na Web

A segurança na web é um conjunto de medidas e práticas projetadas para proteger sites e aplicações contra ataques, roubo de dados, e interrupções.

### 1\. O Papel da Validação de Dados

A **validação de dados** é, talvez, sua primeira e mais importante linha de defesa. Ela garante que os dados de entrada (seja de formulários, URLs ou APIs) estejam no formato, tipo e faixa de valores esperados, **antes** que sejam processados ou armazenados.

  * **Princípio:** Nunca confie na entrada do usuário. Trate todo dado externo como potencialmente malicioso.
  * **Ação:** Implementar validação tanto no lado do cliente (para usabilidade, mas **não segurança**) quanto no lado do servidor (para segurança real).

Exemplo em Python (Validação Simples):

```python
# Exemplo introdutório de validação no lado do servidor
def validar_idade(idade_str):
    """Garante que a entrada é um número inteiro positivo."""
    try:
        idade = int(idade_str)
        if idade > 0 and idade <= 120:
            return True, "Idade válida."
        else:
            return False, "A idade deve estar entre 1 e 120."
    except ValueError:
        return False, "A idade deve ser um número."

# Testes
print(f"25: {validar_idade('25')}")
print(f"'abc': {validar_idade('abc')}")
print(f"-5: {validar_idade('-5')}")
```

#### 1\.1 Tipos de validação de dados

1. **Formato**: consiste em verificar se um valor segue um padrão predefinido. Por exemplo, verificar: se um endereço de e-mail é válido; se os números inseridos seguem um padrão para cartão de crédito; etc.
2. **Tipo**: consiste em verificar se o tipo de dado é correto. Por exemplo, em um campo para nome não pode ter *int* ou *float*.
3. **Faixa** (*range*): consiste em verificar se um valor está dentro de limites estabelecidos. Por exemplo, um campo de idade que aceita de 1 a 120 anos.
4. **Null** e **Presença**: o primeiro é utilizado para verificar valores ausentes, intencionais (ex.: campos opcionais) ou acidentais (ex.: erro no sistema). O segundo é relacionado às informações críticas, que não podem ser deixadas em branco (*required*).
5. **Unicidade** e **Conferência**/**Pesquisa**: o primeiro serve para garantir que nenhum valor esteja/seja duplicado. Exemplo: cada nome de usuário deve ser único. O segundo é a validação a partir da comparação da entrada com uma lista ou outra fonte externa.
6. **Consistência** ou **Cruzada**: consiste em verificar o relacionamento entre os dados. Por exemplo, a data de registro de um novo usuário não pode ser posterior à data do primeiro login.
7. **Personalizada**: verificações ligadas à lógica do negócio, ou ao contexto do cliente/empresa.
8. **Regex**: o uso de expressões regulares é ideal para verificar strings que devam obedecer a alguma lógica. Por exemplo: regex para validar e-mail.
9. **Detecção de anomalia estatística**: um pouco mais avançado, com uso Aprendizado de Máquina ou modelos estatísticos para detectar anomalias ou irregularidades nos dados.
10. **Checksum** e **hash**: o primeiro é utilizado para garantir a integridade dos dados, enquanto o segundo pode ser melhor utilizado para comparar valores sensíveis, como senhas.

#### 1\.2 [Validação de formulário no lado cliente](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)

A validação no lado cliente, conhecida também como validação de formulário, é uma verificação inicial dos dados fornecidos, sendo também um recurso importante para uma boa experiência de usuário. Porém, essa validação não deve ser **exaustiva**.

Existem dois tipos de validação do lado cliente:

- **Validação por HTML**: os atributos dos elementos do formulário podem definir quais controles são requeridos e quais formatos os dados inseridos pelo usuário precisam seguir.
- **Validação por JavaScript**: funciona como uma extenção ou personalização da validação por HTML.

##### 1\.2\.1 Validação de formulário nativa do HTML

Essa validação costuma ser feita com o uso de atributos. Por exemplo:

- `required`: para especificar se um campo tem preenchimento obrigarótio.
- `minlength` e `maxlength`: para especificar o comprimento mínimo e máximo de algum dado textual.
- `min`, `max` e `step`: para especificar valores mínimos e máximos de dados numéricos, e também progressão aritmética entre esses valores.
- `type`: para especificar o tipo de dado de uma determinada entrada.
- `pattern`: especifica a expressão regular que define o padrão que deve ser seguido pela entrada.

Quando um elemento é válido, ele corresponde à pseudo-classe CSS `:valid`, de forma que isso permite ao desenvolvedor aplicar um estilo específico para esse caso. Existem outras pseudo-classes nesse sentido, como `:user-valid` e `:in-range`.

Da mesma forma, quando um elemento é inválido, ele corresponde à pseudo-classe CSS `:invalid`, e pode ser estilizado de acordo.

Exemplos:

- [*Built-in form validation exemples*](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#built-in_form_validation_examples).
- [*Validating forms using JavaScript*](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#validating_forms_using_javascript).


<!--
**Validação** de dados é o processo de **verificação** da **precisão**, **integridade** e **consistência** dos dados **antes de serem processados ​​ou armazenados**.

**Boas práticas de validação**:

- **Definir regras de validação claras**: estabeleça regras explícitas para os formatos dos dados, faixa de valores e campos obrigatórios durante a fase de planejamento. Essas regras devem ser simples, consistentes e alinhadas com as regras de negócio para garantir a integridade dos dados desde o início do projeto.
- **Implementar validação de múltiplas camadas**: valide os dados em múltiplos estágios para identificar erros precocemente e reduzir o risco de propagação deles pelo(s) sistema(s).
  - ***Client-side***: em formulários web, tanto HTML/CSS quanto JavaScript podem fornecer *feedback* aos usuários, de forma a melhorar a experiência de usuário. Ao mesmo tempo, podem também ser usados como os primeiros "filtros", os quais evitam o envio para o servidor de dados inconsistentes ou vazios.
  - ***Server-side***: todos os dados precisam ser reavaliados para prevenir vulnerabilidades de segurança, como SQL Injetction, e forçar a integridade dos dados, mesmo que a validação no *client-side* tenha sido OK.
  - **Nível de banco de dados**: devem ser usadas restrições (`UNIQUE`, `CHECK`, `NOT NULL`) e integridade referencial[^1] como precaução de armazenamento de dados inválidos.
- **Automatizar o processo de validação**.
- **Fornecer feedback claro e imediato sobre erros**: quando necessário exiba mensagens de erro precisas e empáticas próximas aos seus respectivos campos cuja validação falhou. Explique o que aconteceu de errado e o que fazer para evitar o erro novamente. Evite mensagens genéricas.
- **Registre e monitore falhas de validação**: mantenha *logs* detalhados dos erros de validação. Este documento pode ajudar no diagnóstico de erros recorrentes e identificação de padrões sobre os dados errados. Monitore o andamento sistema como um todo.
- **Implemente a rigorosidade e desempenho de forma balanceada**: validações muito complexas podem diminuir o desempenho do sistema, piorando a experiência de usuário. Otimize os processos de validação para que sejam o mais eficiente possível.
- **Valide considerando fontes externas**: quando possível, cruze os dados com alguma referência externa. Por exemplo, a validação de um endereço pode ocorrer com a checagem da base de dados dos Correios.
- **Faça auditorias e revise as regras de validação regularmente**: à medida em que os dados e sistemas evoluem, as regras de validação também evoluem. Periodicamente reveja os procedimentos de validação e garanta que elas continuem relevantes e efetivas.

[^1]: Trata-se de um conceito em banco de dados sobre garantir que o relacioanemnto entre tabelas seja consistente e precisa.
-->

---

### 2\. Princípio do Menor Privilégio (PoLP)

O **Princípio do Menor Privilégio (*Principle of Least Privilege* - PoLP)** é um conceito de cybersegurança e afirma que um usuário, processo ou programa, deve ter apenas as permissões necessárias para realizar suas tarefas designadas e **nada mais**.

  * **Impacto:** Se um invasor comprometer uma parte do sistema, seus danos serão limitados pela baixa permissão que essa parte tinha.
  * **Aplicação:** Se o servidor web só precisa *ler* arquivos de configuração, ele não deve ter permissão de *escrita* neles. Se a aplicação só precisa de acesso a dados específicos do banco de dados, a conta de acesso ao DB deve ser restrita a esses dados.

#### 2\.1 Aspectos chave do princípio

- **Minimizar a exposição**: a limitação de privilégios restringe o ataque de superfície, ou seja, uma conta comprometida terá um escopo limitado do que pode afetar.
- **Aplicação ampla**: o PoLP não é aplicável somente a usuários humanos, mas também a aplicações, serviços e dispositivos.
- **Acesso baseado em papel**: um método de implementação comum é definir papéis baseados na função de um funcionário e atribuir permissões de acordo com o cargo. Isso garante que um usuário do setor de marketing, por exemplo, não tenha acesso ao ambiente de desenvolvimento.
- **Proteção contra erro humano**: a restrição de acesso previna que usuários executem funções que não precisam executar, evitando ou mitigando erros acidentais ou ainda desconfigurando parte do sistema.
- **Acesso *Just-in-Time* (JIT)**: consiste em garantir privilégios somente quando necessário e por tempo limitado.

---

### 3\. Conceito de Segurança por Camadas (Defense in Depth)

A **Segurança por Camadas (Defense in Depth)** é a prática de usar **múltiplas** camadas de controles de segurança independentes para proteger recursos. Se uma camada falhar, a próxima servirá de backup.

  * **Exemplo de Camadas:** Firewall (rede) $\rightarrow$ Autenticação/Autorização (aplicação) $\rightarrow$ Validação de dados (código) $\rightarrow$ Criptografia de dados (armazenamento).
  * **Vantagem:** Não há um "ponto único de falha".

> **Youtube**: [Network Security | Defense in Depth](https://www.youtube.com/watch?v=IiWFMIgKaqQ).


## 💣 Principais Ameaças na Web

Agora, vamos mergulhar nas três ameaças mais comuns e perigosas que vocês encontrarão.

> **Código Fonte TX: [💀 TOP 10 Ameaças de Segurança em Aplicações Web - DICAS DE PREVENÇÃO!](https://www.youtube.com/watch?v=OzBy8nYLY-I)**

### 1\. Cross-Site Scripting (XSS)

O **XSS** ocorre quando um invasor injeta *scripts* maliciosos (geralmente JavaScript) em um website que é visualizado por outros usuários. Ele permite que o atacante roube cookies de sessão, altere o conteúdo da página ou redirecione o usuário.

  * **Tipos Comuns:** Armazenado (Strored), Refletido (Reflected) e Baseado no DOM (DOM-based).
  * **Mitigação:** **Sanitização de dados** e **Escape/Codificação de *Output***. Qualquer dado do usuário que será renderizado na página deve ser codificado para que o navegador o trate como texto, e não como código executável.

#### 1\.1 Exemplo (Conceitual de Mitigação)

Imagine um sistema que mostra o nome do usuário:

  * **Vulnerável:** Se o nome for `<script>alert('XSS!')</script>`, o navegador executa o script.
  * **Mitigado:** Se o código for *escapado*, o navegador o exibe como o texto `&lt;script&gt;alert('XSS!')&lt;/script&gt;`, sem executar nada.

Para um aprofundamento visual e prático no XSS, vejam este vídeo (é um vídeo popular e muito instrutivo sobre o ataque):

> **Código Fonte TV:** [⚔️ XSS Attack (Como Funciona e Como Prevenir Ataques) // Dicionário do Programador)](https://www.youtube.com/watch?v=2LYPyUk-L0k)

-----

### 2\. Cross-Site Request Forgery (CSRF)

O **CSRF** (pronuncia-se "Sea-Surf") força um usuário autenticado a enviar uma requisição indesejada para uma aplicação web na qual ele está logado. O ataque explora a confiança que um site tem no navegador de um usuário.

  * **Cenário:** Um usuário está logado em seu banco (Site A). Ele visita um site malicioso (Site B). O Site B carrega uma imagem oculta ou um formulário automático que envia uma requisição (ex: "transferir $1000") para o Site A. O Site A vê os cookies de sessão e processa a requisição, achando que o usuário a iniciou.
  * **Mitigação:** O uso de **Tokens Anti-CSRF** (tokens únicos e imprevisíveis incluídos em cada requisição *POST*).

#### 2\.2 Exemplo em Python (Token Anti-CSRF Conceitual com Flask)

Embora a implementação completa use um framework web, o conceito de token é simples:

```python
import secrets

# No servidor, ao gerar o formulário
def gerar_token_csrf():
    return secrets.token_hex(16) # Gera um token aleatório

# Token é inserido no formulário (campo hidden)
token_atual = gerar_token_csrf()
# <input type="hidden" name="csrf_token" value="{{ token_atual }}">

# No servidor, ao receber a requisição
def processar_requisicao(token_recebido, token_na_sessao):
    if token_recebido == token_nao_sessao:
        print("Requisição VÁLIDA: Tokens correspondem. Ação executada.")
        return True
    else:
        print("Requisição INVÁLIDA (CSRF provável): Tokens NÃO correspondem.")
        return False

# Teste (Sucesso)
print(processar_requisicao(token_atual, token_atual))

# Teste (Falha - O token do atacante seria NULO ou FALSO)
print(processar_requisicao("token_falso", token_atual))
```

-----

### 3\. SQL Injection (SQLi)

A **SQL Injection** ocorre quando um invasor interfere nas *queries* (consultas) SQL que uma aplicação faz ao seu banco de dados, permitindo a visualização, modificação ou exclusão de dados. É um ataque direto à camada de dados.

  * **Vulnerabilidade:** Acontece quando a entrada do usuário é concatenada diretamente em uma string SQL.
  * **Mitigação:** Uso de **Consultas Parametrizadas** (ou *Prepared Statements*). Isso garante que a entrada do usuário seja tratada *sempre* como dados, e não como parte do comando SQL.

#### 3\.1 Exemplo em Python (SQL Injection VS. Consulta Segura)

```python
# Módulo de Banco de Dados (exemplo conceitual)
class Database:
    def execute(self, query):
        # Apenas simula a execução
        print(f"Executando SQL: {query}")

db = Database()
username_entrada = "user_normal"
password_entrada = "' OR '1'='1" # Payload de Ataque Comum!

# --- 1. CÓDIGO VULNERÁVEL (Concatenando a string) ---
# A query final fica: "SELECT * FROM users WHERE username = 'user_normal' AND password = '' OR '1'='1'"
# O 'OR 1=1' faz o WHERE ser TRUE para qualquer linha, permitindo o login sem senha.
vulnerable_query = f"SELECT * FROM users WHERE username = '{username_entrada}' AND password = '{password_entrada}';"
print("--- 1. CÓDIGO VULNERÁVEL ---")
db.execute(vulnerable_query)


# --- 2. CÓDIGO SEGURO (Consultas Parametrizadas) ---
# A query é passada separada dos dados. O banco trata a entrada como VALOR de campo.
# O payload inteiro (' OR '1'='1) é tratado como a senha que o usuário está procurando, o que falhará.
secure_query = "SELECT * FROM users WHERE username = %s AND password = %s;"
parametros = (username_entrada, password_entrada)

print("\n--- 2. CÓDIGO SEGURO (Consultas Parametrizadas) ---")
print(f"SQL a ser executado: {secure_query}")
print(f"Parâmetros: {parametros}")
# O módulo de banco de dados se encarrega de garantir que os parâmetros sejam escapados.
```

> **Código Fonte TV:** [SQL Injection (Do Ataque a Prevenção) // Dicionário do Programador](https://www.youtube.com/watch?v=jN8QGOxdhvM)

## 📚 Referências e Próximos Passos

Referências e estratégias para aprofundar seus conhecimentos:

  * [**OWASP Top 10**](https://owasp.org/www-project-top-ten/): A lista mais importante dos riscos de segurança mais críticos para aplicações web.
  * **Documentação dos *Frameworks***: Todo framework moderno (como Django, Flask, Rails, Spring) tem documentação específica sobre como mitigar CSRF, XSS e SQLi.
  * **Artigos de Segurança:** Pesquisar as mitigações específicas para a linguagem/tecnologia que você está usando (ex: "SQL injection prevention in Python").