from fastapi import FastAPI

app = FastAPI()


# EXEMPLO 1 ---------------------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"mensagem": "Olá Mundo Cruel!"}
#--------------------------------------------------------------------------------------------------

# EXEMPLO 2 - Path Parameters ---------------------------------------------------------------------
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
#--------------------------------------------------------------------------------------------------

# EXEMPLO 3 - Path & Query Parameters -------------------------------------------------------------
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"descrição": "Este é um item maravilhoso com uma longa descrição"})
    return item
#--------------------------------------------------------------------------------------------------