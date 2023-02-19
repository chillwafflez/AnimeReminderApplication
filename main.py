from win10toast import ToastNotifier
from datetime import datetime
from datetime import date
import schedule
import time
from fetchMethods import *

#method to send Windows notification
def notify(name, timeLeft):
    toaster = ToastNotifier()
    toaster.show_toast(name + " is airing in " + timeLeft + " minutes.", duration=8)
    print("reached the end")
    return schedule.CancelJob

#sets jobs/reminders for 2 timestamps for each anime in my currently watching/releasing list
def setSchedule(name_):
    format = "%H:%M"

    #gets airtime and amount of time before airtime for next episode
    timeData = getNextEpisode(name_)
    airTime = timeData["data"]["Media"]["nextAiringEpisode"]["airingAt"]
    timeUntilAiring = timeData["data"]["Media"]["nextAiringEpisode"]["timeUntilAiring"]

    #this gets todays date and the next episode date in a similar format to compare
    dayFormat = "%m/%d/%Y"
    today= date.today()
    a = datetime.fromtimestamp(airTime)
    nextEpDate = a.strftime(dayFormat)
    todayDate = today.strftime(dayFormat)

    #if the next episode's date and the current date are equal, we can safely make reminders
    if (nextEpDate == todayDate):
        #set job for scheduler at airtime
        b = datetime.fromtimestamp(airTime)
        nextEpStamp = b.strftime(format)    
        schedule.every().day.at(nextEpStamp).do(notify, name = name_, timeLeft = "now").tag("anime")

        #if the time between now and airtime is more than 60 mins, set reminder for hour before release
        if (timeUntilAiring > 3600):
            #timestamp for 60 minutes before airtime
            sixtyMin = airTime - 3600
            c = datetime.fromtimestamp(sixtyMin)
            _60minReminder = c.strftime(format)

            #set job for scheduler 1 hour before airtime
            schedule.every().day.at(_60minReminder).do(notify, name = name_, timeLeft = "1").tag("anime")


#this gets list of shows that are releasing episodes, and makes reminders for their next episode
def setReminders() -> bool:
    #get list of my currently watching anime (that is currently releasing episodes)
    data = getWatchList("chillwafflez")
    releasingAnime = []
    for i in range(len(data["data"]['MediaListCollection']['lists'][0].get('entries'))):

        #if anime in currently watching list that is currently RELEASING episodes, add it to list
        if (data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('status') == 'RELEASING'):
            releasingAnime.append(data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('title').get('english'))

    #set reminders for each anime using scheduler
    for anime in releasingAnime:
        setSchedule(anime)

    #check to see if it correctly made reminders
    all_jobs = schedule.get_jobs()
    print(all_jobs)
    if not all_jobs:
        return False
    else:
        return True
    
def resetScheduler():
    schedule.clear('anime')
    main()

#executes once you run program. starts off with setting reminders and 
def main():
    print("Starting program...")
    remindersToday = setReminders()
    if (remindersToday):
        print("There are episodes airing today")
    else:
        print("There are no episodes airing today")
    schedule.every().day.at("00:00").do(resetScheduler)

if __name__ == "__main__":
    main()

while (True):
    schedule.run_pending()
    time.sleep(1)

