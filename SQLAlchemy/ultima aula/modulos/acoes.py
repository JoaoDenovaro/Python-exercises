import sqlalchemy as sqla
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from modulos.tabela import Product
from modulos.conexao import conecta_bd


def start_session():
    Session = sessionmaker(bind=conecta_bd())
    session = Session()

def new_product():
    start_session()
    prd = Product(
        name = input('Nome do produto: '),
        color = input('Cor do produto: '),
        price = input('Preço do produto: '),
        quantity = input('Quantidade do produto: '),
        description= input('Descrição do produto')
    )
    session.add(prd)
    session.commit()
