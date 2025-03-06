import random
numero_secreto = random.randint(1, 100)
intento = None
while intento != numero_secreto:
    intento = int(input("Adivina el número entre 1 y 100: "))
    if intento < numero_secreto:
        print("Es más alto.")
    elif intento > numero_secreto:
        print("Es más bajo.")
print("¡Felicidades, adivinaste el número!")
50