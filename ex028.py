# entradas 
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    # conversão
    int_idade = int(idade)

    # Fatiamento
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    # Verificação
    if ' ' in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome NÃO contém espaços!')

    # Fatiamento
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"')

# apenas a idade digitada
elif not nome and idade:
    print(f'O nome não foi digitado mas sua idade é de {idade} anos')

# se nada for digitado
else:
    print('Desculpe, você não digitou nada!')