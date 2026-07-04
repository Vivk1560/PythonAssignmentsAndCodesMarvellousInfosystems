checkEven = lambda n1: n1%2==0

def main():
    no1 = int(input("Enter the number you want to check even for: "))
    if(checkEven(no1)==True):
        print(f"The given number {no1} is even")
    else:
        print(f"The given number {no1} is odd")
    return

if __name__ == "__main__":
    main()