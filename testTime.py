from datetime import datetime
import time
import schedule
from win10toast import ToastNotifier
import threading


#currentTimestamp = 167419122
#print(time.ctime(currentTimestamp))

running = True
def wsup():
    global running
    running = False
    toaster = ToastNotifier()
    toaster.show_toast("Wsup", "cock", duration=3)
    print("you should see this at 9:45")
    return schedule.CancelJob


#3 mins from now
currentTimestamp = 1674193711
format = "%H:%M"
t = datetime.fromtimestamp(currentTimestamp)
stopTimestamp = t.strftime(format)



schedule.every().day.at(stopTimestamp).do(wsup)
while running:
    schedule.run_pending()
    time.sleep(1)

print("end")