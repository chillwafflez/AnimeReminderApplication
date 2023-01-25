from win10toast import ToastNotifier
from datetime import datetime
import schedule
import time

anime = [1674638486]
running = 0


#method to send notification
def notify(tag):
    global running
    running += 1
    toaster = ToastNotifier()
    toaster.show_toast("Anime Notification is airing in  minutes.", duration=10)
    print("reached the end")
    return schedule.cancel_job(tag)

for i in range(len(anime)):
    format = "%H:%M"

    threeMin = anime[i] - 180
    t = datetime.fromtimestamp(threeMin)
    stopTimestamp3min = t.strftime(format)
    tag3 = "3min"

    fiveMin = anime[i] - 300
    p = datetime.fromtimestamp(fiveMin)
    stopTimestamp5min = p.strftime(format)
    tag5 = "5min"

    print(stopTimestamp3min)
    print(stopTimestamp5min)

    schedule.every().day.at(stopTimestamp3min).do(notify, tag = tag3).tag(tag3)
    schedule.every().day.at(stopTimestamp5min).do(notify, tag = tag5).tag(tag5)

    

while running !=2:
    schedule.run_pending()
    time.sleep(1)
