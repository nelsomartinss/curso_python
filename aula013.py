# Formatação de Strings

nome = 'Nelson'
sobrenome = 'Martins'
idade = 24

# f-strings - usando variaveis dentro de um texto 
texto = f'{nome} {sobrenome} tem {idade} anos de idade'
print(texto)

# escolhendo quantidade de casas decimais com :.NUMEROf
# duas casas
print(f'{idade} com duas casas decimais: {idade:.2f}') # 24.00