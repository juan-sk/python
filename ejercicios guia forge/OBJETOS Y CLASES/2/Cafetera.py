from re import S


class Cafetera:
    
    def __init__(self,capacidadMaxima,capacidadActual) :
        self.capacidadMaxima=capacidadMaxima
        self.capacidadActual = capacidadActual
        
        
    def llenarCafetera(self):
        self.capacidadActual = self.capacidadMaxima
        
    def servirTaza(self,tamanoTaza):
        if self.capacidadActual-tamanoTaza<0:
            return 0
        else:
            self.capacidadActual -=tamanoTaza
            return tamanoTaza
    def vaciarCafetera(self):
        self.capacidadActual = 0 
    def agregarCafe(self,cantidadAAgregar):
        if self.capacidadActual+ cantidadAAgregar > self.capacidadMaxima:
            return 0
        else:
            self.capacidadActual+cantidadAAgregar
            return self.capacidadActual
        
        