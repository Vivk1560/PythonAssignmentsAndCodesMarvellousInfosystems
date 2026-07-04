checkDiv5 = lambda n1: n1%5==0

def main():
    no1 = int(input("Enter the number you want to check if divisble by 5: "))
    if(checkDiv5(no1)==True):
        print(f"The given number {no1} is divisible by 5")
    else:
        print(f"The given number {no1} is not divisible by 5")
    return

if __name__ == "__main__":
    main()