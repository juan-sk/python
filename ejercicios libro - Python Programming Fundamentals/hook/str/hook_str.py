class Test:
    def __init__(self) :
        self.a = 1
        self.p =2
        
        
    def __str__(self):
        return "Test(a:"+str(self.a)+",p:"+str(self.p)
    
    
def main():
    test_obj = Test()
    print(test_obj)
    
    
if __name__ == "__main__":
    main()