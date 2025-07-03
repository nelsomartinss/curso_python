'''
while com else
'''

contador = 0

while contador < 3:
    print('o while está sendo executado...')
    contador+=1
else:
    print('O else foi executado...')
    # esse else só será executado quando o while for finalizado
    # se estiver um break no while o else não é executado

print('Agora estamos fora do while!')