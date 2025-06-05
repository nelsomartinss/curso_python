# Strings
'''
Python tem tipagem dinâmica (ele já sabe o tipo de dado passado para ele) forte. 
Strings são textos que estão dentro de aspas
'''

# Aspas simples 
print('Nelson')

# Aspas duplas
print("Nelson") # não existe diferença para aspas duplas

# Aspas duplas dentro das simples 
print('Nelson "Martins"') 

# Aspas simples dentro de aspas duplas 
print("Nelson 'Martins'")

# Utilizando o mesmo tipo de aspas e escapando 
print('Nelson \'Martins\'') # usando o \ podemos escapar e utilizar o mesmo tipo de aspas dentro e fora
print("Nelson \"Martins\"") # escapando com aspas duplas 

# Mostrando caracter de escape usando 'r'
print(r'Nelson \'Martins\'') # Nelson \'Martins\' será exibindo no terminal
print(r'Nelson \n Martins') # isso também funciona com os caracteres de quebra de linha