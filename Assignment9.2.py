def ChkGreater(number1,number2):
    if(number1>number2):
        return f"{number1} is greater"
    elif(number1==number2):
        return f"Both {number1} and {number2} are equal"
    else:
        return f"{number2} is greater"

def main():
    no1 = int(input("Enter The First Number: "))
    no2 = int(input("Enter The Second Number: "))
    print(ChkGreater(no1,no2))
    return

if __name__ == "__main__":
    main()
