
from Cafetera import Cafetera


def main():
    cafeteriacion = Cafetera(1000,500)
    
    print("capacidad Actual: %d"% cafeteriacion.capacidadActual)
    cafeteriacion.servirTaza(200)
    print("capacidad Actual: %d"% cafeteriacion.capacidadActual)
    cafeteriacion.llenarCafetera()
    print("capacidad Actual: %d"% cafeteriacion.capacidadActual)
    cafeteriacion.servirTaza(200)
    print("capacidad Actual: %d"% cafeteriacion.capacidadActual)
    cafeteriacion.servirTaza(200)
    cafeteriacion.servirTaza(200)
    cafeteriacion.servirTaza(200)
    print("capacidad Actual: %d"% cafeteriacion.capacidadActual)
    

if __name__ == "__main__":
    main()