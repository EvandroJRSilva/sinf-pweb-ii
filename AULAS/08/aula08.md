# Aula 08

Sumário

- [Aula 08](#aula-08)
  - [Interação entre navegador, servidor e banco](#interação-entre-navegador-servidor-e-banco)
    - [REST](#rest)
      - [Conteúdo de uma solicitação do cliente da API RESTful](#conteúdo-de-uma-solicitação-do-cliente-da-api-restful)
      - [Autenticação](#autenticação)
      - [Conteúdo de uma resposta do servidor da API RESTful](#conteúdo-de-uma-resposta-do-servidor-da-api-restful)
    - [Rotas no back-end](#rotas-no-back-end)
    - [Frameworks](#frameworks)
  - [Exemplos](#exemplos)


Vimos no início do curso sobre os `cookies` (faltou vermos melhor o [Cookie Store API](https://developer.mozilla.org/en-US/docs/Web/API/Cookie_Store_API)) e vimos também o [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API), ambas ferramentas para armazenamento de dados a partir do navegador.

Tanto com `cookies` quanto com `localStorage` é possível armazenar valores de forma persistente, porém de forma limitada. Se quisermos armazenar diversos tipos de valores, de diversos tamanhos e tipos, e também de forma persistente, precisamos utilizar um `banco de dados`. No nosso caso, precisamos conectar um sistema web com um banco de dados.

Sem adentrar em muitos detalhes, é importante especificar que o sistema web estará rodando tanto em um navegador quanto em um servidor. A parte do sistema que estará rodando em um navegador (`front-end`) se comunicará com a parte que está rodando em um servidor (`back-end`). Esta última é que fará a comunicação com o banco de dados.

Um termo técnico que resume bem essa dinâmica é o `modelo cliente-servidor`, onde:

- `cliente`: é o software (ou parte dele) que estará interagindo diretamente com o usuário a partir de uma interface gráfica e respectiva `lógica de apresentação` e, quando necessário, envia requisições ao `servidor`.
- `servidor`: é o software (ou parte dele) que estará em execução normalmente em uma máquina poderosa, a qual é capaz de gerenciar recursos compartilhados e atende às solicitações dos `clientes`. O software no `servidor` é responsável por processar as regras de negócio e gerenciar o acesso e manipulação dos dados.
- `rede`: o meio que permite a comunicação entre `clientes` e `servidores`, normalmente a Internet, mas pode ser também uma rede local (ou intranet).
- `mecanismo de persitência de dados`: normalmente um **Sistema Gerenciador de Banco de Dados** (SGBD), onde os dados serão armazenados de forma permanente.

O fluxo de dados comum é da seguinte forma:

1. **Requisição**: o `cliente`, através da interação do usuário, envia uma solicitação de serviço ao servidor através da rede.
2. **Processamento no servidor**: o `servidor` recebe a requisição, processa a lógica de negócios e interage com o banco de dados para armazenar, recuperar, atualizar ou excluir as informações necessárias.
3. **Resposta**: o banco de dados retorna os resultados ou confirmações para o `servidor` o qual, por sua vez, envia a resposta para o `cliente`.
4. **Apresentação**: o `cliente` recebe a resposta e a apresenta ao usuário de forma apropriada.

A implementação disso se dá, mais comumente, com o padrão de arquitetura de software **MVC** (*Model, View, Controller*, ou Modelo, Visão, Controlador), onde:

- **Model**/**Modelo**: consiste na camada onde o programa vai lidar com os dados e a lógica de negócio (*back-end* e/ou *server-side*).
- **View**/**Visão**: consiste na camada onde o programa gerencia a interface com o usuário (*front-end* e/ou *client-side*).
- **Controller**/**Controlador**: consiste no intermediário entre o Modelo e a Visão.

Existem outros padrões além do MVC:

- **MVP** - *Model-View-Presenter*.
- **MVVM** - *Model-View-ViewModel*.
- **MVT** - *Model-View-Template*.
- **Flux/Redux**.

## Interação entre navegador, servidor e banco

A forma mais comum, ou **padrão**, de comunicação entre front-end e back-end é através de **requisições HTTP**.

Isso pode ser feito através de alguma biblioteca ou módulo nativo de uma linguagem de programação, ou através de alguma biblioteca feita por terceiros. Neste caso é bastante popular o uso de `APIs RESTful`.

### REST

`REST` significa *Representational State Transfer*, Transferência de Estado Representacional em tradução livre, e consiste em uma **arquitetura de software que impõe condições sobre como uma API deve funcionar**. Ou seja, `APIs RESTful` são aquelas que seguem o estilo de arquitetura REST. Alguens de seus princípios são:

- **Interface uniforme**: o servidor transfere informações em um formato padrão, o que pode ser diferente da representação interna. Por exemplo, internamente um dado é armazenado como texto, mas é enviado em formato HTML. Outros formatos bastante utilizados são JSON, XML e mais recentemente, YAML. A interface uniforme impõe quatro restrições arquitetônicas:
  1. As solicitações devem identificar recursos. Elas fazem isso usando um identificador de recurso uniforme.
  2. Os clientes têm informações suficientes na representação do recurso para modificar ou excluir o recurso caso queiram. O servidor atende a essa condição enviando metadados que descrevem melhor o recurso.
  3. Os clientes recebem informações sobre como processar ainda mais a representação. O servidor faz isso enviando mensagens autodescritivas que contêm metadados sobre como o cliente pode usá-los melhor.
  4. Os clientes recebem informações sobre todos os outros recursos relacionados de que precisam para concluir uma tarefa. O servidor faz isso enviando hiperlinks na representação para que os clientes possam descobrir dinamicamente mais recursos.
- **Ausência de estado** (*stateless*): refere-se a um método de comunicação no qual o servidor completa cada solicitação do cliente independentemente de todas as solicitações anteriores. Os clientes podem solicitar recursos em qualquer ordem, e cada solicitação é sem estado ou isolada de outras solicitações. Isso implica que o servidor possa entender completamente e atender à solicitação todas as vezes.
- **Sistema em camadas**: o cliente pode se conectar a outros intermediários autorizados entre o cliente e o servidor e ainda receber respostas do servidor. Os servidores também podem passar solicitações para outros servidores. Essas camadas permanecem invisíveis para o cliente.
- **Capacidade de armazenamento**: permite o armazenamento em cache para melhorar o tempo de resposta do servidor.
- **Código sob demanda**: os servidores podem estender ou personalizar temporariamente a funcionalidade do cliente, transferindo o código de programação de software para o cliente. Por exemplo, o navegador pode destacar imediatamente os erros cometidos por um usuário em um formulário.

#### Conteúdo de uma solicitação do cliente da API RESTful

As APIs RESTful exigem que as solicitações contenham os seguintes componentes principais:

- **Identificador de recurso exclusivo**: ou seja, a URL.
- **Método**: o método HTTP (GET, POST, etc.).
- **Cabeçalhos HTTP**: os metadados presentes nas requisições e respostas do HTTP.

#### Autenticação

Um serviço da Web RESTful deve autenticar solicitações antes de enviar uma resposta. A API RESTful tem quatro métodos de autenticação comuns:

- Autenticação de HTTP.
- Chaves de API.
- OAuth.

#### Conteúdo de uma resposta do servidor da API RESTful

Os princípios da REST exigem que a resposta do servidor contenha os seguintes componentes principais:

- **Linha de status**: o código retornado pelo HTTP (ex.: 200, 404, etc.).
- **Corpo da mensagem**.
- **Cabeçalhos**.

### Rotas no back-end

As rotas são responsáveis por mapear as requisições recebidas do frontend para as funções e métodos adequados. Consiste em uma URL que será mapeada. Por exemplo `/get_users` pode ser mapeada para uma função que busca uma lista de usuários do banco de dados.

No `front-end` a requisição seria da seguinte forma: `GET /get_users`.

### Frameworks

Frameworks podem ser utilizados para a criação de uma RESTful API, ou podem ser RESTful nativamente, ou ainda podem ter versões RESTful. Exemplos em Python:

- Python
  - `Flask-RESTful` ou  `Flask-RESTx`.
  - `Django REST Framework`(**DRF**).
  - `FastAPI`.
- JavaScript (Node.js)
  - `Express.js`.
  - `Fastify`.
- Java
  - `Spring Boot`.

## Exemplos

O exemplo a seguir foi retirado da página do [Flask-RESTful/Quickstart](https://flask-restful.readthedocs.io/en/latest/quickstart.html).

```python
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
```


<!--
PESQUISA NO GOOLE: Exemplos de fluxos de requisições com dados.
-->