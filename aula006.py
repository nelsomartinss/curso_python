# Conversão/Coerção de tipos (type convertion, typecasting, coercion)
# É o ato de converter um tipo em outro
# tipos imutaveis e primitivos: str, int, float, bool

# Concatenção - Se usarmos o operador de adição com strings 
print('1' + '1') # ele junta duas strings: '11'
# print('1' + 1) Isso vai dar um erro

# Convertendo tipos e usando type para ver o tipo

# str para int
print(type(int('1'))) # '1' vai passar a ser 1

# int para float
print(type(float(1))) # 1 vai passar a ser 1.0

# float ou int para str 
print(type(str(1.2))) # vai passar a ser '1.2'

# Obs: int(), float() e str() também são classes e não funções

# resolvendo erro com conversão 
print(int('1') + 1) # agora ele vai transformar '1' em 1 e somar corretamente >>> 2 

# Convertendo em boolean com bool()
# Dependendo do valor que passarmos para bool ele interpretará como true ou false 
print(bool(1)) # True 
print(bool(0)) # False - 0 é considerado False 
print(bool(-1)) # True - Números negativos são True
print(bool(0.1)) # True - apenas o completamente 0 é false 
print(bool('')) # False - Strings vazias também são false 
print(bool('nelson')) # True
