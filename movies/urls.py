from .views import get_movies_api
from django.urls import path


urlpatterns = [
    path('', get_movies_api,name='get_movies_from_api'),
]