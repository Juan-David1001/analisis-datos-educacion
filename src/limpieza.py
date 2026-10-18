import pandas as pd


def cargar_datos(ruta):
    tabla = pd.read_csv(ruta)
    print("Filas:", len(tabla))
    print("Columnas:", list(tabla.columns))
    return tabla


def tratar_nulos(tabla):

    tabla_limpia = tabla.copy()

    columnas_categoricas = ["estrato", "educacion_madre", "educacion_padre", "internet"]

    # Registrar los nulos antes del tratamiento
    nulos_antes = tabla_limpia[columnas_categoricas].isna().sum()
    filas_con_nulo = int(tabla_limpia.isna().any(axis=1).sum())

    # Reemplazar los valores faltantes con una categoria explicita
    for columna in columnas_categoricas:
        tabla_limpia[columna] = tabla_limpia[columna].fillna("No informado")

    print("Filas con al menos un vacio:", filas_con_nulo)
    print("Nulos por columna antes del tratamiento:")
    print(nulos_antes)

    print("\nNulos despues del tratamiento:")
    print(tabla_limpia.isna().sum())

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
