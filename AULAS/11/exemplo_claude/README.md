# Controle de Estoque — Exemplo Didático FastAPI

Projeto de exemplo para sala de aula cobrindo os tópicos do tutorial oficial
do FastAPI (https://fastapi.tiangolo.com/tutorial/), de **Path Parameters** até
**Header Parameter Models**.

---

## Tópicos Abordados

| Tópico | Onde aparece |
|---|---|
| Path Parameters | `GET /produtos/{produto_id}`, `PATCH /produtos/{id}/estoque` |
| Query Parameters | `GET /produtos` (busca, limite, pagina, ordenar_por) |
| Request Body | `POST /produtos` |
| Query Parameter Models | `FiltrosProduto` em `GET /produtos` |
| String Validations | `busca: str = Query(min_length=2)` |
| Numeric Validations | `produto_id: int = Path(ge=1)`, `quantidade: int = Field(ge=0)` |
| Body - Multiple Parameters | `PUT /produtos/{id}` (Path + Body juntos) |
| Body - Fields | Modelo `Produto` com `Field(...)` |
| Response Model | `response_model=ProdutoResposta` em todas as rotas |
| Extra Data Types | `criado_em: datetime` |
| Cookie Parameters | `usuario_id: str = Cookie(None)` |
| Header Parameters | `x_idioma: str = Header(None)` |
| Header Parameter Models | `HeadersApp` em `GET /produtos` |

---

## Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar o servidor

```bash
uvicorn main:app --reload
```

O servidor sobe em: http://localhost:8000

### 3. Abrir o front-end

Abra o arquivo `index.html` no navegador.
> Recomendado: use a extensão **Live Server** do VS Code ou qualquer servidor estático.

### 4. Documentação automática (Swagger UI)

Acesse: http://localhost:8000/docs

---

## Estrutura do Projeto

```
estoque/
├── main.py           # Backend FastAPI (comentado por tópico)
├── index.html        # Front-end (HTML + CSS + JS em um único arquivo)
├── requirements.txt  # Dependências Python
└── README.md
```
