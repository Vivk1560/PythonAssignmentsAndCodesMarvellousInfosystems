from time import sleep
import schedule 

def displayLunch():
    print("Lunch Time")

def displayWork():
    print("Wrap Up Work!")

def main():
    schedule.every().day.at("13:00").do(displayLunch)
    schedule.every().day.at("18:00").do(displayWork)

    while(True):
        schedule.run_pending()
        sleep(240)

if __name__=="__main__":
    main()