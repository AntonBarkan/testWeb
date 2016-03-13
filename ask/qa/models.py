from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=250)
	text = models.CharField(max_length=1000)
	addet_at = models.DateTimeField()
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True)
	likes = models.CharField(max_length=1000)

class Answer(models.Model):
	text = models.CharField(max_length=1000)
	addet_at = models.DateTimeField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author= models.ForeignKey(User, null=True)
