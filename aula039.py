'''
Exercício - Iterando strings
'''

nome = 'Nelson Martins' 
nome_len = len(nome)

contador = 0
nova_string = ''

while contador < nome_len:
    nova_string += f'*{nome[contador]}' # criando nova string colocando um * antes de cada letra
    contador+=1

nova_string+='*' # adicionando o ultimo *
print(f'\n{nova_string}\n')
