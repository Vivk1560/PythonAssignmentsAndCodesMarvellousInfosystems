from multiprocessing import Pool
from os import getpid
from time import perf_counter

def calcFactorial(value):
    print("Process is running with PID:",getpid())
    sum = 1
    for i in range(value,1,-1):
        sum *= i
    return sum

def main():
    start_time = perf_counter()
    pool_object = Pool()
    ans = [10,15,20,25]
    print(f"Input is: {ans}")
    valueX = pool_object.map(calcFactorial,ans)
    print(f"Output is: {valueX}")
    end_time = perf_counter()
    print(f"Time required to do the required operations is {end_time-start_time} seconds")

if __name__ == "__main__":
    main()

