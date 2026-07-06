def sumOfDigits(no): #Logic1: Accepts data as integer returns sum in integer 
    sum = 0
    while(no>0):
        sum += no%10
        no //= 10
    return sum

def sumOfDigitsX(no): #Logic2: Accepts data in string and then typecasts and returns sum in integer
    sum = 0
    l = len(no)
    for i in range(l):
        sum += int(no[i])
    return sum

def main():
    #Logic1
    value = int(input("Enter the number you want the sum of digits: "))
    print(f"The number entered {value} has it's sum of digits as {sumOfDigits(value)}")

    #Logic2
    valueX = input("Enter the number you want the sum of digits: ")
    print(f"The number entered {valueX} has it's sum of digits as {sumOfDigitsX(valueX)}")
    return

if __name__ == "__main__":
    main()
