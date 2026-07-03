def checkPalindrome(n1):
    reverse = 0
    copy = n1
    while(n1>0):
        carry = n1%10
        n1 //= 10
        reverse = (reverse*10) + carry
    return reverse==copy

def main():
    no1 = int(input("Enter the number you want to check wheather palindrome: "))
    if(checkPalindrome(no1)==True):
        print("The number you entered is Palindrome")
    else:
        print("The number you entered is not a Palindrome")
    return

if __name__ == "__main__":
    main()