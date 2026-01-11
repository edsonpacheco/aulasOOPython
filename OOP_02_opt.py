"""
Exemplo de Parâmetros Opcionais 
"""
# REGRA DE OURO: Parâmetros obrigatórios (id_sensor) sempre vêm PRIMEIRO.
# Parâmetros opcionais (limiar, intervalo) vêm depois com um valor padrão.
def processar_sensor(id_sensor, limiar=25.0, intervalo=10):
    print(f"\n[CONFIG] Sensor ID: {id_sensor}")
    print(f"         Limiar de Alerta: {limiar} C")
    print(f"         Intervalo de Leitura: {intervalo}s")

def main():
    # O Python assume limiar=25.0 e intervalo=10
    processar_sensor(3103) 

    # O Python segue a ordem: id_sensor=3104, limiar=30.5, intervalo=10
    processar_sensor(3104, 30.5)

    # 3. Chamada Definindo todos os parâmetros
    processar_sensor(3105, 20.0, 5)

if __name__ == "__main__":
    main()
