from multiprocessing import Pool
from os import getpid
from time import perf_counter

def sumOfSquares(value):
    print("Process is running with PID:",getpid())
    sum = 0
    for i in range(1,value+1):
        sum += i*i
    return sum

def main():
    start_time = perf_counter()
    pool_object = Pool()
    ans = [1000000,2000000,3000000,4000000]
    print(f"Input is: {ans}")
    valueX = pool_object.map(sumOfSquares,ans)
    print(f"Output is: {valueX}")
    end_time = perf_counter()
    print(f"Time required to do the required operations is {end_time-start_time} seconds")

if __name__ == "__main__":
    main()

