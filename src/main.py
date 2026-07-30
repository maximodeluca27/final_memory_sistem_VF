"""
Simulador de Paginación de Memoria Virtual
Pipeline: Python (ETL/Simulación) -> SQLite -> Excel (Dashboard)
"""
import os
import sqlite3
import pandas as pd

#RUTAS 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CSV = os.path.join(BASE_DIR, "data", "memory_accesses.csv")
DB_PATH = os.path.join(BASE_DIR, "data", "paging.db")

def simulation_fifo(df,num_frames):

    frames= []  #memoria ram dividida en marcos
    page_table={} #diccionario clave-valor (pid,virtual_page)-> identificación unica de proceso y página virtual
    log= []

    for _, row in df.iterrows():

        time= row["time"]
        pid= row["pid"]
        virtual_page= row["virtual_page"]
        page=(pid, virtual_page)

        if page in page_table:
            page_fault= 0
        else:
            page_fault= 1

            if len(frames) >= num_frames:
                removed= frames.pop(0)
                del page_table[removed]

            frames.append(page)
            page_table[page]= len(frames) -1 #numero de marco fisico donde esta guardado.

    log.append(
            {
                "time": time,
                "pid": pid,
                "virtual_page": virtual_page,
                "page_fault": page_fault,
                "num_frames": num_frames,
                "frames": str(frames),
            }
        )

    return pd.DataFrame(log)

def guardar_en_sql(df):
    conn = sqlite3.connect(DB_PATH) #conecto con la ruta de db

    # Guardar la traza detallada
    df.to_sql("paging_log", conn, if_exists="replace", index=False) #creo la tabla en db con 

    # Crear Vista de Resumen por Configuración
    cur = conn.cursor()
    cur.execute("""
        CREATE VIEW IF NOT EXISTS vw_resumen_frames AS
        SELECT 
            num_frames,
            COUNT(*) AS total_accesos,
            SUM(page_fault) AS total_page_faults,
            ROUND(100.0 * SUM(page_fault) / COUNT(*), 2) AS tasa_page_fault_pct,
            ROUND(100.0 * (1.0 - (1.0 * SUM(page_fault) / COUNT(*))), 2) AS tasa_hit_pct
        FROM paging_log
        GROUP BY num_frames;
    """)

    conn.commit()
    conn.close()
    print(f"\n[OK] Datos guardados con éxito en '{DB_PATH}'.")