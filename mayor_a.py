import sys


def filtrar_ventas(ventas, umbral):
    return {mes: valor for mes, valor in ventas.items() if valor > umbral}


def main():
    ventas = {
        "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000,
        "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200,
        "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000,
    }
    umbral = int(sys.argv[1])
    ventas_filtradas = filtrar_ventas(ventas, umbral)
    print(ventas_filtradas)


if __name__ == "__main__":
    main()

# python mayor_a.py 40000
