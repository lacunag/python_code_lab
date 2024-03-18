import time

def countdown(t):
    while t > 0:
        print(t)
        time.sleep(1)  # Espera 1 segundo
        t -= 1

while True:
    tiempo_ingresado = int(input("Ingrese el tiempo de cuenta regresiva en segundos (o ingrese 0 para salir): "))
    if tiempo_ingresado == 0:
        break  # Salir del bucle si el usuario ingresa 0
    countdown(tiempo_ingresado)
    
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break  # Salir del bucle si el usuario no desea continuar

print("¡Cuenta regresiva finalizada!")
