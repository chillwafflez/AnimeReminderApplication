from fetchMethods import *

data = getWatchList("chillwafflez")
#this gets gurren lagann's "media" fields/info
print(data["data"]['MediaListCollection']['lists'][0].get('entries')[0].get('media'))

#exp: this gets gurren lagann's status (finished)
print(data["data"]['MediaListCollection']['lists'][0].get('entries')[0].get('media').get('status'))