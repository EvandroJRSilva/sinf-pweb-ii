from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
import uvicorn

app = FastAPI(title="Controle de Estoque Simples - Exemplo Didático")

# Liberando CORS para o front-end funcionar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====================== BANCO DE DADOS SIMULADO ======================
estoque = [
    {"id": 1, "nome": "Notebook Dell", "quantidade": 15, "preco": 3500.00},
    {"id": 2, "nome": "Mouse Logitech", "quantidade": 50, "preco": 89.90},
    {"id": 3, "nome": "Teclado Mecânico", "quantidade": 30, "preco": 299.90},
]

# ====================== MODELOS ======================
class Item(BaseModel):
    nome: str
    quantidade: int
    preco: float

class ItemResponse(BaseModel):
    id: int
    nome: str
    quantidade: int
    preco: float

# ====================== QUERY PARAMETER MODEL ======================
class FiltroEstoque(BaseModel):
    """Modelo para Query Parameters agrupados"""
    min_quantidade: Optional[int] = Field(None, ge=0, description="Quantidade mínima")
    max_preco: Optional[float] = Field(None, gt=0, description="Preço máximo")
    nome_contem: Optional[str] = Field(None, max_length=50, description="Filtro por parte do nome")


# ====================== ROTAS ======================

# --- Path Parameters ---
@app.get("/items/{item_id}")
async def ler_item_por_id(item_id: int):
    """Exemplo básico de Path Parameter"""
    for item in estoque:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")


# --- Path Parameters with Types + Numeric Validations ---
@app.get("/items/{item_id}/detalhes")
async def detalhes_item(
    item_id: int = Path(..., gt=0, title="ID do item", description="ID deve ser maior que zero")
):
    """Path Parameter com validação numérica usando Path()"""
    for item in estoque:
        if item["id"] == item_id:
            return {"item": item, "mensagem": f"Detalhes do item {item_id}"}
    raise HTTPException(status_code=404, detail="Item não encontrado")


# --- Query Parameters simples ---
@app.get("/items/")
async def listar_itens(
    skip: int = 0,
    limit: int = 10
):
    """Exemplo de Query Parameters (padrão)"""
    return estoque[skip : skip + limit]


# --- Query Parameters com Validações de String ---
@app.get("/buscar/")
async def buscar_itens(
    q: Optional[str] = Query(
        None,
        min_length=2,
        max_length=50,
        title="Termo de busca",
        description="Busca pelo nome do produto"
    ),
    ordenar_por: str = Query("nome", regex="^(nome|quantidade|preco)$")
):
    """Query Parameters com validações de string"""
    resultado = estoque.copy()

    if q:
        resultado = [item for item in resultado if q.lower() in item["nome"].lower()]

    if ordenar_por == "quantidade":
        resultado.sort(key=lambda x: x["quantidade"])
    elif ordenar_por == "preco":
        resultado.sort(key=lambda x: x["preco"])

    return {"resultados": resultado, "total": len(resultado)}


# --- Query Parameter Models ---
@app.get("/filtro/")
async def filtrar_estoque(filter_query: FiltroEstoque = Query()):
    """Usando Query Parameter Model (Pydantic)"""
    resultado = estoque.copy()

    if filter_query.min_quantidade is not None:
        resultado = [item for item in resultado if item["quantidade"] >= filter_query.min_quantidade]

    if filter_query.max_preco is not None:
        resultado = [item for item in resultado if item["preco"] <= filter_query.max_preco]

    if filter_query.nome_contem:
        resultado = [item for item in resultado if filter_query.nome_contem.lower() in item["nome"].lower()]

    return {
        "filtro_aplicado": filter_query,
        "itens_encontrados": resultado,
        "total": len(resultado)
    }


# --- Criar item (POST simples) ---
@app.post("/items/", response_model=ItemResponse)
async def criar_item(item: Item):
    novo_id = max([i["id"] for i in estoque]) + 1 if estoque else 1
    novo_item = {"id": novo_id, **item.dict()}
    estoque.append(novo_item)
    return novo_item


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)