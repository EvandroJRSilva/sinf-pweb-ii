# Exercícios para AV1

Fontes para consulta:

- https://eloquentjavascript.net/11_async.html
- https://developer.mozilla.org/pt-BR/docs/conflicting/Learn/JavaScript/Asynchronous/Introducing
- https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Async_JS/Introducing
- https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API
- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Cookies
- https://developer.mozilla.org/en-US/docs/Web/API/Cookie_Store_API
- https://developer.mozilla.org/pt-BR/docs/Web/API/Web_Storage_API

## 1

Qual das opções abaixo representa melhor a característica de uma operação assíncrona em JavaScript?

A) Bloqueia toda a execução até terminar.

B) Executa em paralelo com outras linguagens compiladas.

C) Permite que o restante do código continue executando enquanto espera um resultado.

D) Substitui completamente a execução síncrona.

E) Sempre exige uso de `async/await`.

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 2

Complete: O método `fetch()` retorna um objeto do tipo \_\_\_\_\_\_\_\_, que representa a resposta futura de uma operação de rede.

A) Callback

B) Promise

C) Await

D) Storage

E) Cookie

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 3

Sobre `setTimeout()`:

1. ( ) É uma função assíncrona.
2. ( ) Executa imediatamente o código dentro dela.
3. ( ) Pode ser usada para simular atraso em código.
4. ( ) Sempre bloqueia a execução principal.
5. ( ) Aceita dois argumentos principais: função e tempo.
   
Alternativas:
   
A) V, F, V, F, V
   
B) F, V, F, V, F
   
C) V, V, F, V, V
   
D) V, F, V, V, V
   
E) F, F, F, V, V
   
<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 4

Associe os termos à descrição correta:

1. **Promise**
2. **Callback**
3. **Fetch API**
4. **Await**
5. **Cookies**

( ) Forma tradicional de lidar com assíncrono antes de Promises.

( ) Mecanismo de persistência enviado junto em requisições HTTP.

( ) Função moderna para requisições de rede.

( ) Palavra-chave para pausar até resolver Promise.

( ) Objeto que representa valor futuro.

A) 1-Objeto futuro / 2-Callback / 3-Fetch / 4-Await / 5-Cookie

B) 2-Objeto futuro / 1-Callback / 4-Fetch / 3-Await / 5-Cookie

C) 1-Objeto futuro / 2-Forma tradicional / 3-Requisições / 4-Pausar / 5-Persistência

D) 1-Fetch / 2-Cookie / 3-Promise / 4-Callback / 5-Await

E) 1-Cookie / 2-Fetch / 3-Await / 4-Callback / 5-Promise

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 5

**Asserção**: *Cookies podem ser enviados automaticamente em requisições HTTP.*

**Razão**: *O navegador inclui cookies associados ao domínio ao enviar uma requisição.*

A) Asserção verdadeira, razão verdadeira, e a razão justifica.

B) Asserção verdadeira, razão verdadeira, mas a razão não justifica.

C) Asserção verdadeira, razão falsa.

D) Asserção falsa, razão verdadeira.

E) Ambas falsas.

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 6

Qual método da Fetch API converte uma resposta JSON em objeto JavaScript?

A) `response.text()`

B) `response.json()`

C) `response.body()`

D) `JSON.parse()` sem argumentos

E) `fetch.json()`

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 7

Quais das opções abaixo são **vantagens do uso de Promises** em comparação a callbacks?

A) Tratamento de erro simplificado com `.catch()`

B) Melhor leitura de código

C) Encadeamento de operações assíncronas

D) Sempre execução mais rápida que callbacks

E) Evitam *callback hell*

Alternativas:

A) A, B, C, E

B) A, C, D

C) B, D, E

D) A, B, D, E

E) Todas as alternativas

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 8

```js
console.log("Início");
setTimeout(() => console.log("Assíncrono"), 0);
console.log("Fim");
```

Qual será a saída no console?

A) Início → Assíncrono → Fim

B) Assíncrono → Início → Fim

C) Início → Fim → Assíncrono

D) Fim → Início → Assíncrono

E) Ordem imprevisível

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 9

Ordene as etapas de uma requisição `fetch()` até consumir os dados JSON:

1. Obter objeto Promise da chamada `fetch()`.
2. Usar `.json()` na resposta.
3. Esperar resolução da Promise.
4. Usar os dados convertidos.

A) 1 → 3 → 2 → 4

B) 1 → 2 → 3 → 4

C) 2 → 1 → 3 → 4

D) 3 → 1 → 4 → 2

E) 4 → 3 → 2 → 1

<details>
  <summary><b>Resposta</b></summary>
  A
</details>


## 10

Ao chamar `fetch(url)`, qual é o comportamento padrão da Promise retornada quando o servidor responde com um status HTTP 404?

A) A Promise é rejeitada automaticamente.

B) A Promise é resolvida e a `Response` tem `ok === false`.

C) A Promise lança uma exceção síncrona.

D) A Promise se transforma em um objeto `Error`.

E) O navegador recarrega a página automaticamente.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 11

Complete: o método `response.json()` do objeto `Response` retorna uma \_\_\_\_\_\_\_\_\_\_ que produz o objeto JavaScript quando o corpo for convertido de JSON.

A) callback

B) Promise

C) string síncrona

D) Error

E) iterador

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 12

Quais das opções a seguir representam **formas corretas** de tratar o resultado de uma Promise do `fetch` para obter o JSON?

A) `{ fetch(...).then(r => r.json()).then(data => /* usar data */) }`

B) `{ const r = fetch(...); const data = r.json(); /* usar data */ }`

C) `{ const r = await fetch(...); const data = await r.json(); }`

D) `{ fetch(...).json().then(data => /* usar data */) }`

E) `{ JSON.parse(fetch(...)) }`

Alternativas (escolher o conjunto correto):

A) A e C apenas

B) B e D apenas

C) A, C e D

D) C e E apenas

E) Todas as alternativas

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 13

Associe cada termo à sua definição (coloque a alternativa que contém a associação correta):

1. `async/await`
2. `callback`
3. `fetch`
4. `localStorage`
5. `HttpOnly` (em cookies)

A) Marca que impede que JavaScript no cliente acesse o cookie.

B) API para requisições HTTP no navegador que retorna Promises.

C) Mecanismo antigo para passar uma função que é invocada quando algo termina.

D) Sintaxe que permite escrever código assíncrono com aparência síncrona.

E) Armazenamento chave/valor persistente no browser (por origem).

Alternativas (correspondência):

A) 1–D, 2–C, 3–B, 4–E, 5–A

B) 1–C, 2–D, 3–A, 4–B, 5–E

C) 1–B, 2–A, 3–D, 4–C, 5–E

D) 1–E, 2–D, 3–C, 4–B, 5–A

E) 1–A, 2–B, 3–C, 4–D, 5–E

<details>
  <summary><b>Resposta</b></summary>
  A
</details>**Resposta:** A

## 14

**A (Asserção):** `async/await` torna o tratamento de erros mais direto porque permite usar `try/catch`.

**R (Razão):** `await` converte automaticamente uma Promise rejeitada em um valor `null`.

A) A e R verdadeiras, R justifica A.

B) A e R verdadeiras, R não justifica A.

C) A verdadeira, R falsa.

D) A falsa, R verdadeira.

E) A e R falsas.


<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 15

Coloque em ordem o fluxo típico ao usar `fetch` com `.then` para obter e usar JSON:

1. Chamar `fetch(url)` → retorna Promise.
2. Chamar `.then(response => response.json())`.
3. Chamar `.then(data => /* usar dados */)`.
4. (Opcional) chamar `.catch(...)` para tratar erros de rede ou exceções.

Qual a ordem correta?

A) 1 → 2 → 3 → 4

B) 2 → 1 → 3 → 4

C) 1 → 3 → 2 → 4

D) 4 → 1 → 2 → 3

E) 1 → 2 → 4 → 3

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 16

Qual afirmação é verdadeira sobre `response.ok` em um objeto `Response` do Fetch?

A) `response.ok` é `true` apenas quando o status é 200 exatamente.

B) `response.ok` é `true` para status na faixa 200–299.

C) `response.ok` indica se o corpo é JSON válido.

D) `response.ok` causa uma rejeição automática da Promise se `false`.

E) `response.ok` indica se o cabeçalho `Content-Type` existe.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 17

Qual das opções **não** é verdade sobre cookies HTTP (em geral)?

A) Podem ter expiração configurada.

B) Podem ser enviados automaticamente em requisições HTTP ao domínio correspondente.

C) Sempre estão disponíveis ao código JavaScript (sem restrição).

D) Podem ser marcados como `Secure` para só serem enviados via HTTPS.

E) Podem ter a flag `SameSite` para controlar envio em contextos cross-site.

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 18

Quais das opções abaixo são verdadeiras sobre a **Web Storage API** (localStorage / sessionStorage)?

A) Os valores são armazenados como strings.

B) A API é assíncrona e baseada em Promises.

C) Alterações em `localStorage` em uma aba podem disparar evento `storage` em outra aba da mesma origem.

D) `sessionStorage` é compartilhado entre abas que abriram a mesma janela.

E) `localStorage` pode ser usado entre diferentes origens.

Conjuntos (escolha o conjunto correto):

A) A e C apenas

B) B e D apenas

C) A, B e C

D) C e E apenas

E) Todas as alternativas

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 19

Considere o código:

```js
fetch('/dados')
  .then(r => {
    if (!r.ok) throw new Error('erro');
    return r.json();
  })
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

Qual é o propósito do `if (!r.ok) throw new Error('erro');` ?

A) Garantir que erros de parse de JSON sejam tratados.

B) Forçar rejeição quando o status HTTP não indica sucesso.

C) Evitar que `response.json()` seja chamado em respostas 200.

D) Transformar a resposta em texto.

E) Iniciar uma segunda requisição automaticamente.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 20

O atributo `HttpOnly` em um cookie tem como finalidade:

A) Fazer com que o cookie seja criptografado.

B) Evitar que o cookie seja acessível via `document.cookie` no JavaScript do cliente.

C) Permitir que o cookie seja enviado somente em conexões HTTP simples (sem HTTPS).

D) Tornar o cookie visível somente em ferramentas de desenvolvedor.

E) Multiplicar automaticamente sua validade.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 21

**A:** A API `localStorage` é adequada para armazenar tokens de autenticação sensíveis.

**R:** Itens em `localStorage` podem ser acessados por qualquer script executado na mesma origem, portanto não são seguros contra XSS.

A) A e R verdadeiras e R justifica A.

B) A e R verdadeiras e R não justifica A.

C) A verdadeira, R falsa.

D) A falsa, R verdadeira.

E) A e R falsas.

<details>
  <summary><b>Resposta</b></summary>
  D
</details>

## 22

Complete: o evento `storage` é disparado quando \_\_\_\_\_\_\_\_\_\_.

A) qualquer alteração em `localStorage` ocorre na **mesma** aba que executa a alteração.

B) é feita uma alteração em `localStorage` em uma aba e outra aba da **mesma origem** recebe a notificação.

C) `sessionStorage` é alterado na mesma aba.

D) um cookie é criado via document.cookie.

E) o navegador fecha.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 23

Sobre `sessionStorage`:

1. Os dados sobrevivem após fechar completamente o navegador.
2. Cada aba/janela tem seu próprio `sessionStorage` separado.
3. Valores são armazenados como strings.
4. Eventos `storage` são disparados na mesma aba que realizou a alteração.
5. `sessionStorage` está limitado à mesma origem.

Alternativas:

A) F, V, V, F, V

B) V, F, F, V, F

C) F, V, V, V, V

D) V, V, V, F, V

E) F, F, V, F, F

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 24

Qual a finalidade da flag `SameSite` em cookies?

A) Especificar que o cookie deve ser criptografado.

B) Controlar se o cookie é enviado em requisições cross-site (proteção contra CSRF).

C) Indicar a data de expiração do cookie.

D) Definir o domínio que irá expor o cookie via document.cookie.

E) Tornar o cookie somente legível por service workers.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 25

Considere:

```js
async function f() {
  const r = await fetch('/api');
  const data = await r.json();
  return data;
}
```

Se a resposta do servidor for um JSON malformado, o que acontece dentro de `f()`?

A) `r.json()` resolve com `undefined`.

B) `r.json()` rejeita e isso faz `await` lançar uma exceção que pode ser capturada com `try/catch`.

C) O `fetch` bloqueia indefinidamente.

D) `f()` retorna uma Promise resolvida com `null`.

E) O navegador recarrega a página.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 26

Associe a API ao seu comportamento:

1. `document.cookie`
2. `localStorage`
3. `Cookie Store API`
4. `fetch`
5. `sessionStorage`

A) Acessível via JavaScript como string (síncrono) — permite leitura/escrita simples de cookies (quando não HttpOnly).

B) Armazenamento chave/valor persistente por origem, síncrono.

C) API moderna baseada em Promises para gerenciar cookies de forma assíncrona.

D) Faz requisições HTTP e retorna Promises.

E) Armazenamento por sessão (aba/janela), limpo ao fechar.

Qual conjunto corresponde corretamente?

A) 1–A, 2–B, 3–C, 4–D, 5–E

B) 1–B, 2–A, 3–D, 4–C, 5–E

C) 1–E, 2–D, 3–C, 4–B, 5–A

D) 1–C, 2–B, 3–A, 4–D, 5–E

E) 1–A, 2–E, 3–B, 4–C, 5–D

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 27

Uma vantagem da Cookie Store API em relação ao uso de `document.cookie` é:

A) Ela é síncrona e muito mais rápida.

B) Provê uma interface baseada em Promises (assíncrona) para ler/escrever cookies.

C) Exclui automaticamente cookies antigos sem intervenção do desenvolvedor.

D) Permite leitura de cookies HttpOnly no cliente.

E) Substitui localStorage.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 28

Você faz um `fetch` para uma API e quer garantir que tanto erros de rede quanto respostas HTTP com erro (404, 500) sejam tratados pelo mesmo `catch`. Qual abordagem é mais razoável?

A) `fetch(url).catch(...)` — isso já captura 404s automaticamente.

B) `fetch(url).then(r => { if(!r.ok) throw new Error(); return r.json(); }).catch(...)` — checar `r.ok` e lançar se necessário.

C) `fetch(url).then(r => r.json()).catch(...)` — sem checar `r.ok`.

D) Envolver `fetch` em `try/catch` sem `await`.

E) Usar `response.text()` sempre em vez de JSON.

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 29

**A:** `localStorage` é compartilhado entre todas as abas que pertencem à mesma origem (domínio + porta + protocolo).

**R:** O evento `storage` é disparado nas demais abas quando uma aba modifica `localStorage`.

A) A e R verdadeiras e R justifica A.

B) A e R verdadeiras e R não justifica A.

C) A verdadeira e R falsa.

D) A falsa e R verdadeira.

E) A e R falsas.

<details>
  <summary><b>Resposta</b></summary>
  A
</details>

## 30

Qual das alternativas **não** é correta sobre `response.json()`?

A) Retorna uma Promise que resolve com o JSON parseado.

B) Pode falhar (rejeitar) se o corpo não for JSON válido.

C) Pode ser chamada múltiplas vezes no mesmo `Response` sem restrições.

D) É assíncrona.

E) Depende do conteúdo do corpo para resolver.

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 31

```js
async function exemplo() {
  return 5;
}
console.log(exemplo());
```

O que será exibido no console?

A) `5` diretamente

B) Uma Promise resolvida com valor `5`

C) `undefined`

D) Erro de execução

E) Nada

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 32

Quais cenários justificam o uso de `async/await`?

A) Substituir funções síncronas pesadas.

B) Melhorar legibilidade em operações assíncronas encadeadas.

C) Garantir ordem lógica de execução.

D) Evitar `try/catch`.

E) Reduzir tempo de rede.

<details>
  <summary><b>Resposta</b></summary>
  B, C (conjunto correto depende de como organizar a múltipla escolha)
</details>

## 33

Associe o uso correto das APIs:

1. **Cookies**
2. **localStorage**
3. **sessionStorage**
4. **Cookie Store API**
5. **Fetch API**

( ) Persistência curta, apenas por aba.

( ) Persistência longa, em par chave-valor.

( ) Comunicação cliente-servidor.

( ) Controle assíncrono moderno sobre cookies.

( ) Identificação em requisições.

<details>
  <summary><b>Resposta</b></summary>
  1-Identificação <br> 
  2-Persistência longa <br> 
  3-Persistência curta <br> 
  4-Controle assíncrono <br> 
  5-Comunicação
</details>

## 34

**Asserção**: *Cookies são sempre acessíveis pelo JavaScript.*

**Razão**: *A flag HttpOnly pode restringir o acesso aos cookies pelo cliente.*

A) Asserção verdadeira, razão verdadeira, mas a razão justifica.

B) Asserção verdadeira, razão verdadeira, mas a razão não justifica.

C) Asserção verdadeira, razão falsa.

D) Asserção falsa, razão verdadeira.

E) Ambas falsas.

<details>
  <summary><b>Resposta</b></summary>
  D
</details>

## 35

Coloque em ordem lógica o ciclo de uso da **Fetch API** para realizar uma requisição e processar a resposta:

1. Processar os dados recebidos (ex.: `response.json()`).
2. Chamar `fetch(url)`.
3. Aguardar a Promise ser resolvida.
4. Encadear `.then()` para tratar a resposta.

a) 1 → 2 → 3 → 4

b) 2 → 3 → 4 → 1

c) 2 → 4 → 3 → 1

d) 3 → 2 → 1 → 4

e) 4 → 3 → 2 → 1

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 36

Associe cada **API** à sua principal funcionalidade:

1. **Fetch API**
2. **Cookie Store API**
3. **Web Storage API**

(A) Permite armazenar pequenos pares chave-valor no navegador de forma síncrona.

(B) Facilita a leitura e escrita de cookies de forma assíncrona.

(C) Realiza requisições HTTP e retorna Promises.

a) 1–A, 2–B, 3–C

b) 1–C, 2–B, 3–A

c) 1–B, 2–C, 3–A

d) 1–A, 2–C, 3–B

e) 1–C, 2–A, 3–B

<details>
  <summary><b>Resposta</b></summary>
  B
</details>

## 37

**Aserção (A):** A **Web Storage API** é assíncrona, permitindo operações de leitura e escrita sem bloquear o fluxo principal.

**Razão (R):** O armazenamento local (`localStorage`) e de sessão (`sessionStorage`) utilizam um modelo baseado em Promises.

a) A e R são verdadeiras, e R justifica A.

b) A e R são verdadeiras, mas R não justifica A.

c) A é verdadeira, e R é falsa.

d) A é falsa, e R é verdadeira.

e) A e R são falsas.

<details>
  <summary><b>Resposta</b></summary>
  E (Web Storage é <b>síncrono</b> e não baseado em Promises)
</details>

## 38

Qual das alternativas **não é uma vantagem** de usar **cookies** para persistência de dados?

a) Podem ser enviados automaticamente em cada requisição HTTP.

b) Permitem definir políticas de expiração.

c) São limitados em tamanho (aprox. 4KB por cookie).

d) São compartilhados entre diferentes navegadores do usuário.

e) Podem ser usados para autenticação de sessão.

<details>
  <summary><b>Resposta</b></summary>
  D
</details>

## 39

Complete a frase:

O método `fetch()` retorna uma \_\_\_\_\_\_\_\_\_\_, que representa o resultado futuro de uma requisição e permite encadear métodos como `.then()` e `.catch()`.

a) função

b) callback

c) promessa (Promise)

d) resposta imediata

e) sessão

<details>
  <summary><b>Resposta</b></summary>
  C
</details>

## 40

Analise o código abaixo:

```javascript
localStorage.setItem("tema", "escuro");
sessionStorage.setItem("usuario", "Ana");

console.log(localStorage.getItem("tema"));
console.log(sessionStorage.getItem("usuario"));
```

O que será impresso no console durante a primeira execução no navegador?

a) `undefined` e `undefined`

b) `escuro` e `Ana`

c) `"tema"` e `"usuario"`

d) `null` e `null`

e) Erro de execução

<details>
  <summary><b>Resposta</b></summary>
  B
</details>