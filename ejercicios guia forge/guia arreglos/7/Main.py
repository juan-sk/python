

def ingresarElementoFloat(printString):
    numero =0.0
    while True:
        try:
            valorInput =  input(printString)
            numero = float(valorInput)
            # rompler el cliclo
            break
        except Exception:
            print("ocurrio un error al ingresar el valor, por favor intentelo nuevamente")
    return numero

def ingresarElementoInt(printString):
    numero =0.0
    while True:
        try:
            valorInput =  input(printString)
            numero = int(valorInput)
            # rompler el cliclo
            break
        except Exception:
            print("ocurrio un error al ingresar el valor, por favor intentelo nuevamente")
    return numero

def ingresarNotas(cantidadAlumnos):
    array=[]
    for item in range(cantidadAlumnos):
        printString = "ingrese el elemento N°"+ str(item)+" :"
        numero = ingresarElementoFloat(printString)
        array.append(numero)
    return array

def calcularPromedio(notas):
    
    cantidadElementos = len(notas)
    suma = 0 
    for item in notas:
        suma+=item
        
    return suma/cantidadElementos



def main():
    
    print("este programa calcula el promedio de un curso")
    # ingresar cantidad de alunmos 
    
    cantidadAlumnos = ingresarElementoInt("ingrese la cantidad de alumnos: ")
    # ingresar notas
    notas = ingresarNotas(cantidadAlumnos)
    # calcular promedio
    promedio = calcularPromedio(notas)
    print("el promedio es: %.2f"%promedio)
    # imprimir notas sobre el promedio
    
    for item in notas:
        if item>= promedio:
            print("nota:%.2f"%item)
    

if __name__ == "__main__":
    main()