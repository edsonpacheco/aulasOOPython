import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

if __name__ == "__main__":
    print("Iniciando Etapa 3: Inteligência de Rede...")

    # 1. Carregamento e Downsampling (10% dos dados)
    # O parâmetro low_memory=False é essencial para bases de engenharia em 2026
    df = pd.read_csv('dados_smart_grid/household_power_consumption.txt', 
                    sep=';', na_values=['?'], low_memory=False)
    df = df.iloc[::10].copy()
    df.dropna(inplace=True)

    # 2. Engenharia de Recursos (V_RMS)
    # min_periods=1 evita NaNs no início do processamento
    df['V_RMS'] = df['Voltage'].rolling(window=60, min_periods=1).apply(
        lambda x: np.sqrt(np.mean(x**2))
    )

    # 3. Preparação para Machine Learning
    # Rotulamos como 'Anomalia' (1) tensões abaixo de 232V
    df['Alvo'] = (df['V_RMS'] < 232).astype(int)

    # Selecionamos Features (Variáveis preditoras) e Target (Alvo)
    features = ['V_RMS', 'Global_active_power', 'Global_intensity']
    X = df[features]
    y = df['Alvo']

    # Divisão 80% treino e 20% teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Treinamento do Modelo
    print("Treinando Classificador de Eventos...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # 5. Resultados
    predicoes = modelo.predict(X_test)
    print("\nRelatório de Classificação de Faltas:")
    print(classification_report(y_test, predicoes))
