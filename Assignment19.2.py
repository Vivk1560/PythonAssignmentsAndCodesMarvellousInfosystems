multi = lambda n1,n2 : n1*n2

def main():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    print(f"Multiplication of the given two numbers {val1} and {val2} is {multi(val1,val2)}")
    return

if __name__ == "__main__":
    main()