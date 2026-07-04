checkEven = lambda n1: not(n1%2==0)

def main():
    arr = list()
    l = int(input("Enter the number of objects you want in your list - "))
    carry = 0
    print("Now enter the elements for list one by one-")
    for i in range(l):
        carry = int(input(f"Enter element for {i+1} position: "))
        arr.append(carry)
    liOdd = filter(checkEven,arr)
    print("The result after the filter function is:",list(liOdd))
    return

if __name__ == "__main__":
    main()