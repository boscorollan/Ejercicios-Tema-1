def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        
        if num < 0:
            negativos.append(num)
    
    return pares, impares, negativos

numeros = [10, -3, 7, -8, 0, 5, -1]
pares, impares, negativos = clasificar_numeros(numeros)

print("Los numeros pares son:", pares)
print("Los numeros impares son:", impares)
print("Los numeros negativos son:", negativos)
