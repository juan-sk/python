

from json.encoder import INFINITY


def obtenerNumeroMenor(arreglo):
    numeroMenor = INFINITY
    for element in arreglo:
        if element<numeroMenor:
            numeroMenor= element
    return numeroMenor
    


def main():
    print("muestra el umero menor en un arreglo ")
    
    arreglo =  [90, 1, 38, -10, 29, 4]
    numeroMenor = obtenerNumeroMenor(arreglo)
    
    print("el numero menor del arreglo es: %d"%numeroMenor)

if __name__ == "__main__":
    main()