def checkPrime(no1):
    isPrime = True
    for i in range(2,no1):
        if(no1%i==0):
            isPrime = False
    return isPrime

def main():
    n1 = int(input("Enter the number you wanna check if prime: "))
    ans = checkPrime(n1)
    if(ans==False):
        print("Number is not prime")
    else:
        print("Number is Prime")

if __name__ == "__main__":
    main()
        
