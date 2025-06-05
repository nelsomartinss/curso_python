# A função print() - usada para exibir algo no terminal 
# dentro dela passamos argumentos, tudo vai ser exibido na tela 

print('Nelson', 24) # exibindo a string e o number
print('Quebrando a linha') # esse outro print quebra a linha, ou seja, é exibindo em outra linha

# Nelson 24 -> foi exibindo assim, exibindo separado por um separador padrao, mas podemos mudar o separador

print('Nelson', 24, sep='-') # agora os dois argumentos serão separados por -

# podemos quebrar a linha no mesmo print com o \n
print('Quebrando a\nlinha') # quando o interpretador ler um \n ele quebra a linha

# também podemos usar o end='' para quebrar a linha ou evitar a quebra
print('Nelson', end=' ') 
print('Martins') # adicionei um espaço ao final e ele saiu do padrão de quebrar a linha que é \n e isso fez o 'Nelson Martins' ficar em uma só linha