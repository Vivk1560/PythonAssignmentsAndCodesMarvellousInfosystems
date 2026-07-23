import schedule 
from time import sleep

def weeklyMonday():
    print("Start Your Weekly Goals")

def weeklyWednesday():
    print("Review your weekly progress")

def weeklyFriday():
    print("Weekly Work Completed")

def main():
    schedule.every().monday.at("9:00").do(weeklyMonday)
    schedule.every().wednesday.at("17:00").do(weeklyWednesday)
    schedule.every().friday.at("18:00").do(weeklyFriday)
    while(True):
        schedule.run_pending()
        sleep(300)

if __name__ == "__main__":
    main()