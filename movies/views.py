import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests
from .models import Movies




def get_movies_api(request):
    api_url = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': os.environ.get('MOVIE_API_KEY'),
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        

        
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    results = response.json().get('results', [])
    # import pdb; pdb.set_trace()
    for result in results:
        movie = Movies(
                title=result['title'],
                genre=result['genre_ids'][0],
                rating=result['vote_average'],
                description=result['overview'],
                api_id=result['id'],
            )
        movie.save()
    return render(request, 'home.html', {'movies': results})


