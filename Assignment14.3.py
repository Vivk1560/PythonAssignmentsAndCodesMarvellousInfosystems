max = lambda n1,n2 : n1 if n1>n2 else n2

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    print(f"The max of two numbers entered {no1} and {no2} is {max(no1,no2)}")
    return

if __name__ == "__main__":
    main()