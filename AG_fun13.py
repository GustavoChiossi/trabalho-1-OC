import random
from funcoes import *
from data import *

# CONFIG INICIAL 
setup_diretorios()
mediasFit = []
tamanho_pop = random.randint(10, 30)   
num_geracoes = 5                     

print(f"População inicial: {tamanho_pop}")

populacao = gerarPopulacao(tamanho_pop)

for geracao in range(num_geracoes):

    populacao_avaliada = []
    for individuo in populacao:
        bits_x = individuo[:12]
        bits_y = individuo[12:]
        x = codificacao(bits_x)
        y = codificacao(bits_y)
        fitness = funObjetivo(x, y)
        populacao_avaliada.append((individuo, x, y, fitness))

    populacao_avaliada.sort(key=lambda t: t[3])
    melhor = populacao_avaliada[0]
    media = sum(t[3] for t in populacao_avaliada) / len(populacao_avaliada)
    
    mediasFit.append(media)

    salvar_dados_csv(
        "resultado.csv",
        [geracao, melhor[3], melhor[1], melhor[2], media]
    )

    nova_pop = []

    elite = melhor[0]
    nova_pop.append(elite)

    while len(nova_pop) < tamanho_pop:
        pai1 = selecao_torneio(populacao_avaliada)
        pai2 = selecao_torneio(populacao_avaliada)
        f1, f2 = cruzamento_2_pontos(pai1, pai2)
        f1 = mutacao_inversao(f1)
        f2 = mutacao_inversao(f2)
        nova_pop.append(f1)
        if len(nova_pop) < tamanho_pop:
            nova_pop.append(f2)

    populacao = nova_pop
    
    grafico_linha(mediasFit)
    grafico(melhor, geracao)