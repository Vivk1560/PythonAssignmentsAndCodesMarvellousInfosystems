from threading import Thread

def evenFactors(num,result):
    sum = 0
    factorList = list()
    for i in range(1,num+1):
        if(num%i==0 and i%2==0):
            factorList.append(i)
            sum += i
    result.append((factorList,sum))

def oddFactors(num,result):
    sum = 0
    factorList = list()
    for i in range(1,num+1):
        if(num%i==0 and (not(i%2==0))):
            factorList.append(i)
            sum += i
    result.append((factorList,sum))

def main():
    no = int(input("Enter the number: "))
    
    evenFactorList = list()
    t1_obj = Thread(target=evenFactors,args=(no,evenFactorList))
    oddFactorList = list()
    t2_obj = Thread(target=oddFactors,args=(no,oddFactorList))

    t1_obj.start()
    t2_obj.start()
    t1_obj.join()
    t2_obj.join()

    eFactors,eSum = evenFactorList[0]
    oFactors,oSum = oddFactorList[0]

    print("Even Factors Are As Follows: ",eFactors)
    print("Sum of even factors is: ",eSum)

    print("Odd Factors Are As Follows: ",oFactors)
    print("Sum of odd factors is: ",oSum)
    print("Exit From Main")
    return

if (__name__=="__main__"):
    main()

