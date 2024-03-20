# Este script de Python está diseñado para procesar archivos CSV en un directorio específico.
# Su función principal es convertir archivos CSV con cualquier delimitador en archivos CSV con el delimitador ';'
# El resultado se graba en un nuevo directorio llamado 'processed'.
import csv
import os

def process_csv(input_file):
    # Comprobamos si el directorio 'procesados' existe, y si no, lo creamos
    if not os.path.exists('procesados'):
        os.makedirs('procesados')

    # Creamos el nombre del archivo de salida en el directorio 'procesados'
    output_name = os.path.join('procesados', os.path.basename(input_file))

    # Abrimos el archivo de entrada en modo lectura
    with open(input_file, 'r') as input:
        # Leemos el archivo CSV con el delimitador detectado automáticamente
        csv_dialect = csv.Sniffer().sniff(input.read(1024))
        input.seek(0)  # Volver al inicio del archivo
        csv_reader = csv.reader(input, dialect=csv_dialect)

        # Leemos todas las filas y escribimos en el nuevo archivo con delimitador ';'
        with open(output_name, 'w', newline='') as output:
            csv_writer = csv.writer(output, delimiter=';')
            for row in csv_reader:
                csv_writer.writerow(row)

    print(f"Procesamiento completado para {input_file}. El resultado se encuentra en: {output_name}")

# Directorio que contiene los archivos CSV a procesar (mismo directorio que el script)
input_directory = os.getcwd()

# Iteramos sobre todos los archivos en el directorio de entrada
for input_file in os.listdir(input_directory):
    if input_file.endswith(".csv"):
        full_path = os.path.join(input_directory, input_file)
        process_csv(full_path)
