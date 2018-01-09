import requests

#todo get data from server
#todo make request(probably with 'requests')
#todo store JSON data retrieved from request
#todo get the data needed from JSON ('requests' has parser for JSON to Python Dictionary)
#todo handle errors(access denied, no network connection, invalid response)

key = 'dec8a2ab'

base_url = 'http://www.omdbapi.com/'

movie = input('What movie name?')

params = { 'apikey' : key, 't' : movie }
data = requests.get(base_url, params ).json()

print(data)

print("Rating for that movie: ")
print(data['Ratings'][0]['Value'])