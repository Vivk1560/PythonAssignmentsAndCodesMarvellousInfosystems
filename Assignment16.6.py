def checkNumber(no):
    if(no>0):
        print(f"Given Number {no} is positive number")
    elif(no==0):
        print(f"Given Number {no} is zero")
    else:
        print(f"Given Number {no} is negative number")
    return

def main():
    number = int(input("Enter any number: "))
    checkNumber(number)
    return

if __name__ == "__main__":
    main()