# Interpolação de strings

''' Outra forma de inserir variaveis dentro de uma string

s - string (usamos %s)
d e i - int (usamos %d ou %i)
f - float (usamos %f)
x e X - Hexadecimal (ABCDEF0123456789)

'''

nome = 'Nelson'
peso = 65.6
interpolacao = "%s possui um peso de %.1fKg" %(nome, peso)
print(interpolacao)

# Hexadecimal - Pegando o hexadecimal de um valor

print('O hexadecimal de %i é %06x' %(24, 24)) # descobrindo o hexadecimal de 24 que é 18, adicionamos 06 casas decimais (ele preenchera com 0 caso não tenha mais casas)

print('O hexadecimal de %i é %06X' %(65, 65)) # hexadecimal em maiusculo
# obs: o hexadecimal só funciona com valores inteiros.