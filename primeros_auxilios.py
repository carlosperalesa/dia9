def preguntar(pregunta):
    while True:
        respuesta = input(pregunta + " (s/n): ").lower()
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Por favor conteste con una S o una N segun corresponda")


def primeros_auxilios():
    while True:
        respuesta = preguntar("¿La persona responde a estímulos?")
        if respuesta == "s":
            print("Valorar la necesidad de llevarlo al hospital mas cercano")
            break
        else:
            print("Abrir la vía Aérea")
            respira = preguntar("¿La persona respira?")
            if respira == "s":
                print("Permitirle posicion de suficiente respiración")
                break
            else:
                print("Administrar 5 Ventilaciones y llamar a Ambulancia")
                while True:
                    signos_de_vida = preguntar("¿Signos de vida?")
                    if signos_de_vida == "s":
                        print("Reevaluar a la espera de la Ambulancia")
                    else:
                        print(
                            "Administrar Compresiones Torácicas hasta que llegue ambulancia")
                    llego_ambulancia = preguntar("¿Llegó la ambulancia?")
                    if llego_ambulancia == "s":
                        print("Fin")
                        return


primeros_auxilios()
