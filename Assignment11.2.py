def countDigits(n1):
    count = 0
    while(n1>0):
        n1 //= 10 
        count += 1
    return count

def main():
    no1 = int(input("Enter the number you want to count digits of: "))
    print("The count of digits of the number entered is:",countDigits(no1))
    return

if __name__ == "__main__":
    main()
