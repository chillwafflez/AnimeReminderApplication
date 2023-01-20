from fetchMethods import *
from win10toast import ToastNotifier
import schedule
import time
from datetime import datetime



toaster = ToastNotifier()
toaster.show_toast("Wsup", "cock", duration=3)

#print(searchAnime("Attack on Titan"))
data = getNextEpisode("Vinland Saga Season 2")
airingAt = data['data']['Media']['nextAiringEpisode']['airingAt']
timeUntilAiring = data['data']['Media']['nextAiringEpisode']['timeUntilAiring']
print(airingAt)
print(timeUntilAiring)

