import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from controllers.User import *


df = pd.read_csv('./database/users.csv')
fem = df[df.gender == 'feminino']
mas = df[df.gender == 'masculino']
outro = df[df.gender == 'outro']
idade = pd.DataFrame(data=df['birthdate'].apply(calculateAge))
df['ages'] = idade
count_ages = df['ages']


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return f"{pct:.1f}%\n({absolute} pessoas)"


def plot_details():

    data = [len(fem), len(mas), len(outro)]

    # Criação da figure com uma linha e duas colunas. Figsize define o tamanho da
    # figure
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect='equal'))

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color='w'))

    ax.legend(wedges, ['Masculino', 'Feminino', 'Outro'], title='Pessoas por gênero',
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight='bold')

    #ax.set_title{'Quantidade de pessoas por gênero'}

    plt.show()


def main_statistics():
    print('Principais estatísticas encontradas')

    print(f'Quantidade de usuários cadastrados {len(df)}')
    print(f'Quantidade de usuários do genero Feminino: {len(fem)}')
    print(f'Quantidade de usuários do genero Masculino: {len(mas)}')
    print(f'Quantidade de usuários do genero Outros: {len(outro)}')

    print(f'Menores que 18 anos: {len([x for x in count_ages if x < 18])}')
    print(f'Entre 18 e 35: {len([x for x in count_ages if x >= 18 and x < 35])}')
    print(f'Entre 35 e 65: {len([x for x in count_ages if x >= 35 and x < 65])}')
    print(f'Maior que 65: {len([x for x in count_ages if x >= 65])}')
    try:
        menu = {
            'Mostrar gráficos de idade': plot_details,

        }
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
    except Exception as err:
        print(err)
    input('Tecle Enter para retornar.')
