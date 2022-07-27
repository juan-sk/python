

from Cuenta import Cuenta


def main():
    
    cuenta1= Cuenta("20046877-5",15000000)
    print(cuenta1.obtenerBalance())
    cuenta1.girarMonto(5000000)
    
    print(cuenta1.obtenerBalance())
    cuenta1.despositar(200000)
    print(cuenta1.obtenerBalance())
    

if __name__ == "__main__":
    main()