import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt 
import os
import csv
import funcoes 

# define o caminho dos diretorios
CAMINHO_GRAFICOS = "graficos/"
CAMINHO_CSV = "csv/"

# criar diretorios se nao existirem
def setup_diretorios(): 
    os.makedirs(CAMINHO_GRAFICOS, exist_ok=True)
    os.makedirs(CAMINHO_CSV, exist_ok=True)

# salvar dados em arquivo csv
def salvar_dados_csv(nome_arquivo, linha):              # salva uma linha no arquivo csv
    caminho = os.path.join(CAMINHO_CSV, nome_arquivo)   # caminho completo do arquivo
    novo = not os.path.exists(caminho)                  # verifica se o arquivo ja existe

    with open(caminho, "a") as f:   # abre em modo append (pra nao sobrescrever)
        w = csv.writer(f)           # cria o escritor csv
        if novo:                    # se o arquivo nao existia, escreve o cabecalho
            w.writerow(["Geracao", "Melhor_Fitness", "X", "Y", "Media"]) 
        w.writerow(linha)           # escreve a linha de dados

# grafico 3d
def grafico(melhor, geracao): 
    x = np.linspace(0, 4, 200)  # eixo x
    y = np.linspace(0, 4, 200)  # eixo y
    X, Y = np.meshgrid(x, y)    # cria a grade 2d

    # calculo da funcao objetivo para cada ponto da grade
    Z = funcoes.funObjetivo(X, Y)

    fig = plt.figure(figsize=(10, 8))                       # cria a figura
    ax = fig.add_subplot(111, projection="3d")              # cria o eixo 3d 
    ax.plot_surface(X, Y, Z, cmap=cm.inferno, alpha=0.85)   # superficie 3d

    bx, by, bf = melhor[1], melhor[2], melhor[3] # melhor individuo (x, y, fitness)
    ax.scatter(bx, by, bf, s=120, color="red")   # ponto do melhor individuo

    plt.savefig(f"{CAMINHO_GRAFICOS}/geracao{geracao}.png") # salva o grafico
    plt.close() # fecha a figura

# grafico de linha
def grafico_linha(mediaFit):                # grafico da media fitness por geracao
    plt.figure(figsize=(10, 6))             # cria a figura
    plt.plot(mediaFit, marker='o')          # plota a linha com marcadores
    plt.title("Fitness Médio por Geração")  # titulo
    plt.xlabel("Geração")                   # eixo x
    plt.ylabel("Fitness Médio")             # eixo y
    plt.grid()                              # ativa a grade
    plt.savefig(f"{CAMINHO_GRAFICOS}/fitness_medio.png") 
    plt.close() 
    
# gera heatmap
def heatmap(caminho):
    x = np.linspace(0, 4, 400)
    y = np.linspace(0, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = funcoes.funObjetivo(X, Y)
    
    plt.figure(figsize=(10, 8))
    plt.contourf(X, Y, Z, levels=50, origin='lower', cmap='inferno', antialiased=True)

    plt.title("Heatmap da Função")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.savefig(f"{CAMINHO_GRAFICOS}/heatmap.png")
    plt.close()