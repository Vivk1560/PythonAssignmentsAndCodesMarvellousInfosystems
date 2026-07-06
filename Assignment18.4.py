def countFrequency(series,no):
    count = 0
    for i in series:
        if(i==no):
            count+=1
    return count
def main():
    l = int(input("Enter the number of elements you want in your list: "))
    value = list()
    for i in range(l):
        ret = int(input(f"Enter the element for {i+1} position: "))
        value.append(ret)
    print("The list entered by the user is:",value)
    no = int(input("Enter the number you want frequency of: "))
    print(f"The list entered {value} has the frequency of the provided numer {no} as {countFrequency(value,no)}")
    return

if __name__ == "__main__":
    main()