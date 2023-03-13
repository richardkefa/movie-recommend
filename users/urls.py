from django.urls import path
from .views import index,login_view, logout_view

urlpatterns = [
    path('register/', index, name = 'register'),
    # path('', recommend_movies, name='recommend_movies'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]