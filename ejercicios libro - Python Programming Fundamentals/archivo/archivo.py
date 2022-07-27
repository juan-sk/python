
archivo = open("ejemplo.txt","r")


print(archivo.name)
print("contenido del archivo %s" % archivo.name)
print("\n")
def printFileContent(file):
    for line in file.readlines():
        print (line,end="")        
    
printFileContent(archivo)