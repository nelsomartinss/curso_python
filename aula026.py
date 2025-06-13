# f-strings
'''
s - string
d - int
f - float (mais usado)

> - Preencher para esquerda
< - Preencher para direita
^ - Preencher no centro
'''

nome = 'Nelson'

# Colocando 10 caracteres para completar a string do lado esquerdo
print(f'{nome: >10}') # preenchimento até chegar 10 caracteres

# Colocando 10 caracteres para completar a string do lado direito
print(f'{nome: <10}') # preenchimento até chegar 10 caracteres

# Colocando string no centro
print(f'{nome: ^12}') # fazendo a string completar 12 caracteres dos dois lados

# Preechendo com caracteres de fato
print(f'{nome:->10}') # ira colocar 0 do lado direito até completar
print(f'{nome:-<10}') # ira colocar 0 do lado esquerdo até completar
print(f'{nome:-^10}') # ira colocar 0 no centro até completar

# hexadecimal
print(f'{24:06x}') 

# obs: os dois pontos podem ser chamados por !r também 