from functools import reduce

min = lambda n1,n2 : n1 if n1<n2 else n2

def main():
    arr = list()
    l = int(input("Enter the number of objects you want in your list - "))
    carry = 0
    print("Now enter the elements for list one by one-")
    for i in range(l):
        carry = int(input(f"Enter element for {i+1} position: "))
        arr.append(carry)
    res = reduce(min,arr)
    print("The result after the reduce function is:",res)
    return

if __name__ == "__main__":
    main()