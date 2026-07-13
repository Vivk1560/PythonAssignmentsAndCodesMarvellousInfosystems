from threading import Thread

def evenList(num,result):
    ret = list()
    sum = 0
    for i in num:
        if(i%2==0):
            ret.append(i)
            sum += i
    result.append((ret,sum))

def oddList(num,result):
    ret = list()
    sum = 0
    for i in num:
        if(not(i%2==0)):
            ret.append(i)
            sum += i
    result.append((ret,sum))

def main():
    l = int(input("Enter the number of elements you want in list: "))
    value = list()
    print("Enter the elements of list one by one")
    for i in range(l):
        carry = int(input(f"Enter the element for position {i+1}: "))
        value.append(carry)
    
    eList = list()
    t1_obj = Thread(target=evenList, args=(value,eList))

    oList = list()
    t2_obj = Thread(target=oddList, args=(value,oList))

    t1_obj.start()
    t2_obj.start()
    t1_obj.join()
    t2_obj.join()

    evLi, evSum = eList[0]
    odLi, odSum = oList[0]

    print(f"The even numbers of inputted list are: {evLi} and their sum is {evSum}")
    print(f"The odd numbers of inputted list are: {odLi} and their sum is {odSum}")

    return

if (__name__=="__main__"):
    main()



