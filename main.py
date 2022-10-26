from controllers.User import *
from utils.statistics import main_statistics


menu = {
    'Mostrar todos os usuários': find_all,
    'Encontrar um usuário pelo nome': find_by_name,
    'Cria novo usuário': create,
    'Deletar usuário existente': delete,
    'Atualizar dado de usuário': update,
    'Ver estatísticas': main_statistics,

}


while True:
    print('BEM VINDO AO SISTEMA DE GERENCIAMENTO DE USUÁRIOS')
    try:
        for pos, op in enumerate(menu.keys()):
            print(f'{pos + 1}: {op}')
        print(f'{len(menu) + 1}: Sair')

        choice = input('O que deseja fazer? ')

        if not int(choice) or int(choice) not in list(range(1, len(menu) + 2)):
            raise ValueError('Digite uma opção válida!')

        if int(choice) in list(range(1, len(menu) + 1)):

            for pos, op in enumerate(menu.values()):
                if pos + 1 == int(choice):
                    op()
        else:
            print('FIM DO PROGRAMA')
            break

    except Exception as err:
        print(err)


