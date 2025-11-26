import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import os
from funcoes import funObjetivo

CAMINHO_GRAFICOS = "graficos/"
CAMINHO_CSV = "csv/"

def setup_diretorios():
    os.makedirs(CAMINHO_GRAFICOS, exist_ok=True)
    os.makedirs(CAMINHO_CSV, exist_ok=True)

def salvar_dados_csv(nome_arquivo, linha):
    caminho = os.path.join(CAMINHO_CSV, nome_arquivo)
    novo = not os.path.exists(caminho)

    with open(caminho, "a") as f:
        import csv
        w = csv.writer(f)
        if novo:
            w.writerow(["Geracao", "Melhor_Fitness", "X", "Y", "Media"])
        w.writerow(linha)

# grafico 3d
def grafico(melhor, geracao):
    # domínio
    x = np.linspace(0, 4, 200)
    y = np.linspace(0, 4, 200)
    X, Y = np.meshgrid(x, y)

    # calculo correto
    Z = funObjetivo(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.85)

    # ponto ótimo
    bx, by, bf = melhor[1], melhor[2], melhor[3]
    ax.scatter(bx, by, bf, s=120, color="red")

    plt.savefig(f"{CAMINHO_GRAFICOS}/gen_{geracao}.png")
    plt.close()

# grafico de linha, fitness medio de cada geracao
def grafico_linha(mediaFit):
    plt.figure(figsize=(10, 6))
    plt.plot(mediaFit, marker='o')
    plt.title("Fitness Médio por Geração")
    plt.xlabel("Geração")
    plt.ylabel("Fitness Médio")
    plt.grid()
    plt.savefig(f"{CAMINHO_GRAFICOS}/fitness_medio.png")
    plt.close()