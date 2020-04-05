from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)   #one user one profile and CASCADE: if we delete the user profile will also be deleted
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	bio = models.TextField()

	def __str__(self):
		return self.user.username




# Create your models here.
