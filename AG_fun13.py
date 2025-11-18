# tem uma biblioteca que se chama PyGAD, mas acho que não pode usar

import matplotlib.pyplot as plt # plot de graficos
import random                   # talvez use
import math                     # calculos 
import numpy                    # calculos

#  restricoes
x = 4.00, y = 3.53, z = 24.3212

def fun13(x, y): # funcao objetivo
    return (
        math.sin(math.pi * x)**2 + (x - 1)**2 * (1 + math.sin(math.pi * y)**2) + (y - 1)**2
    )

while (x >= 0.0 and x <= 4.0 and y >= 0.0 and y <= 4.0) {
    # codigo
}

# inicilizar a populacao

# selecao (metedo torneio)

# cruzamento (dois pontos aleatorios)

# mutacao (inversao binaria)

# elitismo (um individuo por geracao)