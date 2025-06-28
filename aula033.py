'''
tipos biuld-in (imbutidos): str, int, float, bool etc (tipos já instalados que não necessitam importação)  - esses são os tipos imutáveis (não podemos mudar o tipo ao longo do programa) e tudo isso é objeto
'''

string = 'Nelson' # dado imutável
outr_string = string # essa variavel copia o valor da primeira
# não é possivel modificar esse tipo de dado
# string[1] = 'D' # Não podemos fazer isso 

# tudo é objeto - objetos possuem funções (métodos)
print(string.upper()) # metodo que deixa tudo maiusculo
print(string.lower()) # metodo que deixa tudo minusculo