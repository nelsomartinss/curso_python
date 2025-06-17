# Boas práticas

# Em python não existem CONSTANTES, porém, por convensão, variáveis que não pretendemos mudar o seu valor escrevemos em letras maiusculas

# variavel
meu_nome = 'Nelson'

# constante
MEU_NOME = 'Nelson'

# Não é bom ter MUITAS condições dentro de um mesmo if - Precisamos aprender a escrever código limpo - é melhor jogar essas expressões dentro de variaveis

# Quanto mais blocos de código dentro de outros blocos mais complexo é. Em python COMPLEXIDADE NÃO É BOM - SIMPLES É MELHOR

# exemplo/exercicio

# variaveis
velocidade = 59 # velocidade do carro
local = 99 # km onde o carro se encontra

# Constantes
RADAR_1 = 60 # Velocidade máxima do radar
LOCAL_1 = 100 # local/km onde esse radar está
RADAR_RANGE = 1 # Espaço antes e depois do radar

# verificando se o carro passou da vel do radar
verificar_carro_pass_radar = velocidade > RADAR_1
# verificando
verificar_carro_pass_range = local >= (LOCAL_1 - RADAR_RANGE) and local <= (LOCAL_1 + RADAR_RANGE)

if verificar_carro_pass_radar: # se o resultado dessa expressão tiver sido true
    print('Velocidade do carro passou do limite máximo')

if verificar_carro_pass_radar and verificar_carro_pass_range: # se o carro tiver passado acima da velocidade dentro do range que é entre 99 e 101
    print('Carro multado em radar 1')

