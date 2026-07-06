def displayPattern(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(j,end="  ")
        print()
    return

def main():
    v = int(input("Enter the number: "))
    displayPattern(v)
    return

if __name__ == "__main__":
    main()