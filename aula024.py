# Operadores 'in' e 'not in'
# in - 'está entre'
# not in - 'não está entre'

# Strings são interáveis, podemos navegar pelos caracteres pelos seus indices. Os indices começam do 0, mas também existem indices negativos. 
# O indice negativo é contado de trás pra frente e vai até o -1

meu_nome = 'Nelson' # o indice positivo vai de 0-5 e o negativo de -6 a -1

# Acessando primeira letra com indice positivo e negativo

print(meu_nome[0], meu_nome[-6]) 

# Utilizando 'in' para checar letras 

print(('n' or 'N') in meu_nome) # verificando se 'n' ou 'N' estão entre as letras do meu_nome='Nelson'

# Utilizando 'not in' para chegar se as letras NÃO estão naquela string

print('a' not in meu_nome) # se o 'a' não estiver, ele retorna true

# Exercicio

nome = input('Digite o seu nome: ')
encontrar_letra = input('Digite a letra que deseja encontrar: ')

if encontrar_letra in nome:
    print(f'Letra "{encontrar_letra}" está em "{nome}"')
else:
    print(f'Letra "{encontrar_letra}" não está em "{nome}"')

