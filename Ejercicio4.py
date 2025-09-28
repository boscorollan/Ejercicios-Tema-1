def analizar_notas(notas):
    media = sum(notas) / len(notas)
    
    nota_max = max(notas)
    nota_min = min(notas)
    
    # Comprobamos si hay alguna suspensa
    hay_suspenso = any(n < 5 for n in notas)

    print(f"La media es: {media}")
    print(f"La nota más alta es: {nota_max}")
    print(f"La nota más baja es: {nota_min}")

    if hay_suspenso:
        num_suspensos = len([n for n in notas if n < 5])
        if num_suspensos == 1:
            print("Hay una nota suspensa.")
        else:
            print(f"Hay {num_suspensos} notas suspensas.")
    else:
        pass

# Ejemplo de uso
notas = [7, 9, 4, 6, 8]
analizar_notas(notas)
