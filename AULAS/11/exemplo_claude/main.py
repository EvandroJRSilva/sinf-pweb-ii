"""
=============================================================
  CONTROLE DE ESTOQUE - Exemplo Didático com FastAPI
=============================================================
  Tópicos abordados (tutorial oficial fastapi.tiangolo.com):
  - Path Parameters
  - Query Parameters
  - Request Body
  - Query Parameter Models
  - String Validations
  - Numeric Validations
  - Body - Multiple Parameters
  - Body - Fields
  - Response Model
  - Extra Data Types
  - Cookie Parameters
  - Header Parameters
  - Header Parameter Models
=============================================================
"""

from fastapi import FastAPI, Path, Query, Body, Cookie, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(title="Controle de Estoque", version="1.0.0")

# Liberando CORS para o front-end funcionar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------
# Banco de dados simulado (só um dicionário mesmo!)
# -------------------------------------------------------
produtos = {
    1: {
        "id": 1,
        "nome": "Caneta Azul",
        "categoria": "papelaria",
        "quantidade": 150,
        "preco": 2.50,
        "criado_em": datetime(2024, 1, 10),
    },
    2: {
        "id": 2,
        "nome": "Caderno A4",
        "categoria": "papelaria",
        "quantidade": 40,
        "preco": 18.90,
        "criado_em": datetime(2024, 2, 5),
    },
    3: {
        "id": 3,
        "nome": "Mouse USB",
        "categoria": "informatica",
        "quantidade": 12,
        "preco": 79.90,
        "criado_em": datetime(2024, 3, 20),
    },
}
proximo_id = 4  # controla o próximo ID disponível


# -------------------------------------------------------
# Enumeração de categorias (usado em Path/Query params)
# -------------------------------------------------------
class Categoria(str, Enum):
    papelaria = "papelaria"
    informatica = "informatica"
    limpeza = "limpeza"
    outros = "outros"


# ===============================================================
# TÓPICO: Request Body + Body - Fields
# Modelo Pydantic com Field() para validações e documentação
# ===============================================================
class Produto(BaseModel):
    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nome do produto",
        examples=["Caneta Azul"],
    )
    categoria: Categoria = Field(..., description="Categoria do produto")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque")
    preco: float = Field(..., gt=0, description="Preço unitário (R$)")


# ===============================================================
# TÓPICO: Response Model
# Modelo de resposta (inclui campos gerados pelo servidor)
# ===============================================================
class ProdutoResposta(BaseModel):
    id: int
    nome: str
    categoria: str
    quantidade: int
    preco: float
    criado_em: datetime  # Extra Data Types: datetime


# ===============================================================
# TÓPICO: Query Parameter Models
# Agrupa vários query params em um único modelo Pydantic
# ===============================================================
class FiltrosProduto(BaseModel):
    categoria: Optional[Categoria] = None
    preco_min: Optional[float] = Field(None, ge=0)
    preco_max: Optional[float] = Field(None, ge=0)
    em_estoque: bool = True  # só mostra produtos com quantidade > 0


# ===============================================================
# TÓPICO: Header Parameter Models
# Agrupa headers esperados em um modelo Pydantic
# ===============================================================
class HeadersApp(BaseModel):
    model_config = {"populate_by_name": True}

    x_app_versao: Optional[str] = Field(None, alias="x-app-versao")
    x_app_cliente: Optional[str] = Field(None, alias="x-app-cliente")


# ---------------------------------------------------------------
# ROTA: Listar todos os produtos
# ---------------------------------------------------------------
@app.get("/produtos", response_model=list[ProdutoResposta])
def listar_produtos(
    # ============================================================
    # TÓPICO: Query Parameter Models
    # Todos os filtros vêm de um único modelo Pydantic
    # Equivale a ter cada campo como parâmetro separado
    # ============================================================
    filtros: FiltrosProduto = Query(),

    # ============================================================
    # TÓPICO: Query Parameters com validação (String Validations)
    # ============================================================
    busca: Optional[str] = Query(
        None,
        min_length=2,
        description="Busca por nome do produto",
    ),

    # ============================================================
    # TÓPICO: Numeric Validations em Query Params
    # ============================================================
    limite: int = Query(10, ge=1, le=100, description="Máx. de itens retornados"),
    pagina: int = Query(1, ge=1, description="Número da página"),

    # ============================================================
    # TÓPICO: Cookie Parameters
    # Lê um cookie chamado "usuario_id" (enviado pelo navegador)
    # ============================================================
    usuario_id: Optional[str] = Cookie(None),

    # ============================================================
    # TÓPICO: Header Parameters
    # Lê o header "x-idioma" da requisição
    # ============================================================
    x_idioma: Optional[str] = Header(None),

    # ============================================================
    # TÓPICO: Header Parameter Models
    # Vários headers agrupados em um modelo
    # ============================================================
    headers_app: HeadersApp = Header(),
):
    print(f"Usuário (cookie): {usuario_id}")
    print(f"Idioma (header): {x_idioma}")
    print(f"Versão do app (header model): {headers_app.x_app_versao}")
    print(f"Cliente do app (header model): {headers_app.x_app_cliente}")

    resultado = list(produtos.values())

    # Aplica filtros do Query Parameter Model
    if filtros.categoria:
        resultado = [p for p in resultado if p["categoria"] == filtros.categoria]
    if filtros.preco_min is not None:
        resultado = [p for p in resultado if p["preco"] >= filtros.preco_min]
    if filtros.preco_max is not None:
        resultado = [p for p in resultado if p["preco"] <= filtros.preco_max]
    if filtros.em_estoque:
        resultado = [p for p in resultado if p["quantidade"] > 0]

    # Aplica busca por nome
    if busca:
        resultado = [
            p for p in resultado if busca.lower() in p["nome"].lower()
        ]

    # Paginação simples
    inicio = (pagina - 1) * limite
    return resultado[inicio: inicio + limite]


# ---------------------------------------------------------------
# ROTA: Buscar produto por ID
# ---------------------------------------------------------------
@app.get("/produtos/{produto_id}", response_model=ProdutoResposta)
def buscar_produto(
    # ============================================================
    # TÓPICO: Path Parameters com validação (Numeric Validations)
    # produto_id é extraído da URL e validado com Path()
    # ============================================================
    produto_id: int = Path(
        ...,
        ge=1,
        description="ID do produto (deve ser >= 1)",
    ),
):
    if produto_id not in produtos:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtos[produto_id]


# ---------------------------------------------------------------
# ROTA: Buscar produtos por categoria
# ---------------------------------------------------------------
@app.get("/produtos/categoria/{categoria}", response_model=list[ProdutoResposta])
def buscar_por_categoria(
    # ============================================================
    # TÓPICO: Path Parameters com Enum
    # O FastAPI valida automaticamente se o valor está no Enum
    # ============================================================
    categoria: Categoria = Path(..., description="Categoria dos produtos"),

    # ============================================================
    # TÓPICO: Query Parameters
    # Parâmetros opcionais passados na URL (?ordenar_por=preco)
    # ============================================================
    ordenar_por: Optional[str] = Query(
        None,
        description="Campo para ordenar (nome, preco, quantidade)",
    ),
    ordem_desc: bool = Query(False, description="Ordenação decrescente?"),
):
    resultado = [p for p in produtos.values() if p["categoria"] == categoria]

    if ordenar_por in ("nome", "preco", "quantidade"):
        resultado.sort(key=lambda p: p[ordenar_por], reverse=ordem_desc)

    return resultado


# ---------------------------------------------------------------
# ROTA: Criar novo produto
# ---------------------------------------------------------------
@app.post("/produtos", response_model=ProdutoResposta, status_code=201)
def criar_produto(
    # ============================================================
    # TÓPICO: Request Body
    # O FastAPI lê o JSON do corpo da requisição e valida com Pydantic
    # ============================================================
    produto: Produto,
):
    global proximo_id
    novo = {
        "id": proximo_id,
        "nome": produto.nome,
        "categoria": produto.categoria,
        "quantidade": produto.quantidade,
        "preco": produto.preco,
        "criado_em": datetime.now(),  # Extra Data Types: datetime
    }
    produtos[proximo_id] = novo
    proximo_id += 1
    return novo


# ---------------------------------------------------------------
# ROTA: Atualizar produto
# ---------------------------------------------------------------
@app.put("/produtos/{produto_id}", response_model=ProdutoResposta)
def atualizar_produto(
    # ============================================================
    # TÓPICO: Body - Multiple Parameters
    # Path param + Body param juntos na mesma função
    # ============================================================
    produto_id: int = Path(..., ge=1),
    produto: Produto = Body(...),
):
    if produto_id not in produtos:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produtos[produto_id].update({
        "nome": produto.nome,
        "categoria": produto.categoria,
        "quantidade": produto.quantidade,
        "preco": produto.preco,
    })
    return produtos[produto_id]


# ---------------------------------------------------------------
# ROTA: Ajustar quantidade (entrada/saída de estoque)
# ---------------------------------------------------------------
@app.patch("/produtos/{produto_id}/estoque")
def ajustar_estoque(
    # ============================================================
    # TÓPICO: Body - Multiple Parameters
    # Combina Path param com um campo Body embutido (Body(...))
    # ============================================================
    produto_id: int = Path(..., ge=1),

    # Numeric Validations: quantidade pode ser negativa (saída) ou positiva (entrada)
    ajuste: int = Body(..., description="Positivo = entrada, Negativo = saída"),
):
    if produto_id not in produtos:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    nova_qtd = produtos[produto_id]["quantidade"] + ajuste
    if nova_qtd < 0:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Estoque não pode ficar negativo")

    produtos[produto_id]["quantidade"] = nova_qtd
    return {
        "mensagem": "Estoque atualizado",
        "produto_id": produto_id,
        "quantidade_anterior": produtos[produto_id]["quantidade"] - ajuste,
        "quantidade_atual": nova_qtd,
    }


# ---------------------------------------------------------------
# ROTA: Deletar produto
# ---------------------------------------------------------------
@app.delete("/produtos/{produto_id}", status_code=204)
def deletar_produto(
    produto_id: int = Path(..., ge=1),
):
    if produto_id not in produtos:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    del produtos[produto_id]
