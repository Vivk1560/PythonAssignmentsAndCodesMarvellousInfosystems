checkLen = lambda n1: len(n1)>=5

def main():
    arr = list()
    l = int(input("Enter the number of objects you want in your list - "))
    carry = 0
    print("Now enter the elements in string form for list one by one-")
    for i in range(l):
        carry = input(f"Enter element for {i+1} position: ")
        arr.append(carry)
    liLen = filter(checkLen,arr)
    print("The result after the filter function is:",list(liLen))
    return

if __name__ == "__main__":
    main()