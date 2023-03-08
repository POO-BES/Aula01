import random

# Função que recebe como parâmetro o tamanho da lista informado pelo usuário
# e retorna a lista preenchida com valores aleatórios 
def randomValues(size):
    # Criamos uma lista vazia
    values = []
    # Criamos um laço de repetição (loop) que irá rodar até o tamanho informado pelo usuário
    for i in range(size):
        # Adicionamos um número inteiro aleatório entre 0 e 30 à lista
        values.append(random.randrange(0, 30))
    
    # Retornamos a lista preenchida
    return values

# Armazenamos na variável size um número inteiro informado pelo usuário
size = int(input("Digite um tamanho para a lista: "))

# Imprimimos um cabeçalho para o resultado
print('\n------------ RESULTADO ------------')
# Percorremos todos os valores da lista que está sendo retornada pela função randomValues
for value in randomValues(size):
    # Se o valor for divisível por 3
    if value % 3 == 0:
        # Então imprimimos o valor seguido de sua descrição
        print(f'{value} - número múltiplo de três')
    # Caso o valor não for divisível por 3 e for par
    elif value % 2 == 0:
        # Então imprimimos o valor seguido de sua descrição
        print(f'{value} - número par')      
    # Caso o valor não for nem divisível por 3, nem par, ele é impar  
    else:
        # Então imprimimos o valor seguido de sua descrição
        print(f'{value} - número ímpar')