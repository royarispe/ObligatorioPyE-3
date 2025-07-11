import pandas as pd
import numpy as np
from scipy.stats import t

#ruta del archivo de datos
archivo = "velocidad_internet_ucu" 

#carga de datos
df = pd.read_csv(archivo)

#paso 1: filtrar datos de Central y Semprun
df_filtrado = df[df["Edificio"].isin(["Central", "Semprún"])]

#paso 2: calcular estadisticas por grupo
stats = df_filtrado.groupby("Edificio")["Velocidad Mb/s"].agg(["mean", "std", "count"])

mean_central = stats.loc["Central", "mean"]
std_central = stats.loc["Central", "std"]
n_central = stats.loc["Central", "count"]

mean_semprun = stats.loc["Semprún", "mean"]
std_semprun = stats.loc["Semprún", "std"]
n_semprun = stats.loc["Semprún", "count"]

#paso 3: calcular estadistico t (Welch)
numerador = mean_central - mean_semprun
denominador = np.sqrt((std_central**2) / n_central + (std_semprun**2) / n_semprun)
t_stat = numerador / denominador

#paso 4: calcular grados de libertad con Welch
num_df = ((std_central**2) / n_central + (std_semprun**2) / n_semprun) ** 2
den_df = (((std_central**2) / n_central) ** 2) / (n_central - 1) + \
         (((std_semprun**2) / n_semprun) ** 2) / (n_semprun - 1)
df_welch = num_df / den_df

#paso 5: calcular p-valor
p_value = t.cdf(t_stat, df_welch)

#paso 6: evaluar hipotesis
alpha = 0.05
rechazar_h0 = p_value < alpha

print("Resultados del análisis")
print("--------------------------")
print(f"Media Central: {round(mean_central, 2)} Mb/s")
print(f"Media Semprún: {round(mean_semprun, 2)} Mb/s")
print(f"Estadístico t: {round(t_stat, 4)}")
print(f"Grados de libertad: {round(df_welch, 2)}")
print(f"p-valor: {round(p_value, 4)}")
print(f"¿Se rechaza H₀ al 5%?: {'Sí' if rechazar_h0 else 'No'}")
