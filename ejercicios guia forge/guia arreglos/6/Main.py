
def ingresarElemento(index):
    numero =0
    while True:
        try:
            valorInput =  input("ingresa el elemento %d del array "% index)
            numero = int(valorInput)
            # rompler el cliclo
            break
        except Exception:
            print("ocurrio un error al ingresar el valor, por favor intentelo nuevamente")
    return numero

def invertArray(array):
    largoArray = len(array)
    print(largoArray)
    arrayInvertido = []
    for item in range(largoArray):
        index= (largoArray-1)-item
        element = array[index]    
        arrayInvertido.append(element)
    return arrayInvertido

def printArray(array):
    largoArry = len(array)
    for item in range(largoArry):
         print("Index: %d, element: %d"%(item,array[item]))

def main():
    
    print("en este programa se ingresan 6 valores en un array y se ordenan inversamente en un arreglo ")
    cantidadElementosAAgregar = 6;
    arrayA = []
    for item in range(cantidadElementosAAgregar):
        
        numero =ingresarElemento(item)
        arrayA.append(numero)
        
    arrayB = invertArray(arrayA)
    print("array ")
    # printArray(arrayB)
    print(arrayB)
    

if __name__ == "__main__":
    main()