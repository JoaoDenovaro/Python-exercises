import sqlalchemy as sqla
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

# Conectando ao banco de dados
engine = create_engine(url="mysql+mysqlconnector://root@localhost:3306/INFINITY", echo=True)

# Declarando o mapeamento
Base = declarative_base()

# Criando a tabela
class Product(Base):
    __tablename__: str = 'products'

    id: int = sqla.Column(sqla.Integer, primary_key=True)
    name: str = sqla.Column(sqla.String(30), nullable=False)
    color: str = sqla.Column(sqla.String(20), nullable=False)
    price: str = sqla.Column(sqla.DECIMAL(6,2), nullable=False)
    description: str = sqla.Column(sqla.String(50))

    def __repr__(self) -> str:
        return f'<Product: {self.name} {self.color}>'

# Crianda tabela no banco de dados
Base.metadata.create_all(engine)

# =========================
prd = Product(
    name = 'Caneta',
    color='Azul',
    price=98.50,
    description='Camiseta de algodão'
)

# Abrindo uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionando objetos (INSERT)
# session.add(prd)
# session.commit()

# Adicionando vários objetos
# session.add_all([
#     Product(
#         name='Short',
#         color='Jeans',
#         price=58,
#         description='Short Jeans'
#     ),
#     Product(
#         name='Kalsa',
#         color='Preta',
#         price=69,
#         description='Kalsa moletom preta uwu'
#     )
# ])
# session.commit()

# Aplicando queries!!
# query_prd = session.query(Product)
# for dados in query_prd:
#     print(f'{dados.name} - R${dados.price}')

# query_prd2 = session.query(Product).filter_by(name='Caneta').first()
# print(f'{query_prd2.name} - R${query_prd2.price}')

# Atualizando dados
# query_prd = session.query(Product).filter_by(name='Kalsa').first()
# query_prd.price = 98.99
# session.commit()

# Apagando dados
# prd = session.query(Product).filter_by(name='Short').first()
# session.delete(prd)
# session.commit()