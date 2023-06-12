from pydantic import BaseModel
from models import FuelType
from typing import Optional, List

# TO support creation and update APIs

class CreateAndUpdateProduto(BaseModel):
    nome: str
    tipo: str
    quantidade: int

# TO support list and get APIs

class Produto(CreateAndUpdateProduto):
    id: int

    class Config:
        orm_mode = True

# To support list Produtos API

class PaginaTedProdutoInfo(BaseModel):
    limit: int
    offset: int
    data: List[Produto]
