from Circle import  Circle
def main():

    print("hello class")
    circulo = Circle(2,3,39)
    print("pocicion")
    posicion = circulo.obtenerPosicion()
    print(posicion)
    print(posicion["x"])
    print (circulo)
    
    
    
if __name__ == "__main__":
    main();
    