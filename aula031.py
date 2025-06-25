'''
flag (bandeira) - marcar local
none - não valor
is - é (tipo, valor, identidade)
is not - não é (tipo, valor, identidade)
id - identidade
'''

# Podemos ver o id das variaveis no python com a função id()
nome = 'nelson'
id_nome = id(nome)
print(id_nome) # o id é o número de um objeto na memória, 

# As vezes o id pode ser o mesmo se o valor for o mesmo (o python tenta ser eficiente)
a = 10
b = 10 # mesmo valor
print(id(a), id(b)) # é o mesmo número porque o python aponta para o mesmo espaço na memoria

# flags - variáveis de controle (True ou False), vamos usa-las para verificar se uma condição foi ou não atendida
condicao = False
flag = None # criamos a flag com o valor none (não valor)

if condicao:
    flag = True # o valor da flag só vai mudar se a condição for true
 
print(flag) # se a condição for satisfeita poderemos ver o True aqui, isso até evita o uso do else, se não for, a flag continuara none

# is e is not
print(flag is None) # verifica se a flag É None
print(flag is not None) # verifica se a flag NÃO É None