def displayAst(no):
    for i in range(no):
        print("*",end="  ")
    return

def main():
    v = int(input("Enter the number of * you want: "))
    displayAst(v)
    return

if __name__ == "__main__":
    main()
