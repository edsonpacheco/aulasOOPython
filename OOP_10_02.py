import pandas as pd
import numpy as np

if __name__ == "__main__":
    print("Iniciando Pipeline de Energia...")
    
    # 1. Carregamento (Carga Total)
    df = pd.read_csv('dados_smart_grid/household_power_consumption.txt', 
                    sep=';', na_values=['?'], low_memory=False)
    
    # 2. DOWNSAMPLING: Reduzimos para 10% do volume original (Decimação)
    # Pegamos uma amostra a cada 10 minutos (já que a base é por minuto)
    df = df.iloc[::10].copy()
    print(f"Dados decimados. Novo tamanho: {len(df)} linhas.")

    # 3. Limpeza
    df.dropna(inplace=True)

    # 4. Cálculo de V_RMS
    # min_periods=1 garante que não teremos NaNs no início do DataFrame
    df['V_RMS'] = df['Voltage'].rolling(window=60, min_periods=1).apply(
        lambda x: np.sqrt(np.mean(x**2))
    )

    # Exibindo o resultado sem NaNs
    print("\nResultado do Processamento (Primeiras 5 linhas):")
    print(df[['Voltage', 'V_RMS']].head())
