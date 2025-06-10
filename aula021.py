# Operadore lógico - and [

'''
Para que o resultado de uma operação and seja True todas as comparações tem que ser True, se alguma for False o resultado é false. 

Valores que avaliam como Falsy 
- 0
- 0.0
- ''
- False

Obs: O tipo de dado 'None' representa um 'não valor'
'''

nome = 'Nelson'
idade = 24

# se as duas condições abaixo forem True então o primeiro bloco será executado, se alguma for false, o segundo será executado
if nome == 'Nelson' and idade == 24:
    print('Olá, Nelson Martins')
else:
    print('Você não é o Nelson')


# Retornando false 
if 1 == 1 and 2 == 1: # 1 é igual 1 mas 2 não é igual a 2, logo isso vai avaliar como False
    print('correto')
else:
    print('errado')

# Avaliação de curto circuito
print(True and False and True) # A operação foi finalizada assim que ele encontrou o False e retorna no console o valor onde ele parou:
print(True and 0 and True) # ele irá retornar o 0