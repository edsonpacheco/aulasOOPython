"""
Cálculo de Média com Vetor
Objetivo: Demonstrar entrada de dados, armazenamento em lista e funções.
"""
def calcular_media(valores):
    # 'valores' recebe o endereço base da lista na memória
    if not valores:
        return 0.0
    
    soma = sum(valores)
    media = soma / len(valores)
    return media
def main():
    leituras = []
    n = int(input("Quantos sensores deseja processar? ")) # Casting para int
    for i in range(n):
        # O input() retorna string, convertemos para float para precisão
        valor = float(input(f"Digite a temperatura do sensor {i}: "))
        leituras.append(valor) # Adiciona ao final do vetor contíguo
    media_final = calcular_media(leituras)
    print(f"Média das {n} leituras: {media_final:.2f} C")
if __name__ == "__main__":
    main()
