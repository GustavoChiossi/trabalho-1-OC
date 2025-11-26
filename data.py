# TEM QUE SER GRAFICO 3D!!
# não precisa de arquivo .log

import matplotlib.pyplot as plt
import csv
import os

# def dos caminhos
CAMINHO_GRAFICOS = "graficos/"
CAMINHO_CSV = "csv/"

def setup_diretorios():
    os.makedirs(CAMINHO_GRAFICOS, exist_ok=True)
    os.makedirs(CAMINHO_CSV, exist_ok=True)
    print("Diretórios verificados/criados com sucesso.")

def salvar_dados_csv(nome_arquivo, dados):
    caminho_completo = os.path.join(CAMINHO_CSV, nome_arquivo)
    arquivo_existe = os.path.isfile(caminho_completo)
    
    with open(caminho_completo, mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        
        if not arquivo_existe:
            escritor.writerow(['Geracao', 'Melhor_Fitness', 'X', 'Y', 'Media_Fitness'])
            
        escritor.writerow(dados)

def plotar_grafico_convergencia(historico_fitness, nome_arquivo="grafico.png"):
    caminho_completo = os.path.join(CAMINHO_GRAFICOS, nome_arquivo)
    
    plt.figure()
    plt.plot(historico_fitness)
    plt.title('Convergência do Algoritmo Genético')
    plt.xlabel('Geração')
    plt.ylabel('Melhor Fitness')
    plt.grid(True)
    plt.savefig(caminho_completo)
    plt.close() 
    print(f"Gráfico salvo em: {caminho_completo}")