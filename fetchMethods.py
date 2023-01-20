import requests

#enter anime name, get info about it back
def searchAnime(name_):
  #Here we define our query as a multi-line string
  query = '''
  query($title: String){
  Media(search: $title, type: ANIME) {
    id
    genres
    status
    episodes
    title {
      english
      romaji
    }
    description
    }
  }
  '''
  #Define our query variables and values that will be used in the query request
  variables = {
      "title": name_
  }

  url = 'https://graphql.anilist.co'
  #Make the HTTP Api request
  response = requests.post(url, json={'query': query, 'variables': variables})
  return response.json()

#enter anime name, get some anime info and info about its next episode back
def getNextEpisode(name_):
  query = '''
  query($title: String){
  Media(search: $title, type: ANIME) {
    id
    episodes
    title {
      english
    }
    nextAiringEpisode {
      id
      airingAt
      timeUntilAiring
      episode
      } 
    }
  }
  '''

  variables = {
      "title": name_
  }

  url = 'https://graphql.anilist.co'
  #Make the HTTP Api request
  response = requests.post(url, json={'query': query, 'variables': variables})
  return response.json()
