# Este script implementa una cuenta regresiva en segundos. 
# El usuario puede ingresar un tiempo en segundos para iniciar la cuenta regresiva.
# Después de cada cuenta regresiva, se le pregunta al usuario si desea continuar con otra cuenta regresiva o salir del programa.
# Utiliza la función countdown para realizar la cuenta regresiva y time.sleep para esperar un segundo entre cada paso.
import time

def countdown(t):
    while t > 0:
        print(t)
        time.sleep(1)  # Esperar durante 1 segundo
        t -= 1

while True:
    time_input = int(input("Ingrese el tiempo de cuenta regresiva en segundos (o ingrese 0 para salir): "))
    if time_input == 0:
        break  # Salir del bucle si el usuario ingresa 0
    countdown(time_input)
    
    continue_option = input("¿Desea continuar? (s/n): ")
    if continue_option.lower() != 's':
        break  # Salir del bucle si el usuario no desea continuar

print("¡Cuenta regresiva finalizada!")


