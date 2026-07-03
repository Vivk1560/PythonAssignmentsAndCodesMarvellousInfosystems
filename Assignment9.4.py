def returnCube(n1):
    return (n1*n1*n1)

def main():
    no1 = int(input("Enter the number you want square of- "))
    print("Cube of entered number is:",returnCube(no1))
    return

if __name__ == "__main__":
    main()