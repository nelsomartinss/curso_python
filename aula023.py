# Operador lógico - not
# ele inverte as expressões
# not True = False
# not False = True

print(not True) # False
print(not False) # True

# Verificando
senha = input('Digite sua senha: ') 

if not senha: # se ele verificar que a senha é False
    print('Você não digitou nada') # esse bloco será exibido