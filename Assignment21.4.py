from threading import Thread

def sumOf(value,result):
    sum = 0
    for i in value:
        sum+=i
    result.append(sum)
    return

def prodOf(value,result):
    product = 1
    for i in value:
        product*=i
    result.append(product)
    return

def main():
    l = int(input("Enter the length of the list you will enter: "))
    print("Enter the elements one by one: ")
    uInput = list()
    for i in range(l):
        carry = int(input(f"Enter the element for position {i+1}: "))
        uInput.append(carry)
    sList = list()
    t1 = Thread(target=sumOf,args=(uInput,sList,))
    pList = list()
    t2 = Thread(target=prodOf,args=(uInput,pList,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    so = sList[0]
    pro = pList[0]

    print("Sum of all the elements from list is: ",so)
    print("Product of all the elements of the list is: ",pro)
    return

if __name__ == "__main__":
    main()