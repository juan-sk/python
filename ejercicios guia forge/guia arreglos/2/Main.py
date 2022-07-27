
def printArregloInvertido(arreglo):


    for item in range(len(arreglo)-1,-1,-1):
        print(arreglo[item])
def main():
    arreglo = [0, 28, 30, 10, 4]
    printArregloInvertido(arreglo)
    
    

if __name__ == "__main__":
    main()