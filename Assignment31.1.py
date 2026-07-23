from time import sleep
import schedule 

def display(message):
    print(message)

def main():
    mess = input("Enter the message: ")
    inter = int(input("Enter the time interval after which desired message should be repeated in seconds: "))
    if(inter>0):
        schedule.every(inter).seconds.do(display,mess)
        while(True):
            schedule.run_pending()
            sleep(1)

    else:
        print("Invalid Interval, please input interval greater than zero")
    return

if __name__ == "__main__":
    main()