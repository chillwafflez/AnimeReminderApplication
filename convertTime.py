import requests
from datetime import datetime

# Here we define our query as a multi-line string
query = '''
query($mediaid: Int, $episode: Int, $airedYet: Boolean){
  AiringSchedule(mediaId: $mediaid, episode: $episode, notYetAired: $airedYet) {
    airingAt
    episode
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
  "mediaid": 136430, "episode": 3, "airedYet": True
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})

data = response.json()

airDate = data["data"]["AiringSchedule"]['airingAt']
#print(time.ctime(date))
#print(time.localtime(date))

print(airDate)
x = datetime.fromtimestamp(airDate)
print(x)