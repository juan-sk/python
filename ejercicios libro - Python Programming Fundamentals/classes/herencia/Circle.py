from Figura import Figura

class Circle(Figura):
    
    def __init__(self,x,y,radio):
        super().__init__(x,y)
        self.radio = radio
    def print(self):
        print("---circulo----")
        print("x:     "+str(self.x))
        print("y:     "+str(self.y))
        print("radio: "+str(self.radio))