def checkDivisible(no):
    return no%5==0

def main():
    n1 = int(input("Enter number: "))
    print(f"The number you entered {n1} is divisible by 5: {checkDivisible(n1)}")
    return

if __name__ == "__main__":
    main()