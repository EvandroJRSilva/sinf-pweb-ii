# Aula 11

## FastAPI

É um framework web moderno e rápido (i.e., de alta performance) para a construção de APIs com Python baseado em **dicas de tipo** (*type hints*) padrões do Python.

Principais características (do site oficial):

- **Rápido**: alta performance, a par com **NodeJS** e **Go** (um dos frameworks Python mais rápidos).
- **Rápido de *codar***.
- **Menos bugs**.
- **Intuitivo**.
- **Fácil**: projetado para ser fácil de aprender e usar.
- **Pequeno**: minimize a duplicação de código.
- **Robusto**: obtenha código pronto para produção. Com documentação interativa automática.
- **Baseado em padrões**: Baseado em (e totalmente compatível com) padrões abertas para APIs: OpenAPI e JSON Schema.

### *Type hints*

É uma sintaxe formal para a declaração do tipo de dado esperado para variáveis, parâmetros de funções e retornos. Exemplos:

```python
# Variável
idade: int = 25

# Função
def saudar(nome: str) -> str:
    return nome + " está saudando a mandioca"
```

Exemplo com tipos mais complexos:

```python
from typing import List, Set, Dict

def processar_valores(valores: List[int]) -> Set[str]:
    ...

def contar_frequencia(palavras: List[str]) -> Dict[str, int]:
    ...
```

Mais informações na [documentação oficial](https://docs.python.org/pt-br/3.14/library/typing.html).

### Instalação

Para instalar o **FastAPI** digite no terminal (de preferência com um ambiente virtual ativado):

```
pip install fastapi[standard]
```

### Primeiros passos

Após instalar vamos fazer um primeiro exemplo bem simples, começando com um arquivo [`main.py`](./exemplo1/main.py). Após salvar o arquivo, no terminal pode ser executado o seguinte comando (na pasta onde está o arquivo `main.py`):

```
fastapi dev
```

Veja os links [localhost:8000](http://127.0.0.1:8000), [documentação](http://127.0.0.1:8000/docs) e também uma [página alternativa de documentação](http://127.0.0.1:8000/redoc).