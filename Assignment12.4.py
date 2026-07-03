def generateIndividualNos(n1):
    numbers = list()
    for i in range(1,n1+1):
        numbers.append(i)
    return numbers

def main():
    n = int(input("Enter any number: "))
    print("Numbers from 1 to entered number are as follows:- ")
    for i in generateIndividualNos(n):
        print(i)
    return

if __name__ == "__main__":
    main()

