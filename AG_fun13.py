# tem uma biblioteca que se chama PyGAD, mas acho que não pode usar

import matplotlib.pyplot as plt # plot de graficos
import random                   # talvez use
import math                     # calculos 
import numpy                    # calculos

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
    inteiro = int(bits, 2)                                  # conversao
    return min + inteiro * ((max - min) / (2**n_bits - 1))  # formula de conversao

# populacao inicial

# selecao (metedo torneio)

# cruzamento (dois pontos aleatorios)

# mutacao (inversao binaria)

# elitismo (um individuo por geracao)