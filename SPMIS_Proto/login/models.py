from django.db import models

class paperHolder(models.Model):
	doi = models.TextField(max_length=100, primary_key=True)
	user_id = models.IntegerField()
	papername = models.TextField(max_length=500, blank=True)
	url = models.TextField(max_length=500, blank=True)
	date = models.TextField(max_length=100, blank=True)

	def createList(self):
		return [papername, url, date]

class variable_holder(models.Model): #useless now?
	counter = models.IntegerField()

	def getCounter(self):
		return self.counter

class historyHolder(models.Model):
	user_id = models.IntegerField()
	searchQuery = models.TextField(max_length=500, blank=True)
	dateAndTime = models.DateTimeField()
	
	def __str__(self):
		return self.title