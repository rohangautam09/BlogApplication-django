from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	pic = models.ImageField(upload_to='images',blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.content[:120] + ("...")


	class Meta:
		ordering = ['-date_posted']

# Create your models here.
