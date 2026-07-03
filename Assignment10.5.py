def printAllOdd(n1):
    oddNos = list()
    for i in range(1,n1+1):
        if(not(i%2==0)):
            oddNos.append(i)
    return oddNos

def main():
    no1 = int(input("Enter the number till which you need the list of odd numbers: "))
    print("The list of odd numbers till the number entered is:",printAllOdd(no1))
    return

if __name__ == "__main__":
    main()
