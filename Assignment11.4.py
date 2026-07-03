def reverseNumber(n1):
    reverse = 0
    while(n1>0):
        carry = n1%10
        n1 //= 10
        reverse = (reverse*10) + carry
    return reverse

def main():
    no1 = int(input("Enter the number you want to reverse: "))
    print("The reverse of the number entered is:",reverseNumber(no1))
    return

if __name__ == "__main__":
    main()



