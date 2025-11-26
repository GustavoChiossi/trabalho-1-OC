import math
import random

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

# elitismo (um individuo por geracao)
def elitismo(populacao_avaliada):
    """
    Preserva o melhor indivíduo da geração.
    populacao_avaliada: lista de tuplas (bits, x, y, fitness)
    """
    # Ordena a lista do menor fitness para o maior (Minimização)
    # A chave t[3] refere-se ao valor do fitness na tupla
    populacao_ordenada = sorted(populacao_avaliada, key=lambda t: t[3])
    
    # Pega o primeiro da lista (o melhor)
    melhor_individuo = populacao_ordenada[0]
    
    # Retorna apenas a string de bits (genótipo) para ser usada na próxima geração
    return melhor_individuo[0]