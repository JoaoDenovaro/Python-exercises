from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv('./modulos/env')

def conecta_bd():
    try:
        engine = create_engine(
            url=os.getenv('STRCNX'),
            echo=False
        )
    except Exception as err:
        raise err('Erro ao se conectar')
    else:
        return type(engine)