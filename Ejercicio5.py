import random

def generar_adn(n):
    letras = ['A', 'T', 'C', 'G']
    
    adn = ""
    for _ in range(n):
        adn += random.choice(letras)
    
    conteo = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for letra in adn:
        conteo[letra] += 1
    
    print("ADN generado:", adn)
    print("Conteo de letras:", conteo)
    
    return adn, conteo

generar_adn(20)
