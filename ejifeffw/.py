from win10toast import ToastNotifier
from datetime import datetime
import schedule
import time
from fetchMethods import *

running = 0

#method to send notification
def notify(name, timeLeft):
    global running
    running += 1
    toaster = ToastNotifier()
    toaster.show_toast(name + " is airing in " + timeLeft + " minutes.", duration=8)
    print("reached the end")
    return schedule.CancelJob

#sets jobs for each 3 timestamp for each anime for the scheduler
def setSchedule(name_):
    format = "%H:%M"

    #gets airtime and amount of time before airtime for next episode
    timeData = getNextEpisode(name_)
    airTime = timeData["data"]["Media"]["nextAiringEpisode"]["airingAt"]
    timeUntilAiring = timeData["data"]["Media"]["nextAiringEpisode"]["timeUntilAiring"]


    #if the time between airing and now is more than 10 mins, set 10 min reminer
    if (timeUntilAiring > 3600):
        #timestamp for 60 minutes before airtime
        sixtyMin = airTime - 3600
        b = datetime.fromtimestamp(sixtyMin)
        _60minReminder = b.strftime(format)

        #set job for scheduler 1 hour before airtime
        schedule.every().day.at(_60minReminder).do(notify(name_, "1"))


    #if the time between airing and now is more than 10 mins, set 10 min reminer
    if (timeUntilAiring > 600):
        #timestamp for 10 minutes before airtime
        tenMin = airTime - 600
        c = datetime.fromtimestamp(tenMin)
        _10minReminder = c.strftime(format)

        #set job for scheduler 10 minutes before airtime
        schedule.every().day.at(_10minReminder).do(notify(name_, "10"))
    
    #set job for scheduler at airtime
    schedule.every().day.at(airTime).do(notify(name_, "now"))


#get list of currently watching anime (that is currently releasing episodes)
data = getWatchList("chillwafflez")
releasingAnime = []
for i in range(len(data["data"]['MediaListCollection']['lists'][0].get('entries'))):

    #if anime in currently watching list is RELEASING episodes, add it to list
    if (data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('status') == 'RELEASING'):
        releasingAnime.append(data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('title').get('english'))

#set schedules for each anime 
for anime in releasingAnime:
    setSchedule(anime)
    

while running !=2:
    schedule.run_pending()
    time.sleep(1)

