import requests

#my unique access code to request information from the api
key = 'dec8a2ab'
#url of the api that I am requesting information from
base_url = 'http://www.omdbapi.com/'
#name of a movie to search for
movieName = input('What movie would you like to search for?\n')
#provide apikey to get access
#'t' is in api documentation: searches movies by name
params = {'apikey': key, 't': movieName}
#request a json object containing info from the movie
#store the json object to display it or get specific information from it
data = requests.get(base_url, params).json()
#view all data in json object
print('data:')
print(data)
#show rating information
print("Ratings: ")
print(data['Ratings'][0]['Value'])
print("Metascore: ")
print(data['Metascore'])
