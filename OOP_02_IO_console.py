"""
Objetivo: Demonstrar entrada de dados, casting e f-strings.
"""
def main():
    # Entrada de dados (sempre string)
    nome = input("Digite o nome do sensor: ")
    
    #  Casting necessário para cálculos
    # Note que se o usuário digitar letras, ocorrerá um ValueError
    leituras = int(input("Número de mensagens enviadas: "))
    energia = float(input("Consumo de energia (mJ): "))

    # 3. Saída formatada com f-string (Python 3.6+)
    # :.2f limita as casas decimaisa
    print(f"\n--- Relatório: {nome} ---")
    print(f"Mensagens: {leituras}")
    print(f"Média de energia por mensagem: {energia/leituras:.4f} mJ")

if __name__ == "__main__":
    main()
