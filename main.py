from problema1 import analisis_ingreso
from problema2 import comparacion_velocidades

def main():
    print("=== MENÚ DE ANÁLISIS ESTADÍSTICO ===")
    print("1. Análisis de distribución del ingreso (Chi-cuadrado)")
    print("2. Comparación de medias de velocidad de internet (Test t de Welch)")

    while True:
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == "1":
            print("\nEjecutando análisis de distribución del ingreso...\n")
            analisis_ingreso()
            break
        elif opcion == "2":
            print("\nEjecutando comparación de velocidades (test t)...\n")
            comparacion_velocidades()
            break
        else:
            print("Opción inválida. Por favor seleccione 1 o 2.")

if __name__ == "__main__":
    main()

