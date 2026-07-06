import MarvellousNum

def ListPrime(value):
    result = 0
    for i in value:
        if(MarvellousNum.chkPrime(i)==True):
            result += i
    return result

def main():
    l = int(input("Enter the number of elements you want in your list: "))
    val = list()
    for i in range(l):
        ret = int(input(f"Enter the element for {i+1} position: "))
        val.append(ret)
    print("The list entered by the user is:",val)
    print(f"The list entered {val} has the addition of all it's prime numbers as: {ListPrime(val)}")
    return

if __name__ == "__main__":
    main()
