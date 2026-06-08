import pandas as pd
import numpy as np
import os
import multiprocessing

import requests
import zipfile
import io

# Endereço da base de dados de consumo da UCI
url = "https://archive.ics.uci.edu/static/public/235/individual+household+electric+power+consumption.zip"

def baixar_dados(url_fonte):
    print("Iniciando download...")
    resposta = requests.get(url_fonte)  
    # O objeto 'resposta' contem o binario do arquivo
    com_zip = zipfile.ZipFile(io.BytesIO(resposta.content))
    com_zip.extractall("./dados_smart_grid")
    print("Dados extraídos com sucesso!")
# Execução

    
def pipeline_diagnostico(df_set):
    """
    Executa a engenharia de recursos e avalia os alertas de forma vetorizada.
    """
    # Cria uma cópia para evitar o aviso SettingWithCopyWarning do pandas
    df_local = df_set.copy()
    
    # Substituição da função lambda por operação vetorizada para permitir a serialização (pickle)
    df_local['V_RMS'] = np.sqrt((df_local['Voltage'] ** 2).rolling(window=10, min_periods=1).mean())
    
    # Contagem de alertas baseada na condição estabelecida
    alertas = int((df_local['V_RMS'] < 232).sum())
    return alertas

if __name__ == "__main__":
    baixar_dados(url)

    print("Sistema de Monitoramento Distribuído UFPR - v3")
    cores = os.cpu_count()
    print(f"Cores detectados: {cores}")

    # 1. Carga e tratamento inicial dos dados
    # Certifique-se de que o caminho do arquivo e o nome das colunas estejam corretos
    df = pd.read_csv('dados_smart_grid/household_power_consumption.txt', 
                     sep=';', na_values=['?'], nrows=200000, low_memory=False)
    df.dropna(subset=['Voltage'], inplace=True)
    df['Voltage'] = pd.to_numeric(df['Voltage'])
    
    # Dividindo o dataframe em 4 partes de forma compatível
    subestacoes = np.array_split(df, 4)

    # 2. Execução Paralela
    with multiprocessing.Pool(processes=4) as pool:
        print("Iniciando análise paralela das subestações...")
        resultados = pool.map(pipeline_diagnostico, subestacoes)

    # 3. Consolidação dos Resultados
    for i, alertas in enumerate(resultados):
        status = "CRÍTICO" if alertas > 0 else "NORMAL"
        print(f"Subestação {i}: {alertas} anomalias detectadas -> STATUS: {status}")
