from collections import Counter
import re

def analizar_frecuencia_palabras(archivo):
    with open(archivo, 'r') as f:
        texto = f.read().lower()
        palabras = re.findall(r'\b\w+\b', texto)
        contador = Counter(palabras)
        palabras_comunes = contador.most_common()
        return palabras_comunes


archivo = input("Ingrese el nombre del archivo de texto y su extension (txt): ")
palabras_comunes = analizar_frecuencia_palabras(archivo)
    
print("Palabras más comunes:")
for palabra, frecuencia in palabras_comunes:
    print(f"- {palabra}: {frecuencia}")