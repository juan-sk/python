

def interceptarArreglos(arrA, arrB):
    
    nuevoArr= set()
    for a in arrA:
        nuevoArr.add(a)
    
    
    for b in arrB:
        nuevoArr.add(b)
    
    return list(nuevoArr)
              
def main():
    arrA = [1, 3, 6, 9, 17]
    arrB = [2, 4, 10, 17]
    
    nueoArr = interceptarArreglos(arrA,arrB)
    print(nueoArr) # 
    

if __name__ == "__main__":
    main()