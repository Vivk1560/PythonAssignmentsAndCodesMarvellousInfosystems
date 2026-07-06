def lenNo(no): #Logic1
    carry = 0
    while(no>0):
        no //= 10
        carry += 1
    return carry

def lenNoX(no): #Logic2
    return len(no)

def main():
    #Logic1
    value = int(input("Enter the number you want count digits of: "))
    print(f"The number entered {value} has {lenNo(value)} digits")

    #Logic2
    valueX = input("Enter the number you want count digits of: ")
    print(f"The number entered {valueX} has {lenNoX(valueX)} digits")
    return

if __name__ == "__main__":
    main()