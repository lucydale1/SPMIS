from django.db import models


class paperHolder(models.Model):
	user_id = models.IntegerField()
	papername = models.TextField(max_length=500, blank=True)
	url = models.TextField(max_length=500, blank=True)
	date = models.TextField(max_length=100, blank=True)

	def createList(self):
		return [papername, url, date]

class variable_holder(models.Model):
    counter = models.IntegerField()

    def getCounter(self):
        return self.counter
