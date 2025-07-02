# while dentro de um while

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: # o programa entra nesse while
    coluna = 1 # cria a variavel coluna
    while coluna <= qtd_colunas: # e depois entra nesse até coluna ser 5
        print(f'{linha=} {coluna=}')
        coluna+=1

    linha+=1 # somente depois ele incrementa 1 a linha e retorna ao inicio onde a coluna volta a ser 1 e começa tudo novamente, depois que linha for 5 o primeiro while acaba
 
print('Acabou!') # e a mensagem final é exibida