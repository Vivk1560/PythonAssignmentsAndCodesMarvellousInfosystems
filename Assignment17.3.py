def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact *= i
    return fact

def main():
    v = int(input("Enter the number you want factorial of: "))
    print(f"The factorial of the number {v} is: {factorial(v)}")
    return

if __name__ == "__main__":
    main()
