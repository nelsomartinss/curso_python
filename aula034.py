# while e break

''' enquanto verdadeira
while True:
    print('Olá, mundo!') # loop infinito '''

# controle
numero = 0
# essa repetição vai ser executada enquanto o numero for menor do que 10
while numero < 10:
    print('Olá, mundo')
    numero+=1 # a cada repetição é somado mais 1 ao numero (isso controla o loop)

# break - Encerrando o loop
while True:
    nome = input('Digite seu nome: ').upper() 
    print(f'Bem vindo, {nome}') # o loop vai pedir o nome infinitamente por que ele é True

    if nome == 'SAIR': # porem se o nome for 'SAIR'
        break # Ele sai do laço - quebra o laço