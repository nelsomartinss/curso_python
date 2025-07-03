'''
Calculadora com While
'''

while True:
    print(f'''\n{'*'*10} CALCULADORA SIMPLES {'*'*10}''')

    # ENTRADA PRIMEIRO VALOR
    primeiro_valor = input('\nDigite o primeiro valor: ')
    try:
        primeiro_valor = float(primeiro_valor)
    except ValueError:
        print("Erro: Digite um valor numérico (inteiro ou decimal).\n")
        continue  

    # ENTRADA SEGUNDO VALOR
    segundo_valor = input('Digite o segundo valor: ')
    try:
        segundo_valor = float(segundo_valor)
    except ValueError:
        print("Erro: Digite um valor numérico (inteiro ou decimal).\n")
        continue  

    # ENTRADA DO OPERADOR
    print('''\nLISTA DE OPERADORES:
+  : ADIÇÃO 
-  : SUBTRAÇÃO
*  : MULTIPLICAÇÃO
/  : DIVISÃO
          ''')
    operador = input('Digite o operador: ')

    # PROCESSAMENTO
    if operador == '+':
        resultado = primeiro_valor + segundo_valor
    elif operador == '-':
        if primeiro_valor < segundo_valor:
            resultado = segundo_valor - primeiro_valor
        else:
            resultado = primeiro_valor - segundo_valor
    elif operador == '*':
        resultado = primeiro_valor * segundo_valor
    elif operador == '/':
        if segundo_valor != 0:
            resultado = primeiro_valor / segundo_valor
        else:
            print('Não posso dividir 0 para nada!\n')
            continue
    else:
        print('\nOperador inválido! Verifique os operadores válidos no menu.')
        print('Reiniciando sistema...')
        continue

    # VERIFICANDO SE OS VALORES SÃO INTEIROS E EXIBINDO RESULTADO
    if primeiro_valor.is_integer() and segundo_valor.is_integer() and resultado.is_integer():
        primeiro_valor = int(primeiro_valor)
        segundo_valor = int(segundo_valor)
        resultado = int(resultado)
        print(f'\nResultado: \n{primeiro_valor} {operador} {segundo_valor} = {resultado}')
    else:
        print(f'\nResultado: \n{primeiro_valor} {operador} {segundo_valor} = {resultado :.2f}')

    # VERIFICANDO SE O USUÁRIO DESEJA CONTINUAR UTILIZANDO O SISTEMA 
    while True:
        pergunta = input('\nDeseja fazer outra operação? s/n: ').lower()

        if pergunta == 's':
            break
        elif pergunta == 'n':
            print('Até a próxima!\n')
            exit()
        else:
            print("Valor inválido! Digite 's' para SIM e 'n' para NÃO")