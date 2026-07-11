from multiprocessing import Pool
from os import getpid
from time import perf_counter

def isPrime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
    return True

def calcSumOfPrime(value):
    print("Process is running with PID:",getpid())
    sum = 0
    for j in range(2,value+1):
        if(isPrime(j)):
            sum+=1
    return sum

def main():
    start_time = perf_counter()
    pool_object = Pool()
    ans = [10000,20000,30000,40000]
    print(f"Input is: {ans}")
    valueX = pool_object.map(calcSumOfPrime,ans)
    print(f"Output is: {valueX}")
    end_time = perf_counter()
    print(f"Time required to do the required operations is {end_time-start_time} seconds")

if __name__ == "__main__":
    main()

