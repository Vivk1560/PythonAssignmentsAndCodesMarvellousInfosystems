checkOdd = lambda n1: not(n1%2==0)

def main():
    no1 = int(input("Enter the number you want to check if odd: "))
    if(checkOdd(no1)==True):
        print(f"The given number {no1} is odd")
    else:
        print(f"The given number {no1} is even")
    return

if __name__ == "__main__":
    main()