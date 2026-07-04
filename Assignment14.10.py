maximum = lambda n1,n2,n3 : n1 if (n1>n2 and n1>n3) else n2 if(n2>n1 and n2>n3) else n3

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    no3 = int(input("Enter the third number: "))
    print(f"The max of three numbers entered {no1},{no2} and {no3} is {maximum(no1,no2,no3)}")
    return

if __name__ == "__main__":
    main()

