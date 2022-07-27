class Circle:
    
    def __init__(self, x=1,y=1,radious=50):
        self.x = x
        self.y=y
        self.radious=radious

        
        
        
    def obtenerPosicion(self):
        return {"x":self.x,"y":self.y}