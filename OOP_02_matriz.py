"""
Processamento de Matrizes
Objetivo: Demonstrar criação, acesso e iteração em listas de listas.
"""
def exibir_matriz(matriz):
    print("\n--- Estrutura da Matriz ---")
    for linha in matriz:
        # Cada 'linha' é, por si só, uma lista (vetor)
        for valor in linha:
            print(f"[{valor:^5}]", end=" ")
        print() # Quebra de linha física no console

def main():
    linhas = int(input("Número de linhas (ex: instantes de tempo): "))
    colunas = int(input("Número de colunas (ex: sensores): "))
    # Inicialização da matriz com zeros
    matriz = []
    for i in range(linhas):
        nova_linha = []
        for j in range(colunas):
            valor = float(input(f"Valor para [{i}][{j}]: "))
            nova_linha.append(valor)
        matriz.append(nova_linha) # Adiciona a referência da linha à lista principal
    exibir_matriz(matriz)

if __name__ == "__main__":
    main()
