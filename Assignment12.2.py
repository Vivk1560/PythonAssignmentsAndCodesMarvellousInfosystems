def printFactors(n1):
    factors = list()
    for i in range(1,n1+1):
        if(n1%i==0):
            factors.append(i)
    return factors

def main():
    no1 = int(input("Enter the number you want factors of: "))
    print("Factors of the entered number are as follows-")
    for i in printFactors(no1):
        print(i)
    return

if __name__ == "__main__":
    main()