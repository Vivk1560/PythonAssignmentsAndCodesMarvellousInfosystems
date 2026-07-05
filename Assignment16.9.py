def displayEven():
    countEven = 0
    carry = 1
    while(countEven<10):
        if(carry%2==0):
            countEven += 1
            print(carry, end="  ")
        carry += 1
    return

def main():
    displayEven()
    return

if __name__ == "__main__":
    main()
        
