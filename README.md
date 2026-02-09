# NYC Taxi Analysis 🚕

Proyecto de análisis exploratorio simple sobre los viajes en taxi amarillo de la ciudad de Nueva York.

## Objetivo
Analizar de forma introductoria:
- Cantidad de viajes
- Distancia promedio de los recorridos
- Monto total promedio
- Métodos de pago más utilizados

## Fuente de datos
Datos públicos de la **NYC Taxi & Limousine Commission (TLC)**, correspondientes a viajes mensuales en formato Parquet.

## Estructura del proyecto
nyc-taxi-analysis/
├── data/
│ ├── raw/
│ └── processed/
├── docs/
├── notebooks/
├── src/
│ └── analysis.py
├── .gitignore
├── README.md
└── requirements.txt

## Ejecución
1. Instalar dependencias:
```bash
pip install -r requirements.txt

2. Ejecutar análisis:
python src/analysis.py

## Alcance
Este proyecto tiene fines académicos y utiliza un análisis exploratorio básico.