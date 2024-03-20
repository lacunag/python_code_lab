# Este script analiza la frecuencia de las palabras en un archivo de texto dado.
# Utiliza expresiones regulares para dividir el texto en palabras, luego cuenta la frecuencia de cada palabra.
# Finalmente, imprime las palabras más comunes junto con su frecuencia.
from collections import Counter
import re

def analyze_word_frequency(file):
    with open(file, 'r') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w+\b', text)
        counter = Counter(words)
        common_words = counter.most_common()
        return common_words


file = input("Ingrese el nombre del archivo de texto y su extension (txt): ")
common_words = analyze_word_frequency(file)
    
print("Palabras más comunes:")
for word, frequency in common_words:
    print(f"- {word}: {frequency}")
