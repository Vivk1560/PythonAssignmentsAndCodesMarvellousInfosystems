isEven = lambda value: value%2==0

def filter(func,val):
    result = list()
    for i in val:
        if(func(i)==True):
            result.append(i)
    return result

squaring = lambda value: value*value

def map(func,val):
    result = list()
    for i in val:
        carry = func(i)
        result.append(carry)
    return result

addition = lambda value1,value2: value1+value2

def reduce(func,val):
    result = 0
    for i in val:
        result += func(result,i)
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
    ret1 = filter(isEven,value)
    ret2 = map(squaring,ret1)
    ret3 = reduce(addition,ret2)
    print(f"List after filter: {ret1}")
    print(f"List after map: {ret2}")
    print(f"Output after reduce: {ret3}")

    return

if __name__ == "__main__":
    main()