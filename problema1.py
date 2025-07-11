import pandas as pd
import numpy as np
from scipy.stats import chi2

def analisis_ingreso():
    # Paso 1: Cargar los datos
    df = pd.read_csv("muestra_ech.csv")

    # Paso 2: Calcular ingreso per cápita
    df["ingreso_per_capita"] = df["ingreso"] / df["personas_hogar"]

    # Paso 3: Calcular el percentil 80
    p80 = np.percentile(df["ingreso_per_capita"], 80)

    # Paso 4: Filtrar los hogares del quintil superior (ricos)
    ricos = df[df["ingreso_per_capita"] >= p80]

    # Paso 5: Calcular frecuencias observadas de hogares ricos por departamento
    observadas = ricos["departamento"].value_counts().sort_index()

    # Paso 6: Calcular frecuencias esperadas bajo distribución uniforme
    k = 19  # Número de departamentos
    n = len(ricos)
    esperadas = pd.Series([n / k] * k, index=observadas.index)

    # Paso 7: Calcular el estadístico chi-cuadrado manualmente
    chi2_stat = (((observadas - esperadas) ** 2) / esperadas).sum()

    # Paso 8: Calcular valor crítico y p-valor
    gl = k - 1  # Grados de libertad
    valor_critico = chi2.ppf(0.95, df=gl)
    p_valor = 1 - chi2.cdf(chi2_stat, df=gl)

    # Paso 9: Mostrar resultados
    print("---------------------------------------------------")
    print("Análisis de distribución del ingreso por departamento")
    print("---------------------------------------------------")
    print(f"Chi-cuadrado calculado: {chi2_stat:.2f}")
    print(f"Valor crítico (gl={gl}, α=0.05): {valor_critico:.2f}")
    print(f"p-valor: {p_valor:.4f}")

    if chi2_stat > valor_critico:
        print("→ Se rechaza la hipótesis nula: la distribución NO es uniforme.")
    else:
        print("→ No se rechaza la hipótesis nula: la distribución podría ser uniforme.")