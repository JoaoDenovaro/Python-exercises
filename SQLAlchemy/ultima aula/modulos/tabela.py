import sqlalchemy as sa
import datetime as dt
from modulos.conexao import conecta_bd
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__: str = 'products'

    id: int = sa.column(sa.Integer, primary_key=True, autoincrement=True)
    creation_date: dt = sa.Column(sa.DateTime, default=dt.now)
    name: str = sa.Column(sa.String(30), nullable=False)
    color: str = sa.Column(sa.String(20), nullable=False)
    price: float = sa.Column(sa.DECIMAL(6,2), nullable=False)
    quantity: int = sa.Column(sa.Integer, nullable=False)
    description: str = sa.Column(sa.String(50))
    def __repr__(self) -> str:
        '''Retorna a representação do objeto'''
        return f'<{self.name} {self.color}>'

def create_table():
    try:
        Base.metadata.create_all(conecta_bd)
    except Exception as err:
        raise err('Erro ao criar tabela')
    else:
        print('Tabela criada!!')
