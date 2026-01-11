import numpy as np # O apelido 'np' é a convenção universal
def main():
    # Criando vetores (ndarrays)
    # Simulando 5 leituras de temperatura de sensores 
    leituras = np.array([25.4, 26.1, 24.8, 25.9, 27.2]) 
  
    # Operação Vetorizada: Soma 2.0 em todos os elementos de uma vez!
    ajustado = leituras + 2.0
    
    # Estatísticas instantâneas (essencial para seu artigo IEEE)
    print(f"Temperaturas: {ajustado}")
    print(f"Média: {np.mean(leituras):.2f}")
    print(f"Desvio Padrão: {np.std(leituras):.2f}") #

    # Criando uma Matriz 2x3 (2 instantes, 3 sensores)
    matriz_sensores = np.array([
        [20, 21, 22],
        [25, 26, 27]
    ])
    
    # Transposta da Matriz (inverte linhas por colunas)
    print("\nMatriz Transposta:")
    print(matriz_sensores.T)

if __name__ == "__main__":
    main()
