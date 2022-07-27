
class Reloj:
    
    def __init__(self,hora=0,minuto=0,segundo=0) :
        self.hora = hora
        self.minuto= minuto
        self.segundo = segundo
    
    def avanzarSegundo(self):
        self.segundo+=1
    
    def __str__(self) :
        return "Reloj(hora:"+str(self.hora)+", minuto: "+str(self.minuto)+" segundo: "+str(self.segundo)+")"
    def print(self):
        hora =Reloj.agregarCero(self.hora)            
        minuto = Reloj.agregarCero(self.minuto)
        segundo = Reloj.agregarCero(self.segundo)
             
        return hora+":" +minuto+":"+segundo
    
    def agregarCero(self, value):

        if value <10:
            return "0"+ str(value)
        else:
            return value
