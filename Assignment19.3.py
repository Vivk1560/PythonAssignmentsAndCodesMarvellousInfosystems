sorting = lambda value: value>=70 and value<=90

def filter(func,val):
    result = list()
    for i in val:
        if(func(i)==True):
            result.append(i)
    return result

increment = lambda value: value+10

def map(func,val):
    result = list()
    for i in val:
        carry = func(i)
        result.append(carry)
    return result

product = lambda value1,value2: value1*value2

def reduce(func,val):
    result = 1
    for i in val:
        result *= func(result,i)
    return result

def main():
    length = int(input("Enter the length of the list you will input: "))
    print("Enter the elements of the list one by one")
    value = list()
    print("Enter the elements of the list you want one by one")
    for i in range(length):
        carry = int(input(f"Enter the value you want at position {i+1}: "))
        value.append(carry)
    print(f"Input List is: {value}")
    ret1 = filter(sorting,value)
    ret2 = map(increment,ret1)
    ret3 = reduce(product,ret2)
    print(f"List after filter: {ret1}")
    print(f"List after map: {ret2}")
    print(f"Output after reduce: {ret3}")

    return

if __name__ == "__main__":
    main()

        