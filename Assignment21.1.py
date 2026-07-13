from threading import Thread


def isPrime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
    return True

def displayPrime(value):
    print("Display of prime numbers from list is as follows: ")
    for i in value:
        if(isPrime(i)):
            print(i)
    

def displayNonPrime(value):
    print("Display of non prime numbers from list is as follows: ")
    for i in value:
        if(not(isPrime(i))):
            print(i)

def main():
    l = int(input("Enter the length of the list of integers you will input: "))
    val = list()
    for i in range(l):
        carry = int(input(f"Enter the element for position {i+1}: "))
        val.append(carry)
    tObj1 = Thread(target=displayPrime,args=(val,),name = "Prime")
    tObj2 = Thread(target=displayNonPrime,args=(val,), name = "NonPrime")
    tObj1.start()
    tObj1.join()
    tObj2.start()
    tObj2.join()

if __name__ == "__main__":
    main()
