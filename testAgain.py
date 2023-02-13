from win10toast import ToastNotifier
from datetime import datetime
from datetime import date
import schedule
import time
from fetchMethods import *

#method to send Windows notification
def notify(bruh, penis):
    toaster = ToastNotifier()
    toaster.show_toast("wsup" + bruh + "i love " + penis, duration=8)
    print("reached the end")
    return schedule.CancelJob


valid = True

epochTime = 1676288220

format = "%H:%M"

b = datetime.fromtimestamp(epochTime)
nextEpStamp = b.strftime(format)
print(nextEpStamp)

oneminbefore = epochTime - 60
c = datetime.fromtimestamp(oneminbefore)
oneminREminer = c.strftime(format)
print(oneminREminer)

if (valid == True):
    schedule.every().day.at(oneminREminer).do(notify, bruh="daddy", penis="lappland")
    schedule.every().day.at(nextEpStamp).do(notify, bruh="mommy", penis = "texas")
else:
    print("nah bruh")

all_jobs = schedule.get_jobs()
print(all_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)

