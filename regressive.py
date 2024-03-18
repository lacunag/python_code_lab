import time

def countdown(t):
    while t > 0:
        print(t)
        time.sleep(1)  # Wait for 1 second
        t -= 1

while True:
    time_input = int(input("Ingrese el tiempo de cuenta regresiva en segundos (o ingrese 0 para salir): "))
    if time_input == 0:
        break  # Exit the loop if the user enters 0
    countdown(time_input)
    
    continue_option = input("¿Desea continuar? (s/n): ")
    if continue_option.lower() != 'y':
        break  # Exit the loop if the user does not want to continue

print("¡Cuenta regresiva finalizada!")

