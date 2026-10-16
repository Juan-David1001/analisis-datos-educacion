import pandas as pd


def cargar_datos(ruta):
    tabla = pd.read_csv(ruta)
    print("Filas:", len(tabla))
    print("Columnas:", list(tabla.columns))
    return tabla


def quitar_nulos(tabla):
    antes = len(tabla)
    tabla_limpia = tabla.dropna()
    print("Se quitaron", antes - len(tabla_limpia), "filas con vacios")
    return tabla_limpia


def quitar_duplicados(tabla):
    antes = len(tabla)
    tabla_limpia = tabla.drop_duplicates()
    print("Se quitaron", antes - len(tabla_limpia), "filas repetidas")
    return tabla_limpia


def resumen(tabla):
    print(tabla.info())
    print(tabla.describe())
    return tabla.describe()
