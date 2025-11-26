# == BIBLIOTECAS 
import matplotlib.pyplot as plt # plot de graficos
import random                   # gerar populacao inicial
import math                     # calculos 
import numpy                    # calculos (talvez use)
import csv                      # gravar em csv
import logging                  # arquivo de log  
import os                       # criar pastas

# == CONFIGURACOES INICIAIS

# caminhos dos arquivos
caminho_graficos = "graficos/"
caminho_csv = "csv/"
caminho_logs = "logs/"

# cria pastas se nao existirem
os.makedirs(caminho_graficos, exist_ok=True)
os.makedirs(caminho_csv, exist_ok=True)
os.makedirs(caminho_logs, exist_ok=True)

#  valores iniciais da funcao
x = 4.00 
y = 3.53 
z = 24.3212

# DEFINICOES DAS FUNCOES

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

# selecao (metedo torneio)
def selecao_torneio(populacao_avaliada, k=3):
    """
    populacao_avaliada: lista de tuplas (bits, x, y, fitness)
    k: tamanho do torneio (padrão 3)
    """
    # 1. Escolhe 'k' competidores aleatoriamente
    competidores = random.sample(populacao_avaliada, k)
    
    # 2. Vence quem tiver o MENOR fitness (t[3])
    vencedor = min(competidores, key=lambda t: t[3])
    
    # Retorna apenas a string de bits do vencedor
    return vencedor[0]

# cruzamento (2 pontos aleatorios)
def cruzamento_2_pontos(pai1, pai2):
    # O tamanho do cromossomo (24 bits)
    tamanho = len(pai1)
    
    # Escolhe 2 pontos de corte distintos (entre o índice 1 e o penúltimo)
    # sorted garante que ponto1 venha antes de ponto2
    p1, p2 = sorted(random.sample(range(1, tamanho), 2))
    
    # Cria os filhos trocando a parte do meio (entre p1 e p2)
    # Filho 1 = Começo Pai1 + Meio Pai2 + Fim Pai1
    filho1 = pai1[:p1] + pai2[p1:p2] + pai1[p2:]
    
    # Filho 2 = Começo Pai2 + Meio Pai1 + Fim Pai2
    filho2 = pai2[:p1] + pai1[p1:p2] + pai2[p2:]
    
    return filho1, filho2

# mutacao (inversao binaria)

# elitismo (um individuo por geracao)

# criterio de parada

# avaliacao da populacao

# ARQUIVOS 

# log

# configuracao do logging (depois
#logging.basicConfig(
#    filename='ag_fun13.log', 
#    level=logging.INFO, 
#    format='%(asctime)s - %(levelname)s - %(message)s',
#    datefmt='%Y-%m-%d %H:%M:%S',
#    handlers=[
#        logging.FileHandler(caminho_logs + 'ag_fun13.log'),
#        logging.StreamHandler()
#    ]    
#)

# gravar em csv

# plotar graficos

# == RESULTADOS DOS TESTES INICIAIS
print("Melhor indivíduo:")
print("Bits:", melhor[0])
print(f"x: {melhor[1]:.3f}")
print(f"y: {melhor[2]:.3f}")
print(f"fitness: {melhor[3]:.3f}")

print("\n--- Testando Operadores ---")

# 1. Selecionar dois pais usando o Torneio
pai1 = selecao_torneio(resultados, k=3)
pai2 = selecao_torneio(resultados, k=3)

print(f"Pai 1 selecionado: {pai1}")
print(f"Pai 2 selecionado: {pai2}")

# 2. Realizar o cruzamento
filho_a, filho_b = cruzamento_2_pontos(pai1, pai2)

print(f"Filho A gerado:    {filho_a}")
print(f"Filho B gerado:    {filho_b}")