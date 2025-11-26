import matplotlib.pyplot as plt
import csv
import logging
import os

# Definição dos caminhos
CAMINHO_GRAFICOS = "graficos/"
CAMINHO_CSV = "csv/"
CAMINHO_LOGS = "logs/"

def setup_diretorios():
    """Cria as pastas necessárias se elas não existirem."""
    os.makedirs(CAMINHO_GRAFICOS, exist_ok=True)
    os.makedirs(CAMINHO_CSV, exist_ok=True)
    os.makedirs(CAMINHO_LOGS, exist_ok=True)
    print("Diretórios verificados/criados com sucesso.")

def configurar_logger(nome_arquivo="ag_execucao.log"):
    """Configura o sistema de log para salvar em arquivo e mostrar na tela."""
    caminho_completo = os.path.join(CAMINHO_LOGS, nome_arquivo)
    
    # Limpa handlers anteriores para evitar duplicação se rodar várias vezes
    logging.getLogger().handlers = []
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(caminho_completo),
            logging.StreamHandler() # Mostra no terminal também
        ]
    )
    return logging.getLogger()

def salvar_dados_csv(nome_arquivo, dados):
    """
    Salva uma linha de dados no CSV.
    dados: Lista com [geracao, melhor_fitness, x, y, media_fitness]
    """
    caminho_completo = os.path.join(CAMINHO_CSV, nome_arquivo)
    arquivo_existe = os.path.isfile(caminho_completo)
    
    with open(caminho_completo, mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        
        # Se o arquivo não existia, escreve o cabeçalho primeiro
        if not arquivo_existe:
            escritor.writerow(['Geracao', 'Melhor_Fitness', 'X', 'Y', 'Media_Fitness'])
            
        escritor.writerow(dados)

def plotar_grafico_convergencia(historico_fitness, nome_arquivo="convergencia.png"):
    """Gera e salva o gráfico de evolução do fitness."""
    caminho_completo = os.path.join(CAMINHO_GRAFICOS, nome_arquivo)
    
    plt.figure()
    plt.plot(historico_fitness)
    plt.title('Convergência do Algoritmo Genético')
    plt.xlabel('Geração')
    plt.ylabel('Melhor Fitness')
    plt.grid(True)
    plt.savefig(caminho_completo)
    plt.close() # Fecha a figura para liberar memória
    print(f"Gráfico salvo em: {caminho_completo}")