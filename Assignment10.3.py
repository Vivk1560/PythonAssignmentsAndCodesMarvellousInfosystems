def factorial(n1):
    if(n1<0):
        return "Factorial is undefined for negative numbers"
    else:
        fact = 1
        for i in range(n1,1,-1):
            fact = fact*i
        return fact

def main():
    no1 = int(input("Enter the number you want factorial of: "))
    print("The Factorial of entered number is:",factorial(no1))
    return

if __name__=="__main__":
    main()