def checkPerfect(n):
    divSum = 0
    for i in range(1,n):
        if(n%i==0):
            divSum += i
    return divSum == n

def main():
    no1 = int(input("Enter the number you wish to check if perfect: "))
    if(checkPerfect(no1)):
        print(f"Entered Number {no1} is Perfect")
    else:
        print(f"Entered Number {no1} is not Perfect")
    return

if __name__ == "__main__":
    main()

    