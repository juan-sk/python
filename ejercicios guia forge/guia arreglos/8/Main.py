
def ingresarElementoInt(printString):
    numero =0
    while True:
        try:
            valorInput =  input(printString)
            numero = int(valorInput)
            # rompler el cliclo
            break
        except Exception:
            print("ocurrio un error al ingresar el valor, por favor intentelo nuevamente")
    return numero

def main():
    cantidadElementos = ingresarElementoInt("ingrese el largo del array:")
    multiplicador = ingresarElementoInt("ingrese el multiplicador:")

    for item in range(cantidadElementos):
        print("resultado:%d"%((item+1)*multiplicador))
     
if __name__ == "__main__":
    main()