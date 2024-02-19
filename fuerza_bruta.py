from string import ascii_lowercase


def fuerza_bruta():
    password = input("Ingrese el password: ").lower()
    intento = ''
    intentos = 0
    for i, _ in enumerate(password):
        for letra in ascii_lowercase:
            intentos += 1
            print(f'Intento {intentos}: {intento + letra}')
            if letra == password[i]:
                intento += letra
                break
    print(f"\nLa contraseña fue forzada en {intentos} intentos")


fuerza_bruta()
