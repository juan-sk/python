class Cuenta:
    
    
    def __init__(self,cliente, balance):
        self.cliente =cliente
        self.balance = balance
        
    def despositar (self,montoADepositar):
        self.balance +=montoADepositar
     
    def obtenerBalance(self):
        return self.balance
    
    def girarMonto(self,monto):
        if self.balance>= monto:
            self.balance-=monto
            return monto
        else:
            print("usted no puede girar esta cantidad")
    