mult = lambda n1,n2 : n1*n2

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    print(f"The multiplication of two numbers entered {no1} and {no2} is {mult(no1,no2)}")
    return

if __name__ == "__main__":
    main()