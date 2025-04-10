import json
import os

# Ruta del archivo JSON
archivo_json = os.path.expanduser("~/Documents/myfile.json")

try:
    # Abre y lee el archivo JSON
    with open(archivo_json, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)  # Mostrar contenido del archivo antes de procesarlo

        # Cargar el archivo JSON como objeto Python
        json_file = json.load(archivo)
        print("Contenido del archivo JSON cargado exitosamente como objeto:")
        print(json_file)  # Muestra el contenido del archivo JSON como objeto

        # Convertir el objeto Python en string para 'ourjson'
        ourjson = json.dumps(json_file)
        print("Contenido del archivo JSON cargado exitosamente en el string 'ourjson':")
        print(ourjson)  # Muestra el contenido del archivo JSON en formato string

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_json}' no se encuentra en la máquina virtual.")
except json.JSONDecodeError:
    print("Error: El archivo no contiene un JSON válido.")
except Exception as e:
    print(f"Error inesperado: {e}")
