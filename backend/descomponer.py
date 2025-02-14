#que vamos a descomponer

'''
el usuario puede adjuntar un excel csv o un archivo de texto plano
debo hacer un scrip que descomponga el archivo en sus partes clave valor y lo guarde en una base de datos
para que el usuario pueda hacer consultas

1. leer el archivo
2. descomponer el archivo
3. guardar en la base de datos
4. hacer graficas
'''

import pandas as pd

def convertir_archivo_a_diccionario(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path, engine="openpyxl")
    else:
        raise ValueError("Formato no soportado. Usa CSV o XLSX.")

    # Eliminar filas completamente vacías
    df.dropna(how='all', inplace=True)

    # Convertir a clave-valor eliminando valores vacíos
    data_dict = [
        {k: v for k, v in row.items() if pd.notna(v) and v != ""}
        for row in df.to_dict(orient="records")
    ]

    return data_dict

# Ejemplo de uso
archivo = "savings.xlsx"  # Reemplaza con el nombre del archivo
resultado = convertir_archivo_a_diccionario(archivo)
print(resultado)  # Lista de diccionarios sin valores vacíos
