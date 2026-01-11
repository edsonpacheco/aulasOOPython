"""
Objetivo: Mostrar como o Python gera índices para as chaves.
"""

def main():
    chaves = ["sensor_3103", "temperatura", "status", "sensor_3103"]
    print(f"{'CHAVE':<15} | {'HASH (ÍNDICE)':<20}")
    print("-" * 40)
    
    for c in chaves:
        # A função hash() retorna um número inteiro único para cada objeto imutável
        # É esse número que garante a busca em O(1)
        h = hash(c)
        print(f"{c:<15} | {h:<20}")

    # Demonstração: chaves iguais SEMPRE geram o mesmo hash na mesma execução
    # Isso permite que sensor["id"] encontre o valor instantaneamente
    if hash("sensor_3103") == hash("sensor_3103"):
        print("\n[OK] Chaves idênticas apontam para o mesmo local na memória.")
if __name__ == "__main__":
    main()
