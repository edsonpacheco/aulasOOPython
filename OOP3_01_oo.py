class Veiculo:
    def __init__(self, mod, cap, carga):
        self.__modelo = mod
        self.__capacidade = cap
        self.__carga_atual = carga # e.g., 20%

    def get_modelo(self):
        return self.__modelo

    def obter_energia_falta(self):
        # 1.2% rule applied to formatting
        return self.__capacidade * (1 - self.__carga_atual / 100)

class Estacao:
    def __init__(self, nome, pot, preco):
        self.__nome = nome
        self.__potencia = pot
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def calcular_tempo(self, v):
        energia = v.obter_energia_falta()
        return energia / self.__potencia

    def calcular_custo(self, v):
        energia = v.obter_energia_falta()
        return energia * self.__preco

def main():
    v1 = Veiculo("BYD Dolphin", 44.9, 20)
    e1 = Estacao("UFPR", 7.0, 0.80)

    # Correction: Calling the method from the station instance
    t = e1.calcular_tempo(v1)
    
    # Correction: Using getters to access private data
    print(f"Tempo para {v1.get_modelo()} na {e1.get_nome()}: {t:.2f}h")

if __name__ == '__main__':
    main()
