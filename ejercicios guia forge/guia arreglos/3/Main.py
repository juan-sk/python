



def sumArrayElements(array):
    total  = 0
    for  a in array:
         total +=a;
    
    return total

def main():
    arreglo=[1, 3, 6, 82, 23]
    total =     sumArrayElements(arreglo);
    print ("la suma del contenido del array es: %d"% total)

if __name__ =="__main__":
    main()