import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import multiprocessing
import os

# Função que encapsula o conhecimento do Engenheiro (Pipeline)
def pipeline_diagnostico(df_set):
    # Engenharia de Recursos
    df_set['V_RMS'] = df_set['Voltage'].rolling(window=10, min_periods=1).apply(
        lambda x: np.sqrt(np.mean(x**2))
    )
    
    # Simulação de Classificação baseada no modelo treinado anteriormente
    # (Em um sistema real, o objeto 'modelo' seria carregado aqui)
    alertas = (df_set['V_RMS'] < 232).sum()
    return alertas

if __name__ == "__main__":
    print(f"Sistema de Monitoramento Distribuído UFPR - 2026")
    print(f"Cores detectados: {os.cpu_count()}")

    # 1. Carga e Particionamento (Simulando 4 subestações diferentes)
    df = pd.read_csv('dados_smart_grid/household_power_consumption.txt', 
                    sep=';', na_values=['?'], nrows=200000, low_memory=False)
    df.dropna(inplace=True)
    
    # Dividindo o dataframe em 4 partes para processamento paralelo
    subestacoes = np.array_split(df, 4)

    # 2. Execução Paralela (O pulo do gato)
    with multiprocessing.Pool(processes=4) as pool:
        print("Iniciando análise paralela das subestações...")
        resultados = pool.map(pipeline_diagnostico, subestacoes)

    # 3. Consolidação dos Resultados
    for i, alertas in enumerate(resultados):
        status = "CRÍTICO" if alertas > 0 else "NORMAL"
        print(f"Subestação {i}: {alertas} anomalias detectadas -> STATUS: {status}")
