'''Este é o modulo do menu'''

import os
import platform

def limpa_tela():
    '''
    Limpa a tela do terminal, independente do Sistema Operacional
    return:
        None
    '''

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu_principal() -> int:
    '''
    Exibe o menu principal na tela
    
    return:
        None
    '''

    limpa_tela()
    print(f'''
        {"MENU PRINCIPAL":=^30}
        1) Cadastrar Produto
        2) Atualizar Produto
        3) Remover Produto
        4) Listar Produtos
        5) Criar Tabela
        6) Sair
        ''')
    opcao = int(input('Opção: '))
    return opcao
