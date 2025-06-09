# Exercicios com if e else

primeiro_numero = input('Digite o primeiro numero: ')
segundo_numero = input('Digite o segundo numero: ')

int_primeiro_numero = int(primeiro_numero)
int_segundo_numero = int(segundo_numero)

if int_primeiro_numero > int_segundo_numero:
    print(f"O {primeiro_numero=} é maior do que o {segundo_numero=}")
elif int_segundo_numero > int_primeiro_numero:
    print(f"O {segundo_numero=} é maior do que {primeiro_numero=}")
else:
    print(f'Os números {primeiro_numero} e {segundo_numero} são iguais!')
