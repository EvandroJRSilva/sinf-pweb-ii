# Aula 03 - 🌐 Armazenamento no Navegador: Cookies, sessionStorage e localStorage

## 🎯 Objetivos da Aula
- Compreender os principais mecanismos de armazenamento no navegador.  
- Diferenciar **cookies**, **sessionStorage** e **localStorage**.  
- Implementar exemplos práticos em **JavaScript**.  
- Integrar cookies com um servidor em **Python/Flask**.  

---

## 📚 Referências
- MDN Web Docs – [Cookies](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Cookies), [localStorage](https://developer.mozilla.org/pt-BR/docs/Web/API/Window/localStorage), [sessionStorage](https://developer.mozilla.org/pt-BR/docs/Web/API/Window/sessionStorage).
- Miguel Grinberg – Flask Web Development (2ª edição).
- Mozilla Developer Network – [Uma visão geral do HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Overview).

MDN Web Docs – Cookies

## 🔑 1. Por que armazenar dados no navegador?
Muitas vezes uma aplicação web precisa **guardar informações do usuário**:  
- Preferências (tema claro/escuro, idioma).  
- Dados de login e autenticação.  
- Itens de um carrinho de compras.  

Existem três mecanismos principais para isso:  
1. **Cookies** – armazenamento leve, também acessível pelo servidor.  
2. **sessionStorage** – dados temporários, válidos apenas enquanto a aba/janela está aberta.  
3. **localStorage** – dados persistentes, mantidos mesmo após fechar o navegador.  

---

## 🍪 2. Cookies
- Criados originalmente para permitir **sessões de usuário**.  
- Podem ser **acessados pelo servidor** em cada requisição HTTP.  
- Tamanho máximo: ~4 KB por cookie.  
- Possuem **data de expiração**.  

[Exemplo](./cookies.html).

## 📌 3. sessionStorage
- Armazena dados somente durante a sessão (aba/janela aberta).
- Dados são apagados ao fechar a aba.
- Mais seguro para informações temporárias.

[Exemplo](./sessionStorage.html).

## 💾 4. localStorage
- Armazena dados de forma persistente (não expiram).
- Capacidade maior (~5MB por domínio).
- Bom para preferências do usuário.

[Exemplo](./localStorage.html).

## ⚡ 5. Comparando os métodos

| Mecanismo          | Duração        | Acessível pelo servidor | Capacidade | Uso típico                   |
| ------------------ | -------------- | ----------------------- | ---------- | ---------------------------- |
| **Cookies**        | Até expirar    | ✅ Sim                   | \~4 KB     | Autenticação, sessões, login |
| **sessionStorage** | Até fechar aba | ❌ Não                   | \~5 MB     | Dados temporários de sessão  |
| **localStorage**   | Persistente    | ❌ Não                   | \~5 MB     | Preferências, dados offline  |

## 🐍 6. Exemplo de Cookies no Servidor com Flask

[cookies.py com Flask](./cookies.py).

## 📝 7. Atividades Propostas

### 💾 localStorage

1. Crie uma página que salve a cor preferida do usuário no `localStorage` e a aplique no background da página
2. **Salvando preferências de tema**: Crie uma página que permita ao usuário alternar entre tema claro e tema escuro, salvando a escolha em `localStorage`.
3. **Formulário persistente**: Ao preencher um formulário (nome, email), salve os valores em `localStorage` e carregue-os automaticamente quando a página for aberta novamente.
4. **Lista de tarefas**: Desenvolva um to-do list simples que armazene as tarefas em `localStorage`, de modo que elas não desapareçam após recarregar a página.
5. **Histórico de acessos**: Registre a data e hora de cada acesso à página em `localStorage` e exiba o histórico.
6. **Contador de visitas persistente**: Crie um contador que incremente a cada visita do usuário e salve o valor em `localStorage`.
7. **Preferências de idioma**: Permita que o usuário escolha um idioma (ex: português, inglês) e salve em `localStorage`. Ao recarregar, o site deve mostrar o idioma selecionado.
8. **Carrinho de compras persistente**: Simule um carrinho de compras que armazene os itens adicionados em `localStorage`, para que não sejam perdidos ao fechar o navegador.
9. **Configurações de layout**: Crie botões para aumentar/diminuir o tamanho da fonte da página e salve a configuração em `localStorage`.
10. **Aplicativo de notas**: Desenvolva um bloco de notas no navegador que salve automaticamente o texto digitado em `localStorage`.

## 📌 sessionStorage

1. Implemente uma aplicação que use `sessionStorage` para guardar o nome do usuário digitado em um formulário e exibir esse nome em diferentes páginas abertas na mesma aba.
2. **Armazenando o nome do usuário**: Crie um formulário simples que peça o nome do usuário e armazene-o em `sessionStorage`. Exiba o nome em uma mensagem de boas-vindas.
3. **Itens temporários de carrinho**: Simule um carrinho de compras temporário, que desaparece quando o usuário fecha a aba.
4. **Timer de sessão**: Crie um cronômetro que conta o tempo desde que a aba foi aberta e armazene o valor em `sessionStorage`.
5. **Formulário multi-páginas**: Implemente um formulário dividido em duas páginas. Os dados preenchidos na primeira devem ser armazenados em `sessionStorage` e recuperados na segunda.
6. **Status de login temporário**: Crie um sistema de login simples que armazena o usuário logado em `sessionStorage` (só vale enquanto a aba estiver aberta).
7. **Histórico de navegação na sessão**: Registre as páginas visitadas dentro da mesma sessão e exiba o histórico.
8. **Pontuação de jogo**: Simule um jogo onde a pontuação atual do usuário é armazenada em `sessionStorage`.
9. **Preferências de aba**: Permita que o usuário selecione uma cor de fundo para a aba atual e salve em `sessionStorage`. Ao abrir uma nova aba, a cor não deve persistir.
10. **Verificação de sessão ativa**: Implemente uma verificação que mostre se ainda existe uma sessão válida em `sessionStorage` (ex: "Sessão ativa" ou "Sessão encerrada").

## 🍪 Cookies

1. Modifique o exemplo em `Flask` para salvar no `cookie` o idioma preferido do usuário (ex: pt-BR ou en-US) e retornar uma mensagem no idioma escolhido.
2. **Salvar nome do usuário em cookie**: Crie um formulário para capturar o nome e salvá-lo em um cookie com validade de 7 dias.
3. **Contador de visitas com cookies**: Registre quantas vezes o usuário visitou a página utilizando cookies.
4. **Lembrar idioma escolhido**: Crie uma página multilíngue e salve a escolha do idioma em cookie.
5. **Data da última visita**: Salve em cookie a data/hora da última visita do usuário e exiba na próxima vez que ele acessar a página.
6. **Checkbox “Lembrar-me”**: Implemente um formulário de login com a opção "Lembrar-me". Se marcada, salve o usuário em cookie.
7. **Expiração de cookies**: Crie um cookie que expira após 1 minuto e mostre uma mensagem se ele já tiver expirado.
8. **Preferência de layout com cookies**: Permita ao usuário escolher entre layout em lista ou em grade e salve essa preferência em cookie.
9. **Carrinho de compras com cookies**: Simule um carrinho que salve os itens adicionados em cookies, acessíveis ao servidor Flask.
10. **Integração com Flask**: Crie uma rota Flask que leia um cookie usuario e retorne uma mensagem personalizada (“Bem-vindo de volta, João!”).