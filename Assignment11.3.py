def sumOfDigits(n1):
    count = 0
    while(n1>0):
        count += n1%10
        n1 //= 10   
    return count

def main():
    no1 = int(input("Enter the number you want to count digits of: "))
    print("The count of digits of the number entered is:",sumOfDigits(no1))
    return

if __name__ == "__main__":
    main()

