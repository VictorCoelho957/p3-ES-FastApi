from typing import List
from sqlalchemy.orm import Session
from   exceptions import ProdutoInfoInfoAlreadyExistError, ProdutoInfoNotFoundError

from models import ProdutoInfo
from schemas import CreateAndUpdateProduto

def get_all_produtos(session: Session, limit: int, offset: int) -> List[ProdutoInfo]:
    return session.query(ProdutoInfo).offset(offset).limit(limit).all()

def get_produto_info_by_id(session: Session, _id: int) -> ProdutoInfo:
    produto_info = session.query(ProdutoInfo).get(_id)

    if produto_info is None:
        raise ProdutoInfoNotFoundError

    return produto_info


# Function to add a new produto info to the database
def create_produto(session: Session, produto_info: CreateAndUpdateProduto) -> ProdutoInfo:
    produto_details = session.query(ProdutoInfo).filter(ProdutoInfo.nome == produto_info.nome, ProdutoInfo.tipo == produto_info.tipo).first()
    if produto_details is not None:
        raise ProdutoInfoInfoAlreadyExistError

    new_produto_info = ProdutoInfo(**produto_info.dict())
    session.add(new_produto_info)
    session.commit()
    session.refresh(new_produto_info)
    return new_produto_info


# Function to update details of the produto
def update_produto_info(session: Session, _id: int, info_update: CreateAndUpdateProduto) -> ProdutoInfo:
    produto_info = get_produto_info_by_id(session, _id)

    if produto_info is None:
        raise ProdutoInfoNotFoundError

    produto_info.nome = info_update.nome
    produto_info.tipo = info_update.tipo
    produto_info.quantiadade = info_update.quantidade
    

    session.commit()
    session.refresh(produto_info)

    return produto_info


# Function to delete a produto info from the db
def delete_produto_info(session: Session, _id: int):
    produto_info = get_produto_info_by_id(session, _id)

    if produto_info is None:
        raise ProdutoInfoNotFoundError

    session.delete(produto_info)
    session.commit()

    return
