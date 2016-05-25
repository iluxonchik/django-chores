from django.db import models

# Create your models here.

class ChoreList(models.Model):
	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()

class Chore(models.Model):
	chore_list = models.ForeignKey(ChoreList)
	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()
	complete = models.BooleanField(default=True)
