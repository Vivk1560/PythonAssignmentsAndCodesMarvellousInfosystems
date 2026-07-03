def calculation(n1,n2):
    add = n1+n2
    sub = n1-n2
    mult = n1*n2
    div = n1/n2
    return add,sub,mult,div

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    a,s,m,d = calculation(no1,no2)
    print("Addition of given numbers is -",a)
    print("Subtraction of given numbers is-",s)
    print("Multiplication of given numbers is-",m)
    print("Division of given numbers is-",d)
    return

if __name__ == "__main__":
    main()