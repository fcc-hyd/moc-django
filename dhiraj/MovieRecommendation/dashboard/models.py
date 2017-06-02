from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
tbl_MST_User 
  - user_id*
  - email_address
  - password

tbl_MST_Movie
  - movie_id*
  - movie_name
  - movie_duration
  - movie_release_date
  - movie_director
  - movie_lead_roles
  - movie_writer
  - movie_banner_link
  - movie_average_rating
  - movie_genre
  - movie_storyline
  - movie_certificate
  - movie_language

tbl_TRN_Watchlist
  - watchlist_id*
  - user_id
  - movie_id

tbl_MST_User_Rating
  - user_rating_id*
  - user_id
  - movie_id
  - rating

tbl_MST_User_Comments
  - user_comments_id*
  - user_id
  - movie_id
  - comment

"""
class tbl_MST_User(models.Model):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=70,unique=True)
	password = models.CharField(max_length=35)

class tbl_MST_Director(models.Model):
	director_id = models.AutoField(primary_key=True)
	movie_director = models.CharField(max_length = 30)
	movie_writer = models.CharField(max_length = 30)
	movie_genre = models.CharField(max_length = 10)

class tbl_MST_Movie(models.Model):
	movie_id = models.AutoField(primary_key=True)
	director_id = models.ForeignKey(tbl_MST_Director, on_delete=models.CASCADE, default=1)
	movie_name = models.CharField(max_length=30)
	movie_duration = models.CharField(max_length=7)
	movie_release_date = models.DateField()
	movie_lead_roles = models.CharField(max_length=300)
	movie_banner_link = models.CharField(max_length=200)
	movie_average_rating = models.IntegerField()
	movie_storyline = models.CharField(max_length=500)
	movie_certificate = models.CharField(max_length=3)
	movie_language = models.CharField(max_length=15)

class tbl_TRN_Watchlist(models.Model):
	watchlist_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(tbl_MST_User, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(tbl_MST_Movie, on_delete=models.CASCADE)

class tbl_TRN_User_Rating(models.Model):
	user_rating_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(tbl_MST_User, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(tbl_MST_Movie, on_delete=models.CASCADE)
	rating = models.IntegerField()

class tbl_TRN_User_Comments(models.Model):
	user_comments_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(tbl_MST_User, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(tbl_MST_Movie, on_delete=models.CASCADE)
	comment = models.CharField(max_length=500)