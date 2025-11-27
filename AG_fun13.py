import random
from funcoes import *
from data import *

# CONFIGURACOES INICIAIS (PADROES)
mediasFit = []                       # lista pra guardar as medias fitness 
setup_diretorios()                   # iniciar diretorios 
TAMANHO_POP = random.randint(20, 60) # tamanho entre 20 e 60 
NUM_GERACOES = 50                                             
TAXA_CRUZAMENTO = 0.7                   
TAXA_MUTACAO = 0.01       

# PROMPT PRO USUARIO
print("\n=== Configuração do AG ===")

# pega valores do usuario (Enter = padrao)
valor = input("Tamanho da população (ENTER para usar aleatório entre 20 e 60): ")
if valor.strip():               # se o usuario digitou algo
    TAMANHO_POP = int(valor)    # atualiza 
else:
    TAMANHO_POP = TAMANHO_POP   # usa o valor aleatorio gerado

valor = input("Número de gerações (padrão: 50): ")
if valor.strip():
    NUM_GERACOES = int(valor)

valor = input("Taxa de cruzamento (padrão: 0.7): ")
if valor.strip():
    TAXA_CRUZAMENTO = float(valor)

valor = input("Taxa de mutação (pdrão: 0.01): ")
if valor.strip():
    TAXA_MUTACAO = float(valor)

print("\nConfiguração aplicada. Executando o algoritmo.\n")

# ALGORITMO
populacao = gerarPopulacao(TAMANHO_POP) # gera populacao inicial

for geracao in range(NUM_GERACOES):

    # lista que guarda dados dos individuos avaliados
    populacao_avaliada = []     
    for individuo in populacao:
        bits_x = individuo[:12]     # 12 primeiros bits (x)
        bits_y = individuo[12:]     # 12 ultimos bits (y)
        x = codificacao(bits_x)     # decodifica x
        y = codificacao(bits_y)     # decodifica y
        fitness = funObjetivo(x, y) # calcula fitness
        populacao_avaliada.append((individuo, x, y, fitness)) # armazena na lista

    populacao_avaliada.sort(key=lambda t: t[3]) # ordena pela fitness (menor é melhor)
    melhor = populacao_avaliada[0]              # tupla completa do melhor individuo
    media = sum(t[3] for t in populacao_avaliada) / len(populacao_avaliada) 
    
    mediasFit.append(media) # adiciona as medias na lista de medias

    # salva os dados da geracao no arquivo csv
    salvar_dados_csv(
        "resultado.csv",
        [geracao, melhor[3], melhor[1], melhor[2], media]
    )

    nova_pop = [] # nova populacao

    elite = elitismo(populacao_avaliada) # seleciona o elite (melhor individuo)
    nova_pop.append(elite)               # adiciona o elite na nova populacao

    while len(nova_pop) < TAMANHO_POP:              # enquanto a nova populacao nao estiver completa
        pai1 = selecao_torneio(populacao_avaliada)  # seleciona pais por torneio
        pai2 = selecao_torneio(populacao_avaliada)  # seleciona pais por torneio
        f1, f2 = cruzamento_2_pontos(pai1, pai2, TAXA_CRUZAMENTO) # cruzamento de 2 pontos
        f1 = mutacao_inversao(f1, TAXA_MUTACAO)     # mutacao por inversao
        f2 = mutacao_inversao(f2, TAXA_MUTACAO)     # mutacao por inversao
        nova_pop.append(f1)                         # adiciona filhos na nova populacao
        if len(nova_pop) < TAMANHO_POP:             # verifica se ainda cabe mais um filho
            nova_pop.append(f2)                     # adiciona segundo filho na nova populacao

    populacao = nova_pop # atualiza a populacao para a proxima geracao
    
    # gera os graficos a cada geracao
    grafico_linha(mediasFit) 
    grafico(melhor, geracao)
    heatmap()