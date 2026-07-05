def Add(no1,no2):
    return no1+no2

def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Addition of given 2 numbers {n1} and {n2} is: {Add(n1,n2)}")
    return

if __name__ == "__main__":
    main()