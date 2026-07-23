from time import sleep
import schedule 

def DisplayMesssage(message):
    print(message)

def main():
    message = input("Enter the message: ")
    schedule.every(5).seconds.do(DisplayMesssage,message)
    while(True):
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()