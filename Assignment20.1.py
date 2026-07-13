from threading import Thread

def firstEvenNos():
    evenCount = 0
    carry = 1
    print("Printing first 10 Even Numbers")
    while(evenCount<10):
        if (carry%2 == 0):
            print(carry)
            evenCount += 1
        carry += 1
    print("")
    return

def firstOddNos():
    oddCount = 0
    carry = 1
    print("Printing first 10 Odd Numbers")
    while(oddCount<10):
        if (not(carry%2 == 0)):
            print(carry)
            oddCount += 1
        carry += 1
    print("")
    return

def main():
    thrd_obj1 = Thread(target=firstEvenNos)
    thrd_obj2 = Thread(target=firstOddNos)
    thrd_obj1.start()
    thrd_obj1.join()
    thrd_obj2.start()
    thrd_obj2.join()
    return

if __name__ == "__main__":
    main()



