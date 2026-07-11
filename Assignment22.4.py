from multiprocessing import Pool
from os import getpid
from time import perf_counter

def calcPowerOf5(value):
    print("Process is running with PID:",getpid())
    sum = 0
    for i in range(1,value+1):
        sum += i**5
    return sum

def main():
    start_time = perf_counter()
    pool_object = Pool()
    valueX = [10000000,20000000,30000000,40000000]
    print(f"Input is: {valueX}")
    ans = pool_object.map(calcPowerOf5,valueX)
    print(f"Output is: {ans}")
    end_time = perf_counter()
    print(f"Time required to do the required operations is {end_time-start_time} seconds")

if __name__ == "__main__":
    main()

