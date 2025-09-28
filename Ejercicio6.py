def inventario_personajes(personajes):
    """
    Recibe un diccionario {nombre: tipo} y devuelve:
    - Lista de humanos ordenados alfabéticamente.
    - Lista de criaturas ordenadas por longitud de nombre.
    """
    humanos = [nombre for nombre, tipo in personajes.items() if tipo == "humano"]
    criaturas = [nombre for nombre, tipo in personajes.items() if tipo == "criatura"]

    humanos_ordenados = sorted(humanos)
    criaturas_ordenadas = sorted(criaturas, key=len)

    return humanos_ordenados, criaturas_ordenadas

# Ejemplo de uso
if __name__ == "__main__":
    personajes = {
        "Aragorn": "humano",
        "Legolas": "criatura",
        "Gimli": "criatura",
        "Boromir": "humano",
        "Frodo": "humano",
        "Gollum": "criatura"
    }
    humanos, criaturas = inventario_personajes(personajes)
    print("Humanos ordenados:", humanos)
    print("Criaturas ordenadas:", criaturas)