from threading import Thread, get_ident, current_thread

def Small(value,result):
    print("Thread ID: ",get_ident())
    print("Thread Name:", current_thread())
    sum = 0
    ret = list()
    for i in value:
        if(i.islower()):
            ret.append(i)
            sum += 1
    result.append((ret,sum))

def Capital(value,result):
    print("Thread ID is: ",get_ident())
    print("Thread Name:", current_thread())
    sum = 0
    ret = list()
    for i in value:
        if(i.isupper()):
            ret.append(i)
            sum += 1
    result.append((ret,sum))

def Digits(value,result):
    print("Thread ID is: ",get_ident())
    print("Thread Name:", current_thread())
    sum = 0
    ret = list()
    for i in value:
        if(i.isdigit()):
            ret.append(i)
            sum += 1
    result.append((ret,sum))


def main():
    uInput = input("Enter the string you want: ")
    smallList = list()
    t1_obj = Thread(target=Small,args=(uInput,smallList), name="Small")
    capitalList = list()
    t2_obj = Thread(target=Capital,args=(uInput,capitalList),name="Capital")
    digitList = list()
    t3_obj = Thread(target=Digits,args=(uInput,digitList),name="Digits")
    t1_obj.start()
    t2_obj.start()
    t3_obj.start()
    t1_obj.join()
    t2_obj.join()
    t3_obj.join()

    smallDisplay,smallCount = smallList[0]
    capitalDisplay,capitalCount = capitalList[0]
    digitDisplay,digitSum = digitList[0]

    print(f"The list of lowercase letters in given string is: {smallDisplay} and count of the lowercase letters is {smallCount}")
    print(f"The list of the uppercase letters in given string is {capitalDisplay} and their count is {capitalCount}")
    print(f"The list of digits in the given string is {digitDisplay} and their count is {digitSum}")

if (__name__=="__main__"):
    main()
