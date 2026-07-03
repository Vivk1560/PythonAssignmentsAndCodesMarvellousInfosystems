def convBinary(n):
    binary = 0
    place = 1
    carry = 0
    while(n>0):
        carry = n%2
        binary = binary + (carry*place)
        place *= 10
        n //= 2
    return binary

def main():
    no1 = int(input("Enter the number you want binary equivalent of: "))
    print(f"Binary equivalent of {no1} is {convBinary(no1)}")
    return

if __name__ == "__main__":
    main()