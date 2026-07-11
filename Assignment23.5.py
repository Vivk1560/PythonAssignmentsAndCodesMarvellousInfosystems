from os import getpid
from multiprocessing import Pool

def calcFactorial(value):
    factorial = 1
    for i in range(value,1,-1):
        factorial *= i
    id = getpid()
    return (id,value,factorial)

def main():
    pool_object = Pool()
    valueX = [10,15,20,25]
    result = pool_object.map(calcFactorial,valueX)
    for pid,value,ans in result :
        print("Process ID:",pid)
        print("Input Number:",value)
        print("Factorial:",ans)
        print("")
    return
    
if __name__ == "__main__":
    main()
