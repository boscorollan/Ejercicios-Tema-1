def ahorro(cant_inicial, cant_mensual, meses):
    total = cant_inicial + (cant_mensual * meses)
    if total >= 5000:
        print(f"Felcidades has ahorrado {total}")
    else:
        print(f"Has ahorrado {total} euros en {meses} meses.")
cantidad_inicial = float(input("Ingrese la cantidad inicial: "))
cantidad_mensual = float(input("Ingrese la cantidad mensual a ahorrar: "))
meses = int(input("Ingrese la cantidad de meses que va a ahorrar: "))

ahorro(cantidad_inicial, cantidad_mensual, meses)