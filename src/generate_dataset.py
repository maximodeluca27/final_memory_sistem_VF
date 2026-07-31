import os
import random
import pandas as pd

# Definir la ruta de salida
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "memory_accesses.csv")

def generar_accesos(num_registros=1000):
    random.seed(42)  # Semilla fija para reproducibilidad, misma para cada uno que ejecuta.

    procesos = [101, 102, 103]  # PIDs simulados
    registros = []

    time = 1
    for _ in range(num_registros):
        pid = random.choice(procesos)

        # Simular patrones de acceso (localidad de referencia)
        modo = random.random()

        if modo < 0.6:
            # 60% Accesos con localidad (páginas cercanas entre 0 y 15). MUY PROBABLE.
            virtual_page = random.randint(0, 15)
        elif modo < 0.9:
            # 30% Accesos a páginas de rango medio (16 a 40). MEDIO PROBABLE.
            virtual_page = random.randint(16, 40)
        else:
            # 10% Accesos a páginas distantes/raras (41 a 80). MUY POCO PROBABLE.
            virtual_page = random.randint(41, 80)

        registros.append(
            {"time": time, "pid": pid, "virtual_page": virtual_page}
        )

        time += 1

    # Asegurar que la carpeta data exista
    data_dir = os.path.dirname(OUTPUT_CSV)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Crear el DataFrame y exportar
    df = pd.DataFrame(registros)
    df.to_csv(OUTPUT_CSV, index=False)
    print(
        f"[OK] Dataset generado exitosamente con {len(df)} registros en: '{OUTPUT_CSV}'"
    )


if __name__ == "__main__":
    generar_accesos()