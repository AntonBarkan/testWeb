from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=250)
	text = models.CharField(max_length=1000)
	addet_at = models.DateTimeField()
	rating = models.IntegerField(default=0)
	author = models..ForeignKey(models.User)
	likes = models.IntegerField(default=0)

class Answer(models.Model):
	text = models.CharField(max_length=1000)
	addet_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author= models..ForeignKey(models.User)
