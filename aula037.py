# while - continue

contador = 0

while contador < 20:
    contador+=1

    if contador >= 1 and contador <= 10: # se o contador estiver entre 1 e 10
        continue # continue (ele pula)

    print(contador) # depois ele exibe o valor de contador