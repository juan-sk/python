from Rectangle import Rectangle
from Circle import Circle

def main():
    print("hello herencia")
    
    rectangulo = Rectangle(1,2,4,5)
    circulo=Circle(2,3,40)
    rectangulo.print();
    circulo.print()
    
    
    
if __name__ == "__main__":
    main();