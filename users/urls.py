from django.urls import path
from .views import index,login_view, logout_view,register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register_view, name = 'register'),
    # path('', recommend_movies, name='recommend_movies'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]