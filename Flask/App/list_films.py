import urllib.request
import json

def result_films(type):
    if type == "Popular":
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=af5bcc9570d838260f1c1e42aac760c9'
    elif type == "Animation":
        url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&with_genres=16&api_key=af5bcc9570d838260f1c1e42aac760c9'
    elif type == "Nota_10":
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=af5bcc9570d838260f1c1e42aac760c9'
        
    answer = urllib.request.urlopen(url)

    data = answer.read()

    data_json = json.loads(data)

    return data_json['results']

