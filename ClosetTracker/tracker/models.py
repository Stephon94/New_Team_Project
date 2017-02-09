#from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# class UserProfile(models.Model):
# 	#This line is required. Links UserProfile to a User model instance.
# 	user = models.OneToOneField(User, related_name="user")

# 	#The additional attributes we wish to include.
# 	# picture = models.ImageField(upload_to='profile_images', blank=True)
# 	bio = models.TextField(blank=True)

# 	def __unicode__(self):
# 		return self.user.username
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		self.user.username

class ClothingType(models.Model):
	name = models.CharField(max_length=128, unique=True)
	user = models.ForeignKey(User)
	price = models.IntegerField(default=0)
	picture = models.ImageField()
	purchased_at = models.DateTimeField(auto_now=True)
	pos_x = models.IntegerField(default=0)
	pos_y = models.IntegerField(default=0)
	pos_z = models.IntegerField(default=0)

class Size(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Color(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Season(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Accessory(models.Model):
	name = models.CharField(max_length=128, unique=True)
	user = models.ForeignKey(User)


