# Função/Método format() - Outra forma de formatar strings
# .format() é um método que é uma função que está dentro de um objeto e tudo em python é um objeto

nome = 'Nelson'
sobrenome = 'Martins'
idade = 24

# Formatação por ordem
#                                                   argumentos
formatacao1 = "{} {} possui {} anos de idade".format(nome, sobrenome, idade)
#                                                   colocamos na ordem das chaves

print(formatacao1)

# Formatação por indice
formatacao2 = "{0} {0} {1} possui {2} anos de idade".format(nome, sobrenome, idade)
# com os indices podemos colocar a mesma variavel repetidas vezes na string, a variavel de posição 0 vai repetir 2 vezes

print(formatacao2)

# Formatação com parametros nomeados 
formatacao3 = "{primeiro_nome} {segundo_nome} possui {idade} anos de idade".format(
    primeiro_nome = nome, 
    segundo_nome = sobrenome,
    idade = idade) # assim que nomearmos um parametro os outros tambem precisam ser nomeados

print(formatacao3)