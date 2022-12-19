from modulos.menu import menu_principal
from time import sleep
from modulos.tabela import create_table
from modulos.acoes import *
import sys

if __name__ == '__main__':
    while True:
        match menu_principal():
            case 1:
                new_product()
            case 5:
                create_table()
                sleep(1)
            case 6:
                print('Encerrando o programa...')
                sleep(2)
                sys.exit('Programa encerrado')
            case _:
                print('Opção inválida')
                sleep(1)
        