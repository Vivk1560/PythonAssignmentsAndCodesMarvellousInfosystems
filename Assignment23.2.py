from os import getpid
from multiprocessing import Pool

def sumOfOdd(value):
    sum = 0
    for i in range(2,value+1):
        if(not(i%2==0)):
            sum += i
    id = getpid()
    return (id,value,sum)

def main():
    pool_object = Pool()
    valueX = [1000000,2000000,3000000,4000000]
    result = pool_object.map(sumOfOdd,valueX)
    for pid,value,ans in result :
        print("Process ID:",pid)
        print("Input Number:",value)
        print("Sum Of Odd Numbers:",ans)
        print("")
    return
    
if __name__ == "__main__":
    main()
