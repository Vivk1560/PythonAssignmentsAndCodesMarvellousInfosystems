def displayPattern(no):
    for i in range(no,0,-1):
        print("  *  "*i)
    return

def main():
    v = int(input("Enter the number of which you want length of asterick triangle to be: "))
    displayPattern(v)
    return

if __name__ == "__main__":
    main()