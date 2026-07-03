def generateIndRevNos(n1):
    reverseNumbers = list()
    for i in range(n1,0,-1):
        reverseNumbers.append(i)
    return reverseNumbers

def main():
    n = int(input("Enter any number: "))
    print("Numbers from entered number to 1 are as follows:- ")
    for i in generateIndRevNos(n):
        print(i)
    return

if __name__ == "__main__":
    main()