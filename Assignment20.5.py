from threading import Thread

def display():
    for i in range(1,51):
        print(i)
    print("")

def displayX():
    for i in range(50,0,-1):
        print(i)
    print("")

def main():
    t1_obj = Thread(target=display,name="Thread1")
    t2_obj = Thread(target=displayX,name="Thread2")
    t1_obj.start()
    t1_obj.join()
    print("Thread1 Complete")
    print("")
    t2_obj.start()
    t2_obj.join()
    print("Thread2 Complete")

if (__name__=="__main__"):
    main()