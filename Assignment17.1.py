import Arithmetic

def main():
    v1 = int(input("Enter the first number for calculations: "))
    v2 = int(input("Enter the second number for calculations: "))
    print(f"The Result of addition of the 2 numbers {v1} and {v2} is {Arithmetic.Add(v1,v2)}")
    print(f"The Result of subtraction of the 2 numbers {v1} and {v2} is {Arithmetic.Sub(v1,v2)}")
    print(f"The Result of multiplication of the 2 numbers {v1} and {v2} is {Arithmetic.Mult(v1,v2)}")
    print(f"The Result of division of the 2 numbers {v1} and {v2} is {Arithmetic.Div(v1,v2)}")
    return

if __name__ == "__main__":
    main()
