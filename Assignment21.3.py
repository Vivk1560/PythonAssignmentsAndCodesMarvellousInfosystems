from threading import Thread,Lock
counter = 0
lock = Lock()

def increment(noX):
    global counter

    with lock:
        counter += noX
    return

def main():
    global counter
    t1 = Thread(target=increment, args = (5,))
    t2 = Thread(target=increment, args = (10,))
    t3 = Thread(target=increment, args = (100,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(counter)
    
if __name__ == "__main__":
    main()
    
