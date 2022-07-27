


def ingresarElemento(msgString):
    numero =0
    while True:
        try:
            valorInput =  input(msgString)
            numero = int(valorInput)
            # rompler el cliclo
            break
        except Exception:
            print("ocurrio un error al ingresar el valor, por favor intentelo nuevamente")
    return numero

def promedio(values):
    cantidadTotal = len(values)
    suma =0
    
    for item in values:
         suma+=item
    valPromedio = suma/cantidadTotal
    
    return valPromedio


def realizarPreguntas():
    atencion =ingresarElemento("ingrese la calificacion para la Atencion: ")
    calidadComida = ingresarElemento("ingrese la calificacion para la calidad de la Comida: ")
    precio = ingresarElemento("ingrese la calificacion para el precio: ")
    ambiente = ingresarElemento("ingrese la calificacion para el ambiente: ")
    
    return {
       "atencion":atencion,
       "calidadComida":calidadComida,
       "precio":precio,
       "ambiente":ambiente
        }
def main():
    # atención,
    # calidad de la comida,
    # precio,
    # ambiente
    atencion=[]
    calidadComida=[]
    precio=[]
    ambiente=[]
    
    cantidadClietes = 5
    
    
    for item in range(cantidadClietes):
        print("realizando la pregunta al cliente N°:%d"%item)
        resultados = realizarPreguntas()
        
        atencion.append(resultados["atencion"])
        calidadComida.append(resultados["calidadComida"])
        precio.append(resultados["precio"])
        ambiente.append(resultados["ambiente"])
        
    # calculo de promedios
    promedioAtencion = promedio(atencion)
    promedioCalidadComida = promedio(calidadComida)
    promedioPrecio = promedio(precio)
    promedioAmbiente = promedio(ambiente)
    
    print("se imprimen los promedios para las categorias")
    
    print("Atencion:       %.2f"%promedioAtencion)
    print("Calidad Comida: %.2f"%promedioCalidadComida)
    print("Precio:         %.2f"%promedioPrecio)
    print("Ambiente:       %.2f"%promedioAmbiente
          
          
          
    )
if __name__ == "__main__":
    main()