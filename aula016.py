# introdução ao if e else

entrada = input('Você deseja "entrar" ou "sair"? ')

if entrada == 'entrar': # se entrada for igual a entrar
    print('Você entrou no sistema') # ... 
elif entrada == 'sair': # se não, se for igual a sair
    print('Você saiu do sistema') # ... 
else: # se não
    print('inválido!') # ...

# if = 'se'
# elif = 'se não, se'
# else = 'se não'

'''
O if pode existir sozinho, mas o elif e o else não, eles dependem de que um if exista anteriormente. 
Quando uma condição for verdadeira as condicionais são cessadas. 
Só podemos ter um if, o resto tem que ser 'elif', e só podemos ter um else
Se quisermos checar mais de uma condição verdadeiras precisamos iniciar novos blocos if 
'''