
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv('./env')

try:
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        passwd=os.getenv('PASSWD'),
        db=os.getenv('DB')
    )
except Exception as err:
    raise err('deu ruim')
#CRIAÇÃO DO CURSOR, PARA FAZER AS OPERAÇÕES
else:
    cursor = conn.cursor()


def adicionar3():
    for i in range (1, 4):
        query = 'SELECT * FROM USERS'
        cursor.execute(query)
        resultado = cursor.fetchall()
        users = [user[0] for user in resultado]
        
        novo_login = input(f'Login #{i}: ').lower()
        novo_nome = input(f'Nome #{i}: ').title()

        if novo_login not in users:
            query_insert = f'INSERT INTO USERS VALUES ("{novo_login}", "{novo_nome}")'
            cursor.execute(query_insert)
            conn.commit()
            print(f'{novo_nome} foi cadastrado com sucesso!')
        else:
            print('Login ja existe :(')

adicionar3()