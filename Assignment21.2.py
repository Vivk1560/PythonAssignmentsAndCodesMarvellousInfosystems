from threading import Thread

def minElement(value,result):
    min = 1000000000000
    for i in value:
        if(i<min):
            min = i
    result.append(min)
    return min

def maxElement(value,result):
    max = 0
    for i in value:
        if(i>max):
            max = i
    result.append(max)
    return max

def main():
    l = int(input("Enter the length of the list you will enter: "))
    print("Enter the elements one by one: ")
    uInput = list()
    for i in range(l):
        carry = int(input(f"Enter the element for position {i+1}: "))
        uInput.append(carry)
    miList = list()
    t1 = Thread(target=minElement,args=(uInput,miList,))
    mxList = list()
    t2 = Thread(target=maxElement,args=(uInput,mxList))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    minEl = miList[0]
    maxEl = mxList[0]

    print("Min Element from list is: ",minEl)
    print("Max Element from list is: ",maxEl)
    return

if __name__ == "__main__":
    main()
