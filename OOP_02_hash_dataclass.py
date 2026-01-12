from dataclasses import dataclass # import/include

#  Definimos o "molde" (Data Type) para o nosso sensor
@dataclass
class Sensor:
    temperatura: float
    energia: float
    protocolo: str

def main():
    # Nosso "banco de dados" agora mapeia ID -> Instância de Sensor
    rede_sensores: dict[int, Sensor] = {}
    # Simulando a captura de dados de 2 sensores diferentes
    ids_encontrados = [3103, 3105]

    for node_id in ids_encontrados:
        # Criamos o objeto Sensor de forma muito mais legível
        rede_sensores[node_id] = Sensor(
            temperatura=24.0 + (node_id % 10),
            energia=100.0,
            protocolo="RPL"
        )
    #  Acessando via "Dot Notation" (Ponto) - O editor autocompleta
    temp_3103 = rede_sensores[3103].temperatura
    print(f"Temperatura do Mote 3103: {temp_3103} C")

    # Atualizando um campo de forma direta e segura
    rede_sensores[3105].energia = 85.5

    # Exibindo o relatório completo
    print("\n--- Estado Atual da Rede (via Dataclasses) ---")
    for mote_id, sensor in rede_sensores.items():
        print(f"ID: {mote_id} | Status: {sensor.protocolo} | Bateria: {sensor.energia}%")

if __name__ == "__main__":
    main()
