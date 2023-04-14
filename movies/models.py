from django.db import models
from django.contrib.auth.models import User
 
class Movies(models.Model):
  title = models.CharField(max_length=200)
  genre = models.CharField(max_length=200)
  rating = models.FloatField()
  description = models.TextField()
  api_id = models.IntegerField()

  def __str__(self):
    return self.title
    
class favoriteUserGenre(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
  genre = models.CharField(max_length=200,blank=True) 

  def __str__(self):
    return self.genre
