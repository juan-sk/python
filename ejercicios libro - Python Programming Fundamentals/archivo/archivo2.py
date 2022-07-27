

from fileinput import filename


fileName = "arch_ej_2.txt"
def printFileContent(file):
    for line in file.readlines():
        print (line,end="")        
    
archivo = open(fileName,"r")


printFileContent(archivo)
