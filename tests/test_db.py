import os
import sqlite3
import pandas as pd

# Encuentra la raíz del proyecto sin importar dónde ejecutes el script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "paging.db")

conn = sqlite3.connect(DB_PATH)
try:
    df = pd.read_sql_query("SELECT * FROM vw_resumen_frames;", conn)
    print("\n--- RESULTADOS EN LA BASE SQLITE ---")
    print(df)
except Exception as e:
    print("Error al consultar:", e)
finally:
    conn.close()