def displayPattern(no):
    for i in range(no):
        print("  *  "*no)
    return

def main():
    v = int(input("Enter the number of which you want length to be of the asterick square: "))
    displayPattern(v)
    return

if __name__ == "__main__":
    main()