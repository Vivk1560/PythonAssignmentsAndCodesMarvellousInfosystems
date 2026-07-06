from functools import reduce
add = lambda n1,n2 : n1+n2

def main():
    l = int(input("Enter the number of elements you want in your list: "))
    value = list()
    for i in range(l):
        ret = int(input(f"Enter the element for {i+1} position: "))
        value.append(ret)
    print("The list entered by the user is:",value)
    result = reduce(add,value)
    print(f"The addition of all the elements of the list {value} is {result}")
    return

if __name__ == "__main__":
    main()