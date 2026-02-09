import pandas as pd
import matplotlib.pyplot as plt

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

def main():
    df = pd.read_parquet(URL)

    cols = ["trip_distance", "total_amount", "payment_type"]
    df = df[[c for c in cols if c in df.columns]].dropna()

    print("Total de viajes:", len(df))

    print("\nEstadísticas básicas:")
    if "trip_distance" in df.columns:
        print("Distancia promedio (millas):", df["trip_distance"].mean())

    if "total_amount" in df.columns:
        print("Pago promedio (USD):", df["total_amount"].mean())

    print("\nMétodos de pago:")
    print(df["payment_type"].value_counts())

    df["trip_distance"].clip(upper=30).hist(bins=50)
    plt.title("Distribución de distancias de viaje")
    plt.xlabel("Millas")
    plt.ylabel("Frecuencia")
    plt.show()

if __name__ == "__main__":
    main()
