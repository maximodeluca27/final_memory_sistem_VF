# 💻 Memory Paging Simulator & Analytics

Este proyecto es un simulador de gestión de memoria virtual enfocado en el algoritmo de reemplazo de páginas **FIFO (First-In, First-Out)**. Evalúa el impacto en la tasa de fallos de página (*Page Faults*) y aciertos (*Hit Rate*) a medida que varía la cantidad de marcos de memoria asignados (*Frames*).

Los resultados de las simulaciones son persisitidos en una base de datos relacional **SQLite** (`paging.db`) para su posterior ingesta, modelado y análisis visual a través de **Power Query** y un **Dashboard en Excel**.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Base de Datos:** SQLite 3
- **Data Analytics:** Power Query & Microsoft Excel (ODBC Driver / SQLite OLEDB)
- **Control de Versiones:** Git & GitHub

---

## 📊 Resultados y Análisis de Rendimiento

A partir de la simulación ejecutada sobre una traza de **1.000 accesos a memoria**, se evaluaron configuraciones de **1, 2, 4, 8 y 16 marcos de memoria**. Los resultados consolidados exportados desde `paging.db` son los siguientes:

| Marcos (Frames) | Total Accesos | Page Faults | Tasa de Fallo (%) | Hit Rate (%) |
|:---------------:|:-------------:|:-----------:|:-----------------:|:------------:|
| **1**           | 1000          | 980         | 98.0%             | 2.0%         |
| **2**           | 1000          | 961         | 96.1%             | 3.9%         |
| **4**           | 1000          | 961         | 96.1%             | 3.9%         |
| **8**           | 1000          | 961         | 96.1%             | 3.9%         |
| **16**          | 1000          | 39          | 3.9%              | 96.1%        |

---

## 💡 Conclusiones Técnicas

1. **Punto de Inflexión Crítico:** Se evidencia un salto drástico de rendimiento al alcanzar los **16 marcos de memoria**, pasando de un escaso **3.9% de Hit Rate** con 8 marcos a un **96.1% de Hit Rate**.
2. **Comportamiento en Marcos Intermedios:** Entre 2, 4 y 8 marcos la tasa de fallos se mantiene constante (96.1%), lo que demuestra cómo la estructura y repetición de la traza de accesos exige una cantidad mínima de marcos para alojar el conjunto de trabajo (*Working Set*) del proceso.
3. **Integración con BI/Analytics:** La arquitectura desacoplada permite alimentar dashboards ejecutivos en tiempo real conectando la base SQLite directamente con herramientas de BI/Excel vía Power Query.

---

## 📁 Estructura del Repositorio

```text
final_memory_sistem_VF/
│
├── paging.db                  # Base de datos SQLite con los resultados de simulación
├── main.py                    # Script ejecutor de la simulación FIFO
├── dashboard/
│   └── Paging_Analytics.xlsx  # Dashboard en Excel conectado vía Power Query a SQLite
└── README.md                  # Documentación del proyecto
