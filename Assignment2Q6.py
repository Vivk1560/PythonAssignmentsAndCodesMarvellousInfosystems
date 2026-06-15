def calculation():
    print("Enter The 2 Numbers For Calculation:")
    print("Please Enter First Number-")
    no1 = int(input())
    print("Please Enter Second Number-")
    no2 = int(input())
    add = no1+no2
    if(no2>no1):
        sub = no2-no1
    else:
        sub = no1-no2
    mult = no1*no2
    div = no1/no2
    print("The Addition of given two numbers is:",add)
    print("The Subtraction of given two numbers is(considering greatest one as first number):",sub)
    print("The Multiplication of given two numbers is:",mult)
    print("The Division of given two numbers is:",div)

def main():
    calculation()

if(__name__=="__main__"):
    main()