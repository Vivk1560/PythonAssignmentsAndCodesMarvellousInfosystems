from os import getpid
from multiprocessing import Pool

def countOfEven(value):
    sum = 0
    for i in range(1,value+1):
        if(i%2==0):
            sum += 1
    id = getpid()
    return (id,value,sum)

def main():
    pool_object = Pool()
    valueX = [1000000,2000000,3000000,4000000]
    result = pool_object.map(countOfEven,valueX)
    for pid,value,ans in result :
        print("Process ID:",pid)
        print("Input Number:",value)
        print("Count Of Even Numbers:",ans)
        print("")
    return
    
if __name__ == "__main__":
    main()
