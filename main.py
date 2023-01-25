from fetchMethods import *
from win10toast import ToastNotifier
import schedule
import time
from datetime import datetime
from convertTime import *

#CURRENT TEST: VINLAND SAGA SEASON 2 EPISODE 3 
airingAt = 1674465867
name = "Vinland Saga"
fiveMin = convertToTimestamp(airingAt - 300)
test5 = "5"
threeMin = convertToTimestamp(airingAt - 180)
test3 = "3"


data = getNextEpisode("Vinland Saga Season 2")
#airingAt = data['data']['Media']['nextAiringEpisode']['airingAt']
timeUntilAiring = data['data']['Media']['nextAiringEpisode']['timeUntilAiring']

#timestamp of 30 minutes before airing
thirtyMinTIMESTAMP = convertToTimestamp(airingAt - 1800)
timeLeft1 = "30"
#timestamp of 10 minutes before airing
tenMinTIMESTAMP = convertToTimestamp(airingAt - 600)
timeLeft1 = "10"

#method to send notification
def notify(name_, timeLeft):
    global running
    running = False
    toaster = ToastNotifier()
    toaster.show_toast("Anime Notification", name_ + " is airing in " + timeLeft + " minutes.", duration=3)
    return schedule.CancelJob

#method to set schedule for each timestamp
#def setSchedule(stopTimestamp, name_, timeLeft):

schedule.every().day.at(fiveMin).do(notify(name, "5")).tag(name + "|" + test5 + " minutes")
schedule.every().day.at(threeMin).do(notify(name, "3")).tag(name + "|" + test3 + " minutes")
    #while running:
     #   schedule.run_pending()
      #  time.sleep(1)


while running:
    schedule.run_pending()
    time.sleep(1)
    print("end")



#print(searchAnime("Attack on Titan"))
#print(airingAt)
#print(time.ctime(airingAt))
#print(timeUntilAiring)

