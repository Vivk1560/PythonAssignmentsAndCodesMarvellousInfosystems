def checkDivisibility3and5(n1):
    return (n1%3==0 and n1%5==0)

def main():
    no1 = int(input("Enter the number for which divisibility by 3 and 5 is to be checked: "))
    if(checkDivisibility3and5(no1)):
        print("Divisble By 3 and 5")
    else:
        print("Not divisible by 3 as well as 5")
    return

if __name__ == "__main__":
    main()