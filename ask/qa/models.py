from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=250, null=True)
	text = models.CharField(max_length=1000, null=True)
	addet_at = models.DateTimeField(null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True)
	likes = models.CharField(max_length=1000, null=True)
	
	def __unicode__(self):
		return self.title

class Answer(models.Model):
	text = models.CharField(max_length=1000,null=True)
	addet_at = models.DateTimeField(null=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author= models.ForeignKey(User, null=True)
