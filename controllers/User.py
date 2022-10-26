import csv

from prettytable import PrettyTable
from utils.clear_screen import clear_screen
from utils.validations import * #validate_cpf, validate_email, validate_phone, validate_birthdate


field_names_table = ['Nome', 'Gênero', 'Email', 'Telefone', 'CPF', 'Data de Nascimento']


def find_all():
    clear_screen()
    try:
        with open('database/users.csv', 'r', encoding='utf-8') as file:
            users = csv.DictReader(file)

            table = PrettyTable()
            table.title = 'USUÁRIOS CADASTRADOS'
            table.field_names = field_names_table

            for user in users:
                table.add_row(user.values())

            print(table)

        input('Tecle Enter para retornar.')
    except Exception:
        print('Erro ao ler arquivo')



def find_by_name():
    clear_screen()
    found = False
    with open('database/users.csv', 'r', encoding='utf-8') as file:
        name = input('Digite o nome: ')

        users = csv.DictReader(file)

        table = PrettyTable()
        table.title = 'USUÁRIO ENCONTRADO'
        table.field_names = field_names_table

        for user in users:
            if name.lower() in user['name'].lower():
                table.add_row(user.values())
                found = True

        if found:
            print(table)
        else:
            print(f'Usuário {name} não encontrado!')

    input('Tecle Enter para retornar.')


def create(new_user=None):
    new_user = {'name': '', 'gender': '', 'email': '', 'phone': '', 'cpf': '', 'birthdate': ''}

    is_create = False

    while not is_create:
        print('CRIAÇÃO DE NOVO USUÁRIO')

        new_user['name'] = validate_name()
        new_user['gender'] = validate_gender()
        new_user['email'] = validate_email()
        new_user['phone'] = validate_phone()
        new_user['cpf'] = validate_cpf()
        new_user['birthdate'] = validate_birthdate()

        clear_screen()

        table = PrettyTable()
        table.title = 'USUÁRIO CRIADO'
        table.field_names = field_names_table
        table.add_row(new_user.values())

        print(table)

        resp = ' '

        while resp not in 'SN':
            resp = input('As informações conferem? ').strip().upper()[0]

            if resp == 'S':
                with open('database/users.csv', 'a', encoding='utf-8', newline='') as file:
                    fieldnames = new_user.keys()
                    writer = csv.DictWriter(file, fieldnames)

                    writer.writerow(new_user)
                    print('Cadastro realizado!')

                    pass

                is_create = True


def delete():
    new_list = []
    clear_screen()
    exist = False

    with open('database/users.csv', 'r', encoding='utf-8') as read:
        query = input('Digite o CPF do usuário a ser excluído: ')

        users = csv.DictReader(read)
        table = PrettyTable()
        table.title = 'USUÁRIOS ENCONTRADOS'
        table.field_names = field_names_table
        try:
            for user in users:
                new_list.append(user)
                if query == user['cpf']:
                    exist = True
                    del_user = user.values()
                    table.add_row(del_user)
                    pos = len(new_list)
            if exist:
                print(table)

                conf = ' '

                while conf not in 'SN':
                    conf = input('As informações conferem? ').strip().upper()[0]

                    if conf == 'S':
                        new_list.pop(pos - 1)
                        with open('database/users.csv', 'w', encoding='utf-8', newline='') as write:
                            fieldnames = new_list[0].keys()
                            writer = csv.DictWriter(write, fieldnames)
                            writer.writeheader()

                            for i in new_list:
                                writer.writerow(i)

                            print('Exclusão realizada com sucesso!')
                            table = PrettyTable()
                            table.title = 'USUÁRIO EXCLUÍDO'
                            table.field_names = field_names_table
                            table.add_row(del_user)
                            print(table)
            else:
                print(f'CPF {query} não encontrado!')
        except KeyError as err:
            print(err)
    input('Tecle Enter para retornar.')


def update():
    new_update_list = []
    exists = False

    user_template = {'name': 'Nome',
                 'gender': 'Gênero',
                 'email': 'Email',
                 'phone': 'Telefone',
                 'cpf': 'CPF',
                 'birthdate': 'Data de Nascimento'
    }

    clear_screen()

    with open('database/users.csv', 'r', encoding='utf-8') as file:
        query = input('Digite o CPF do usuário a ser atualizado: ')

        users = csv.DictReader(file)
        table = PrettyTable()
        table.title = 'USUÁRIO ENCONTRADO'
        table.field_names = field_names_table

        try:
            for user in users:
                new_update_list.append(user)
                if query == user['cpf']:
                    user_data = user
                    user_to_update = user_data.values()
                    table.add_row(list(user.values()))
                    indice = len(new_update_list)
                    exists = True
            if exists:

                print(table)

                try:
                    for pos, selecao in enumerate(user_template.values()):
                        print(f'{pos + 1}: {selecao}')
                    print(f'{len(user_template.values()) + 1}: Cancelar')

                    choice = input('Qual dado deseja atualizar? ')

                    if not int(choice) or int(choice) not in list(range(1, len(user_template.values()) + 2)):
                        raise ValueError('Digite uma opção válida!')

                    if int(choice) in list(range(1, len(user_template.values()) + 1)):
                        for pos, sel in enumerate(user_template.keys()):
                            if pos + 1 == int(choice):
                                print(f'Atualizando {sel}')

                                try:
                                    if pos == 0:
                                        user_data['name'] = validate_name()
                                    elif pos == 1:
                                        user_data['gender'] = validate_gender()
                                    elif pos == 2:
                                        user_data['email'] = validate_email()
                                    elif pos == 3:
                                        user_data['phone']: validate_phone()
                                    elif pos == 4:
                                        user_data['cpf']: validate_cpf()
                                    elif pos == 5:
                                        user_data['birthdate'] = validate_birthdate()

                                except Exception:
                                    print(Exception)
                        conf = ' '

                        while conf not in 'SN':
                            with open('database/users.csv', 'r', encoding='utf-8') as file:
                                users = csv.DictReader(file)
                                table = PrettyTable()
                                table.title = 'ATUALIZAÇÃO DE USUÁRIO'
                                table.field_names = field_names_table

                                try:
                                    for user in users:
                                        if query == user['cpf']:
                                            user_to_update = user.values()
                                except Exception:
                                    print('Não encontrado na escrita')

                            table = PrettyTable()
                            table.title = 'DADO ANTES E APÓS ALTERAÇÃO'
                            table.field_names = field_names_table
                            table.add_row(user_to_update)
                            table.add_row(list(user_data.values()))
                            print(table)
                            conf = input('As informações conferem? ').strip().upper()[0]

                            if conf == 'S':
                                new_update_list[indice - 1] = user_data
                                with open('database/users.csv', 'w', encoding='utf-8', newline='') as writer_update:
                                    users = csv.DictReader(writer_update)
                                    fieldnames = new_update_list[0].keys()
                                    writer = csv.DictWriter(writer_update, fieldnames)
                                    writer.writeheader()
                                    for i in new_update_list:
                                        writer.writerow(i)
                                    print('Alteração feita com sucesso!')

                    else:
                        print('Operação cancelada! Retorne à tela principal.')

                except Exception as err:
                    print(err)

            else:
                print(f'CPF {query} não encontrado!')
        except KeyError as err:
            print(err)
    input('Tecle Enter para retornar.')
