# Fatiamento de strings
'''
Strigns em python são iteraveis (possuem indice)
A função len retorna a quantidade de caracteres que uma string possui

fatiamento [i:f:p] [::]
'''

nome = 'Nelson'
print(nome[0]) # primeira letra do indice positivo
print(nome[-6]) # primeira letra do indice negativo 

# Fatiando a string a partir de um ponto especifico

print(nome[1:]) # do caractere da posição 1 até o final

print(nome[1:3]) # do primeiro ao segundo caractere (ele corta o 3 que é onde pedimos para ele parar)

# Fatiando no indice negativo
print(nome[-3:]) # os tres ultimos caracteres

# Função len
print(len(nome)) # contador de caracteres

# inicio: fim: passo [i:f:p]

print(nome[0:5:2]) # vou começar do 0, parar no 5 e pular de 2 em dois
print(nome[::-1]) # invertendo a string
print(nome[-1:-7:-1]) # vai do -1 até o -6, coloquei -7 para ele não cortar o ultimo caractere