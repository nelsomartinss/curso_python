"""
Faça um programa que peça ao usuário para digitar um número inteiro,Add commentMore actions
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print(f"\n{'*'*10} EX01 {'*'*10}\n")

numero = input('Digite um número inteiro: ')

try:
    int_numero = int(numero)
    if int_numero % 2 == 0:
        print(f'O número {int_numero} é PAR!\n')
    else:
        print(f'O número {int_numero} é IMPAR!\n')
except:
    print('\nVocê não digitou um número inteiro...')
    print('Tente novamente!\n')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print(f"\n{'*'*10} EX02 {'*'*10}\n")

hora = input('Digite que horas são (sem os minutos): ')

try:
    int_hora = int(hora)

    manha = int_hora >= 0 and int_hora <= 11
    tarde = int_hora >= 12 and int_hora <= 17
    noite = int_hora >= 18 and int_hora <= 23

    if manha:
        print('Bom dia!\n')
    elif tarde:
        print('Boa tarde!\n')
    elif noite:
        print('Boa noite!\n')
    else:
        print('Horário inválido ou inexistente!\n')
except:
    print('\nVocê não digitou um número inteiro...')
    print('Tente novamente!\n')
    exit()

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print(f"\n{'*'*10} EX03 {'*'*10}\n")

nome = input('Digite seu nome: ')
nome_len = len(nome)

nome_curto = nome_len > 0 and nome_len <= 4
nome_normal = nome_len >= 5 and nome_len <= 6
nome_grande = nome_len > 6

if nome_curto:
    print('Seu nome é curto.\n')
elif nome_normal:
    print('Seu nome é normal.\n')
elif nome_grande:
    print('Seu nome é muito grande.\n')
else:
    print('Algo deu errado. Tente novamente!\n')