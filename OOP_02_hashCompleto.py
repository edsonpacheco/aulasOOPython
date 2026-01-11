"""
Objetivo: Mapear ID de sensor para uma estrutura de dados completa.
"""
def main():
    # Nosso "banco de dados" em memória RAM
    rede_sensores = {}
    # Simulando a captura de dados de 2 sensores diferentes
    ids_encontrados = [3103, 3105]
    for node_id in ids_encontrados:
        # Criamos uma chave para o ID e atribuímos um NOVO dicionário como valor
        rede_sensores[node_id] = {
            "temperatura": 24.0 + (node_id % 10), # Simulação de dado
            "energia": 100.0,
            "protocolo": "RPL"
        }

    # Acessando um dado específico de um sensor específico
    print(f"Temperatura do Mote 3103: {rede_sensores[3103]['temperatura']} C")
    # Adicionando uma nova leitura a um sensor existente
    rede_sensores[3105]["energia"] = 85.5
    # Exibindo o relatório completo
    print("\n--- Estado Atual da Rede ---")
    for mote, dados in rede_sensores.items():
        print(f"ID: {mote} | Status: {dados['protocolo']} | Bateria: {dados['energia']}%")

if __name__ == "__main__":
    main()
