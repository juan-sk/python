from re import S
from Figura import Figura
class Rectangle(Figura):
    
    def __init__(self,x,y,largo,ancho):
        super().__init__(x,y)
        self.largo=largo
        self.ancho=ancho
        
    def print(self):
        print("---Rectangulo---")
        print("x:     "+str(self.x))
        print("y:     "+str(self.y))
        print("largo: "+str(self.largo))
        print("ancho: "+str(self.ancho))
        
        