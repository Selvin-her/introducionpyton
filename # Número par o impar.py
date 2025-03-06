# Número par o impar
def par_o_impar():
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print(f"{num} es un número par.")
    else:
        print(f"{num} es un número impar.")

par_o_impar()
