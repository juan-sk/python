

def findIndexes(arr,value):
    for item in range(len(arr)):
         if(arr[item] == value):
            print(item);

def main():
    arr = [1, 2, 3, 100, 23, 2, 2, 1]
    value = 2
    findIndexes(arr,value)

if __name__ == "__main__":
    main()