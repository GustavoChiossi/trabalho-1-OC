# tem uma biblioteca que se chama PyGAD, mas acho que não pode usar

import matplotlib.pyplot as plt # plot de graficos
import random                   # gerar populacao inicial
import math                     # calculos 
import numpy                    # calculos (talvez use)

#  valores iniciais da funcao
x = 4.00 
y = 3.53 
z = 24.3212

# funcao objetivo
def funObjetivo(x, y): 
    return (
        math.sin(math.pi * x)**2 + (x - 1)**2 * (1 + math.sin(math.pi * y)**2) + (y - 1)**2
    )
    
# codificacao binaria
def codificacao(bits, min=0.0, max=4.0, n_bits=12):         # 12 bits cabe o intervalo de 0 a 4 com precisao de 3 casas decimais
    inteiro = int(bits, 2)                                  # converte string binaria pra inteiro
    return min + inteiro * ((max - min) / (2**n_bits - 1))  # formula de conversao

# populacao inicial
def gerarPopulacao(qtd, n_bits=12):
    return [''.join(random.choice("01") for _ in range(n_bits*2)) for _ in range(qtd)] # *2 pq x=12 bits e y=12, crom de 24 bits

# teste inicial
# depois precisa corrigir pra gerar N individuos
pop = gerarPopulacao(10)  

resultados = [] # lista
for individuo in pop:
    x_bits = individuo[:12] # 12 primeiros bits
    y_bits = individuo[12:] # 12 ultimos bits 
    x = codificacao(x_bits)
    y = codificacao(y_bits)
    fitness = funObjetivo(x, y)
    resultados.append((individuo, x, y, fitness)) # armazena 

# seleciona o individuo com o menor valor (fitness)
melhor = min(resultados, key=lambda t: t[3]) # t[3] é a fitness na lista de tuplas

# resultados
print("Melhor indivíduo:")
print("Bits:", melhor[0])
print(f"x: {melhor[1]:.3f}")
print(f"y: {melhor[2]:.3f}")
print(f"fitness: {melhor[3]:.3f}")

# selecao (metedo torneio)

# cruzamento (2 pontos aleatorios)

# mutacao (inversao binaria)

# elitismo (um individuo por geracao)

# criterio de parada

# avaliacao da populacao

# gravar em csv

# plotar graficos