from dataclasses import dataclass

@dataclass
class Veiculo:
    modelo: str
    capacidade: float  # kWh
    carga_atual: float # %

@dataclass
class Estacao:
    nome: str
    potencia: float   # kW
    preco_kwh: float  # R$

def calcular_tempo(v: Veiculo, e: Estacao):
    energia_falta = v.capacidade * (1 - v.carga_atual / 100)
    return energia_falta / e.potencia

def calcular_custo(v: Veiculo, e: Estacao):
    energia_falta = v.capacidade * (1 - v.carga_atual / 100)
    return energia_falta * e.preco_kwh

# =============================================================================
# MAIN
# =============================================================================

def main():
    v1 = Veiculo("BYD Dolphin", 44.9, .20)
    e1 = Estacao("Eletroposto UFPR", 7.0, 0.80)
    t = calcular_tempo(v1, e1)
    print(f"Tempo de carga para {v1.modelo} na {e1.nome}: {t:.2f} horas")

if __name__ == '__main__':
    main()
