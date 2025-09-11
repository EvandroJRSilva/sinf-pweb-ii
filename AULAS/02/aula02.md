# Aula 02

## AJAX

AJAX (**A**synchronous **J**avaScript **A**nd **X**ML), JavaScript Assíncrono e XML (em tradução livre) é um conjunto de **técnicas de desenvolvimento web que usa várias tecnologias** (HTML, CSS, JavaScript, DOM e XMLHttpRequest object) no **lado cliente** para criar aplicações web assíncronas. Foi inicialmente desenvolvido por [Jesse James Garret](https://en.wikipedia.org/wiki/Jesse_James_Garrett) em um [artigo publicado em 2005](https://web.archive.org/web/20150910072359/http://adaptivepath.org/ideas/ajax-new-approach-web-applications/).

Com o AJAX é possível que partes de uma página web possam ser atualizadas sem a necessidade de carregar a página inteira novamente. Além disso, apesar do XML fazer parte do nome, seu uso não é obrigatório e atualmente o JSON é mais utilizado que o XML devido às suas vantagens, como ser mais leve e ser parte do JavaScript.

### Exemplos

O [exemplo 1](./exemplo-1/ajax-index.html) mostra como usar o AJAX para carregar o conteúdo de um [arquivo de texto](./exemplo-1/conteudo.txt) (.txt) e exibi-lo em uma página web sem a necessidade de recarregá-la.

O [exemplo 2](./exemplo-2/ajax-index.html) mostra o uso do AJAX para carregar o conteúdo de um [arquivo JSON](./exemplo-2/dados.json) e exibindo os dados em uma lista.

O [exemplo 3](./exemplo-3/templates/ajax-index.html) mostra o uso do AJAX após utilizar o método `POST` do HTTP. Para criar um servidor foi usado o `Flask`, um framework para desenvolvimento web com Python.

## Fetch API

A [Fetch API](https://fetch.spec.whatwg.org/) é uma interface JavaScript moderna para executar requisições HTTP. Ela substitui o método XMLHttpRequest e provê uma forma mais limpa e flexível de buscar recursos de forma assíncrona.

Foi criada com o objetivo de unificar a busca de recursos na web e fornecer tratamento consistente de tudo o que isso envolva.

**Sintaxe**

```javascript
fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

- **url**: onde os dados serão buscados.
- **options** (opcional): especifica o método, cabeçalho, corpo, etc.
- **response.json()**: converte a resposta em JSON.
- **catch(error)**: para o tratamento de quaisquer erros que tenham ocorrido durante a requisição.

De forma geral **funciona da seguinte forma**:

1. Uma requisição é enviada a um URL específico.
2. O servidor processa a requisição e envia a resposta.
3. A resposta é convertida em JSON, ou outro formato especificado pelo desenvolvedor.
4. Erros são tratados nos blocos `try-catch`.

### Exemplos

Vamos revisitar os exemplos de AJAX, porém utilizando Fetch API:

- [Exemplo 1](./exemplo-1/fetch-index.html)
- [Exemplo 2](./exemplo-2/fetch-index.html)
- [Exemplo 3](./exemplo-3/templates/fetch-index.html)

Novos exemplos:

- [Exemplo 4](./exemplo-4/index.html)
- [Exemplo 5](./exemplo-5/index.html)

<!--
Vamos seguir o guia [Usando Fetch](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch) do MDN para vermos exemplos de código.

#### Requisições Fetch

##### Exemplo simples

```javascript
var myImage = document.querySelector("img");

fetch("flowers.jpg")
  .then(function (response) {
    return response.blob();
  })
  .then(function (myBlob) {
    var objectURL = URL.createObjectURL(myBlob);
    myImage.src = objectURL;
  });
```

Com o código acima uma imagem é procurada e, após ser achada é inserida em um elemento `<img>`.

##### Fornecendo opções de request

```javascript
var myHeaders = new Headers();

var myInit = {
  method: "GET",
  headers: myHeaders,
  mode: "cors",
  cache: "default",
};

fetch("flowers.jpg", myInit)
  .then(function (response) {
    return response.blob();
  })
  .then(function (myBlob) {
    var objectURL = URL.createObjectURL(myBlob);
    myImage.src = objectURL;
  });
```

CORS é o acrônimo para *Cross-Origin Requests Allowed* (solicitações permitidas de origem cruzada, em tradução livre). É o modo padrão de requisições `fetch`, e permite a requisição de recursos localizados em origens diferentes (domínio, protocolo ou porta) da que está servindo a página web atual.

##### Verificando se o fetch foi bem sucedido
-->

## Exercícios

1. Carregar um texto de um arquivo:
    -  Crie um arquivo HTML com um botão e um parágrafo (`<p>`).
    - Crie um arquivo de texto (mensagem.txt) com a frase "Olá, mundo! Esta é a resposta da Fetch API.".
    - Adicione um evento de clique no botão que usa fetch() para carregar o conteúdo de mensagem.txt e exibi-lo no parágrafo.

2. Carregar dados de um arquivo JSON:
    - Crie um arquivo HTML com um botão e uma lista não ordenada (`<ul>`).
    - Crie um arquivo JSON (usuarios.json) com um array de objetos, onde cada objeto tem uma chave nome e uma chave idade.
    - Use fetch() para carregar os dados JSON e, em seguida, itere sobre o array para criar itens de lista (`<li>`) com o nome e a idade de cada usuário, inserindo-os na lista na página.

3. Obter dados de uma API pública e exibir:
    - Use a API pública do JSONPlaceholder para obter o primeiro post (https://jsonplaceholder.typicode.com/posts/1).
    - Crie um HTML com um botão e um elemento para exibir os dados (como uma `<div>`).
    - Ao clicar no botão, faça a requisição e exiba o title e o body do post na página.

4. Exibir uma lista de itens de uma API:
    - Use a API pública do JSONPlaceholder para obter a lista de todos os posts (https://jsonplaceholder.typicode.com/posts).
    - Crie uma lista no HTML.
    - Faça a requisição e exiba o title de cada um dos 100 posts em itens de lista (`<li>`).

5. Exibir uma imagem de uma API de imagens:
    - Use a API pública do Dog API para obter uma imagem aleatória de cachorro (https://dog.ceo/api/breeds/image/random).
    - No HTML, adicione um botão e uma tag `<img>`.
    - Ao clicar no botão, use fetch() para obter a URL da imagem no JSON e atualize o atributo src da tag `<img>` com essa URL.

### Um pouco de desafio

1. Carregar um texto de um arquivo:
    - Crie um arquivo HTML com um botão e um parágrafo (`<p>`).
    - Crie um arquivo de texto (mensagem.txt) com a frase "Olá, mundo! Esta é a resposta da Fetch API.".
    - Adicione um evento de clique no botão que usa fetch() para carregar o conteúdo de mensagem.txt e exibi-lo no parágrafo.

2. Carregar dados de um arquivo JSON:
    - Crie um arquivo HTML com um botão e uma lista não ordenada (`<ul>`).
    - Crie um arquivo JSON (usuarios.json) com um array de objetos, onde cada objeto tem uma chave nome e uma chave idade.
    - Use fetch() para carregar os dados JSON e, em seguida, itere sobre o array para criar itens de lista (`<li>`) com o nome e a idade de cada usuário, inserindo-os na lista na página.

3. Obter dados de uma API pública e exibir:
    - Use a API pública do JSONPlaceholder para obter o primeiro post (https://jsonplaceholder.typicode.com/posts/1).
    - Crie um HTML com um botão e um elemento para exibir os dados (como uma `<div>`).
    - Ao clicar no botão, faça a requisição e exiba o title e o body do post na página.

4. Exibir uma lista de itens de uma API:
    - Use a API pública do JSONPlaceholder para obter a lista de todos os posts (https://jsonplaceholder.typicode.com/posts).
    - Crie uma lista no HTML.
    - Faça a requisição e exiba o title de cada um dos 100 posts em itens de lista (`<li>`).

5. Exibir uma imagem de uma API de imagens:
    - Use a API pública do Dog API para obter uma imagem aleatória de cachorro (https://dog.ceo/api/breeds/image/random).
    - No HTML, adicione um botão e uma tag `<img>`.
    - Ao clicar no botão, use fetch() para obter a URL da imagem no JSON e atualize o atributo src da tag `<img>` com essa URL.