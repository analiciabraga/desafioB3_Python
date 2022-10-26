import re

from validate_docbr import CPF
from datetime import date, datetime


def validate_name():
    while True:
        try:
            name = input('Digite seu primeiro nome: ').strip().capitalize()

            if not name.isalpha():
                raise Exception('Formato de nome incorreto')

            return name

        except Exception as err:
            print(err)


def validate_gender():
    genders = ['feminino', 'masculino', 'outro']
    while True:
        try:
            for pos, gender in enumerate(genders):
                print(f'{pos + 1:02}: {gender}')

            escolha = input('Escolha seu gênero: ')

            if not escolha.isdigit() or int(escolha) not in list(range(1, len(genders) + 1)):
                raise ValueError('Digite um valor válido')

            return genders[int(escolha) - 1]
        except ValueError as err:
            print(err)


def validate_email():
    while True:
        try:
            email = input('Digite seu email: ')
            email_format = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'

            if not re.match(email_format, email):
                raise Exception('Digite um email válido')

            return email

        except Exception as err:
            print(err)


def validate_phone():
    while True:
        try:
            phone = input('Digite seu número de telefone: ')
            pattern = '([0-9]{2})(9)?([0-9]{4,5})([0-9]{4})'
            res = re.search(pattern, phone)
            return f'({res.group(1)}) {res.group(2) if res.group(2) else "9"} {res.group(3)}-{res.group(4)}'

        except Exception:
            print('Formato de telefone inválido!')


def validate_cpf():
    while True:
        try:
            cpf = input('Digite seu CPF: ')

            cpf_regex = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'

            if len(cpf) != 11 or not re.match(cpf_regex, cpf):
                raise Exception('Formato de CPF inválido')

            if not CPF().validate(cpf):
                raise Exception('CPF inválido')
            return cpf
        except Exception as err:
            print(err)


def validate_birthdate():
    while True:
        try:
            birthdate = input('Digite sua data de nascimento: ')

            date_of_birth = datetime.strptime(birthdate, '%d/%m/%Y')
            today = datetime.now()

            if date_of_birth > today:
                raise Exception('Data inválida! Digite no formato DD/MM/AAAA.')

            return birthdate
        except Exception as err:
            print(err)


def calculateAge(birthDate):
    birthDate = datetime.strptime(birthDate, "%d/%m/%Y").date()

    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age
