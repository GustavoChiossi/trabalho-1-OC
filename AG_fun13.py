import random           
from funcoes import *   # modulo de logica do AG
from data import *      # modulo de csv e graficos

# == CONFIGURACOES INICIAIS

# prepara as pastas 
setup_diretorios()

# valores base da funcao
# (tem que pedir pro professor se tem que usar ou não)
x = 4.00 
y = 3.53 
z = 24.3212

# teste inicial
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

print("--- Resultados Iniciais ---")
print(f"Melhor indivíduo: Bits: {melhor[0]}")
print(f"x: {melhor[1]:.3f} | y: {melhor[2]:.3f}")
print(f"fitness: {melhor[3]:.3f}")

print("\n--- Testando Operadores ---")

# selecionar dois pais usando o Torneio
pai1 = selecao_torneio(resultados, k=3)
pai2 = selecao_torneio(resultados, k=3)

print(f"Pai 1 selecionado: {pai1}")
print(f"Pai 2 selecionado: {pai2}")

# realizar o cruzamento
filho_a, filho_b = cruzamento_2_pontos(pai1, pai2)

print(f"Filho A gerado:    {filho_a}")
print(f"Filho B gerado:    {filho_b}")

print("\n--- Teste de Elitismo ---")
melhor_bits = elitismo(resultados)
print(f"Indivíduo preservado pelo elitismo: {melhor_bits}")

# Teste de Mutação
filho_a_mutado = mutacao_inversao(filho_a, taxa_mutacao=0.01)
filho_b_mutado = mutacao_inversao(filho_b, taxa_mutacao=0.01)

print(f"Filho A mutado:    {filho_a_mutado}")
print(f"Filho B mutado:    {filho_b_mutado}") 

# == EXEMPLO DE COMO USAR AS FUNÇÕES DE DADOS (DATA.PY) 

# Exemplo: Salvando no CSV (Simulando a Geração 0)
# Formato: [Geracao, Melhor Fitness, X, Y, Media(opcional)]
salvar_dados_csv("historico_execucao.csv", [0, melhor[3], melhor[1], melhor[2], 0.0])

# Exemplo: Plotando gráfico (Simulação com dados falsos só para testar)
historico_teste = [13.0, 10.5, 8.2, 5.1, 3.0, 1.5, 0.0]
plotar_grafico_convergencia(historico_teste, "grafico_teste.png")