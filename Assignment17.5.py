def chkPrime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
    return True

def main():
    v = int(input("Enter the number you want to check if Prime: "))
    if(chkPrime(v)==True):
        print(f"The Number entered {v} is Prime")
    else:
        print(f"The Number entered {v} is not Prime")
    return

if __name__ == "__main__":
    main()