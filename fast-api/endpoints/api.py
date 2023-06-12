# api.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_produtos, create_produto, get_produto_info_by_id, update_produto_info, delete_produto_info
from database import get_db
from exceptions import ProdutoInfoException
from schemas import Produto, CreateAndUpdateProduto, PaginatedProdutoInfo

router = APIRouter()


# Example of Class based view
@cbv(router)
class Produto:
    session: Session = Depends(get_db)

    # API to get the list of produto  info
    @router.get("/produtos", response_model=PaginatedProdutoInfo)
    def list_produtos(self, limit: int = 10, offset: int = 0):

        produtos_list = get_all_produtos(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": produtos_list}

        return response

    # API endpoint to add a produto info to the database
    @router.post("produtos")
    def add_produtos(self, produto_info: CreateAndUpdateProduto):

        try:
            produto_info = create_produto(self.session, produto_info)
            return produto_info
        except ProdutoInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular produto
@router.get("/produtos/{produtos_id}", response_model=Produto)
def get_produto_info(produto_id: int, session: Session = Depends(get_db)):

    try:
        produto_info = get_produto_info_by_id(session, produto_id)
        return produto_info
    except ProdutoInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing produto info
@router.put("/produtos/{produto_id}", response_model=Produto)
def update_car(produto_id: int, new_info: CreateAndUpdateProduto, session: Session = Depends(get_db)):

    try:
        produto_info = update_produto_info(session, produto_id, new_info)
        return produto_info
    except ProdutoInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a produto info from the data base
@router.delete("/produtoss/{produtos_id}")
def delete_car(produto_id: int, session: Session = Depends(get_db)):

    try:
        return delete_produto_info(session, produto_id)
    except ProdutoInfoException as cie:
        raise HTTPException(**cie.__dict__)
