

def decodificador(mensaje):
    mensaje_invertido = mensaje[::-1]

    mensaje_final = ""

    for caracter in mensaje_invertido:
        if caracter.isalpha() or caracter.isspace():
            mensaje_final += caracter

    return mensaje_final

mensaje = input("Ingrese el mensaje codificado: ")
mensaje_f = decodificador(mensaje)
print(f"El mensaje final es: {mensaje_f}")
