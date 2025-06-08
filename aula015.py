# input

nome = input('Digite o seu nome: ') # recebe os dados do usuario via terminal
# tudo que vem do teclado é string
print(f'O seu nome é {nome}') 
# print(f'O seu nome é {nome=}') colocamos um = apos o nome da variavel se desejarmos saber o nome da variavel e o valor ao mesmo tempo

# Recebendo e convertendo numeros 
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# OBS: Faça a coerção de tipos em outras variaveis e não na variavel de recebimento
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

soma = int_numero_1 + int_numero_2 
print(soma)
