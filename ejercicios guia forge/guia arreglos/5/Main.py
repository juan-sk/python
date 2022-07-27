
def obtenerSumas(a,b):
    
    sumas = []
    for i in range(len(a)):
        sumas.append(a[i]+b[i])
    return sumas

def obtieneProducto(a,b):
    productos = []
    for i in range(len(a)):
        productos.append(a[i]*b[i])
    return productos
         
def printResultados(a,b,sumas,productos):
    for i in range(len(a)):
        print ("para: %d y %d la suma es %d y el producto es %d" % (a[i],b[i],sumas[i],productos[i]))
         

def main():
    print("calcula la suma y el producto entre dos arreglos")
    
    arregloA = [0, 28, 30, 10, 4]
    arregloB = [1, 3, 6, 82, 23]
    
    sumas = obtenerSumas(arregloA,arregloB)
    producto = obtieneProducto(arregloA,arregloB)
    

    
    printResultados(arregloA,arregloB,sumas, producto)
    
    

    

if __name__ == "__main__":
    main()