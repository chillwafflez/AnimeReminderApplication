from fetchMethods import *
import time

data = getWatchList("chillwafflez")
#this gets gurren lagann's "media" fields/info
#print(data["data"]['MediaListCollection']['lists'][0].get('entries')[0].get('media'))

#exp: this gets gurren lagann's status (finished)
#print(data["data"]['MediaListCollection']['lists'][0].get('entries')[0].get('media').get('status'))


animeListNAMES = []

for i in range(len(data["data"]['MediaListCollection']['lists'][0].get('entries'))):

    if (data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('status') == 'RELEASING'):
        animeListNAMES.append(data["data"]['MediaListCollection']['lists'][0].get('entries')[i].get('media').get('title').get('english'))

for anime in animeListNAMES:
    nextEp = getNextEpisode(anime)
    print(nextEp["data"]["Media"]["nextAiringEpisode"]["airingAt"])
    print(anime)

t = time.time()
currentTimeSeconds = int(t)
print(currentTimeSeconds)