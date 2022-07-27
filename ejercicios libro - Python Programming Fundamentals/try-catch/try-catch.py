

nombre = input("ingresa tu nombre: ")

edadString =""
edadNumero = 0
try:

    edadString = input("ingresa tu edad: ")
    edadNumero = int(edadString)
except ValueError:
    print("no se ingreso la edad correcta, se te asignara la edad 0 por larry")
    edadString = "0"

print("has sido ingresado en la base de datos")
print("Datos ingresados:")
print("Nombre:"+ nombre)
print("edad %d"% edadNumero)