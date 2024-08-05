import urllib.request
import json
import os

api_key = os.environ.get('API_KEY')

def result_films(type):
    if type == "Popular":
        url = f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}'
    elif type == "Animation":
        url = f'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&with_genres=16&api_key={api_key}'
    elif type == "Nota_10":
        url = f'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key={api_key}'
        
    answer = urllib.request.urlopen(url)

    data = answer.read()

    data_json = json.loads(data)

    return data_json['results']

