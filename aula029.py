''' introdução ao try/except
try -> tenta executar um código
except -> captura o erro (se houver um)

Uma exceção é um erro
int('a') essa linha causa uma exceção, por exemplo 
'''

numero = input('Digite um número: ')

# tente
try:
    # se por algum motivo houver um erro dentro desse código
    int_numero = int(numero)
    somar = int_numero + int_numero
    print(somar)

# excessão
except:
    # ele pula para dentro desse bloco de excessão
    print('Isso não é um número')

# se fosse um if o código iria dar erro e seria interrompido, o try except é justamente para isso, para executarmos outra coisa quando ocorrer uma excessão