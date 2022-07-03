#Schedule 
import time
import datetime
import schedule 

def Task():
    
    print("Task after each minute gets excuted")
    print("Current time is : ",datetime.datetime.now())

def main ():
    print("Inside main")
    print("Schedular starts .....")

    schedule.every(1).minutes.do(Task)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()