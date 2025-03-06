# Un cajero automático
Usuario = list()

Usuario.append("Selvin")
Usuario.append("1234")
Usuario.append(1000)

recibo = list()
recibo.append(["123", 600])
recibo.append(["124", 845])
recibo.append(["125", 67])
recibo.append(["126", 500])
recibo.append(["127", 100])
recibo.append(["128", 1000])

acciones = list()
acciones.append("Depositar")
acciones.append("pago de recibo")
acciones.append("Retirar")

# Definir Usuario2 correctamente
Usuario2 = list()
Usuario2.append("Selvin")
Usuario2.append("12345")
Usuario2.append(1500)

def registrar():
    UsuarioRegistrado = list()
    usuarioc = input("Ingrese su nombre: ")
    password = input("Ingrese su password: ")
    
    UsuarioRegistrado.append(usuarioc)
    UsuarioRegistrado.append(password)

    if usuarioc == Usuario[0] and password == Usuario[1]:
        print("Bienvenido al cajero automático")
    else:
        print("Usuario o contraseña incorrecta")
        return registrar()

# Llamar a la función registrar para probar
registrar()