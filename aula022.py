# Operador lógico - OR
# Para o resultado ser True pelomenos uma verificação tem que ser True
# 'ISSO' OU 'AQUILO'
# Se as duas ou mais condições forem falsas o resultado é FALSE

entrar = input('Digite [E] para entrar e [S] para sair: ')

if entrar == 'E' or 'e': # verifica se foi 'E' ou 'e'
    print('entrou!')
elif entrar == 'S' or 'S': # o verifica se foi 'S' ou 's'
    print('Saiu!')
else: # resultado enviado caso seja FALSE
    print('inválido')

# Avaliação de curto circuito
print(True or False or 0) # ele vai finalizar no primeiro True que encontrar, depois disso ele não precisa mais verificar

print(False or False or True or False) # Ele vai exibir o valor que foi avalido como True e finalizar ali mesmo