def main():
    # Criando o dicionário com dados de um sensor 
    # As chaves (strings) funcionam como etiquetas para os valores
    sensor = {                     # <--- Início do Dicionário
        "id": 3103,                # Chave: "id", Valor: 3103
        "tipo": "RPL_Node",        # Chave: "tipo", Valor: "RPL_Node"
        "valor": 25.5,             # Chave: "valor", Valor: 25.5
        "unidade": "Celsius"       # Chave: "unidade", Valor: "Celsius"
    }                              # <--- Fim do Dicionário
    # Acesso rápido via chave
    print(f"--- Telemetria do Sensor {sensor['id']} ---")
    print(f"Leitura: {sensor['valor']} {sensor['unidade']}")

    # Adicionando nova chave em tempo de execução
    sensor["status"] = "Ativo"   
    # Verificando se uma chave existe (segurança)
    if "bateria" in sensor:
        print(f"Bateria: {sensor['bateria']}%")
    else:
        print("Aviso: Nível de bateria não informado.")

if __name__ == "__main__":
    main()
