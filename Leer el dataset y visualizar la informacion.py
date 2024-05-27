import pandas as pd

url = 'https://raw.githubusercontent.com/Mav3r5ck/MiDataSeEjemplo/main/uso_de_memoria.txt'

try: 
    df = pd.read_csv(url)
    print("Primeras filas del dataset:")
    print(df.head())
except Exception as e:
    print("Error al leer el dataset:", e)
