from sqlalchemy.schema import Column
from sqlalchemy.types import String , Integer
from database import Base

class ProdutoInfo(Base):
    __tablename__="produto"
    id=Column(Integer, primary_key=True, index=True)
    nome= Column(String)
    tipo=Column(String)
    quantidade=Column(Integer)