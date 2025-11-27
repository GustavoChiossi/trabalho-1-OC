import random
import numpy as np

# FUNCAO OBJETIVO
def funObjetivo(x, y):
    return (np.sin(np.pi * x)**2 + (x - 1)**2 * (1 + np.sin(np.pi * y)**2) + (y - 1)**2)
    
# CODIFICACAO BINARIA
def codificacao(bits, min=0.0, max=4.0, n_bits=12):         # 12 bits cabe o intervalo de 0 a 4 com precisao de 3 casas decimais
    inteiro = int(bits, 2)                                  # converte string binaria pra inteiro
    return min + inteiro * ((max - min) / (2**n_bits - 1))  # formula de conversao

# POPULACAO INICIAL
def gerarPopulacao(qtd, n_bits=12):
    return [''.join(random.choice("01") for _ in range(n_bits*2)) for _ in range(qtd)] # *2 pq (x=12b) + (y=12b) = cromosso de 24b

# SELECAO (METODO TORNEIO)
def selecao_torneio(populacao_avaliada, k=3): # k=3 é o padrao de competidores
    # escolhe k competidores aleatoriamente
    competidores = random.sample(populacao_avaliada, k) 
    
    # vence quem tiver o menor fitness 
    # lambda compara individuos usando o fitness como metrica
    vencedor = min(competidores, key=lambda t: t[3])    
    
    # retorna a string de bits do vencedor
    return vencedor[0]                                  

# CRUZAMENTO (2 PONTOS ALEATORIOS)
def cruzamento_2_pontos(pai1, pai2, taxa_cruzamento):
    if random.random() > taxa_cruzamento:   # verifica se ocorre cruzamento
        return pai1, pai2                   # se nao ocorrer, retorna os pais originais
    
    tamanho = len(pai1) # tamanho do cromossomo 
    
    # escolhe 2 pontos de corte distintos (entre 1 e tamanho-1)
    # sorted ordena p1 antes de p2
    p1, p2 = sorted(random.sample(range(1, tamanho), 2))
    
    # cria os filhos trocando a parte do meio (entre p1 e p2)
    # filho 1 = começo pai1 + meio pai2 + fim pai1
    filho1 = pai1[:p1] + pai2[p1:p2] + pai1[p2:]
    
    # filho 2 = começo pai2 + meio pai1 + fim pai2
    filho2 = pai2[:p1] + pai1[p1:p2] + pai2[p2:]
    
    return filho1, filho2 # retorna os dois filhos gerados

# ELITISMO (UM INDIVIDUO POR GERACAO)
def elitismo(populacao_avaliada):
    # ordena a lista do menor fitness para o maior (t[3] = valor do fitness na tupla)
    populacao_ordenada = sorted(populacao_avaliada, key=lambda t: t[3])
    
    # pega o primeiro da lista (o melhor)
    melhor_individuo = populacao_ordenada[0]
    
    # retorna apenas a string de bits (genotipo) para ser usada na proxima geracao
    return melhor_individuo[0]

# MUTACAO (INVERSAO DE BITS)
def mutacao_inversao(individuo, taxa_mutacao):         
    novo_individuo = ''                                     # string vazia para construir o novo individuo
    for bit in individuo:                                   # percorre cada bit do individuo
        if random.random() < taxa_mutacao:                  # verifica se deve mutar
            novo_individuo += '1' if bit == '0' else '0'    # inverte o bit
        else:                                               # nao muta
            novo_individuo += bit                           # mantem o bit original
    return novo_individuo                                   # retorna o novo individuo mutado