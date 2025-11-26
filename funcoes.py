import numpy as np
import random

# funcao objetivo
def funObjetivo(x, y):
    return (
        np.sin(np.pi * x)**2
        + (x - 1)**2 * (1 + np.sin(np.pi * y)**2)
        + (y - 1)**2
    )
    
# codificacao binaria
def codificacao(bits, min=0.0, max=4.0, n_bits=12):         # 12 bits cabe o intervalo de 0 a 4 com precisao de 3 casas decimais
    inteiro = int(bits, 2)                                  # converte string binaria pra inteiro
    return min + inteiro * ((max - min) / (2**n_bits - 1))  # formula de conversao

# populacao inicial
def gerarPopulacao(qtd, n_bits=12):
    return [''.join(random.choice("01") for _ in range(n_bits*2)) for _ in range(qtd)] # *2 pq x=12 bits e y=12, cromosso de 24 bits

# selecao (metedo torneio)
def selecao_torneio(populacao_avaliada, k=3):
    # escolhe k competidores aleatoriamente
    competidores = random.sample(populacao_avaliada, k)
    
    # vence quem tiver o menor fitness (t[3])
    vencedor = min(competidores, key=lambda t: t[3])
    
    # retorna apenas a string de bits do vencedor
    return vencedor[0]

# cruzamento (2 pontos aleatorios)
def cruzamento_2_pontos(pai1, pai2):
    # o tamanho do cromossomo 
    tamanho = len(pai1)
    
    # escolhe 2 pontos de corte distintos (entre o indice 1 e o penultimo), sorted garante que p1 venha antes de p2
    p1, p2 = sorted(random.sample(range(1, tamanho), 2))
    
    # cria os filhos trocando a parte do meio (entre p1 e p2)
    # filho 1 = começo pai1 + meio pai2 + fim pai1
    filho1 = pai1[:p1] + pai2[p1:p2] + pai1[p2:]
    
    # filho 2 = começo pai2 + meio pai1 + fim pai2
    filho2 = pai2[:p1] + pai1[p1:p2] + pai2[p2:]
    
    return filho1, filho2

# elitismo (um individuo por geracao)
def elitismo(populacao_avaliada):
    # ordena a lista do menor fitness para o maior (t[3] = valor do fitness na tupla)
    populacao_ordenada = sorted(populacao_avaliada, key=lambda t: t[3])
    
    # pega o primeiro da lista (o melhor)
    melhor_individuo = populacao_ordenada[0]
    
    # retorna apenas a string de bits (genótipo) para ser usada na próxima geração
    return melhor_individuo[0]

# mutacao (inversao de bits)
def mutacao_inversao(individuo, taxa_mutacao=0.01):
    novo_individuo = ''
    for bit in individuo:
        if random.random() < taxa_mutacao:
            novo_individuo += '1' if bit == '0' else '0' 
        else:
            novo_individuo += bit
    return novo_individuo