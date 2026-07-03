def printAllEven(n1):
    evenNos = list()
    for i in range(1,n1+1):
        if(i%2==0):
            evenNos.append(i)
    return evenNos

def main():
    no1 = int(input("Enter the number till which you need the list of even numbers: "))
    print("The list of even numbers till the number entered is:",printAllEven(no1))
    return

if __name__ == "__main__":
    main()

