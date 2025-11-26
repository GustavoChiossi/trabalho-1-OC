# == BIBLIOTECAS 
import random 
# As bibliotecas pesadas (matplotlib, csv, logging) foram movidas para data.py

# IMPORTAÇÕES DOS SEUS MÓDULOS
from funcoes import * # Lógica do AG (Torneio, Cruzamento, etc)
from data import * # Dados (Logs, CSV, Gráficos)

# == CONFIGURACOES INICIAIS

# 1. Prepara as pastas (Log, CSV, Graficos)
setup_diretorios()

# 2. Configura o Logger
logger = configurar_logger("teste_inicial.log")
logger.info("=== Iniciando Execução do Algoritmo Genético ===")

# valores iniciais da funcao (apenas referência)
x = 4.00 
y = 3.53 
z = 24.3212

# teste inicial
logger.info("Gerando população inicial...")
pop = gerarPopulacao(10)  

resultados = [] # lista
for individuo in pop:
    x_bits = individuo[:12] 
    y_bits = individuo[12:] 
    x = codificacao(x_bits)
    y = codificacao(y_bits)
    fitness = funObjetivo(x, y)
    resultados.append((individuo, x, y, fitness)) 

# seleciona o individuo com o menor valor (fitness)
melhor = min(resultados, key=lambda t: t[3]) 

# == RESULTADOS DOS TESTES INICIAIS
# Usando o logger em vez de print (aparece na tela E salva no arquivo)
logger.info(f"Melhor indivíduo: Bits: {melhor[0]}")
logger.info(f"x: {melhor[1]:.3f} | y: {melhor[2]:.3f}")
logger.info(f"fitness: {melhor[3]:.3f}")

print("\n--- Testando Operadores ---")

# 1. Selecionar dois pais usando o Torneio
pai1 = selecao_torneio(resultados, k=3)
pai2 = selecao_torneio(resultados, k=3)

logger.info(f"Pai 1 selecionado: {pai1}")
logger.info(f"Pai 2 selecionado: {pai2}")

# 2. Realizar o cruzamento
filho_a, filho_b = cruzamento_2_pontos(pai1, pai2)

logger.info(f"Filho A gerado:    {filho_a}")
logger.info(f"Filho B gerado:    {filho_b}")

print("\n--- Teste de Elitismo ---")
melhor_bits = elitismo(resultados)
logger.info(f"Indivíduo preservado pelo elitismo: {melhor_bits}")

# == EXEMPLO DE COMO USAR AS FUNÇÕES DE DADOS (DATA.PY) ==

# Exemplo: Salvando no CSV (Simulando a Geração 0)
# Formato: [Geracao, Melhor Fitness, X, Y, Media(opcional)]
salvar_dados_csv("historico_execucao.csv", [0, melhor[3], melhor[1], melhor[2], 0.0])

# Exemplo: Plotando gráfico (Simulação com dados falsos só para testar)
historico_teste = [13.0, 10.5, 8.2, 5.1, 3.0, 1.5, 0.0]
plotar_grafico_convergencia(historico_teste, "grafico_teste.png")