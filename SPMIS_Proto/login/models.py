from django.db import models


class paperHolder(models.Model):
	user_id = models.IntegerField()
	papername = models.TextField(max_length=500, blank=True)
	url = models.TextField(max_length=500, blank=True)
	date = models.TextField(max_length=100, blank=True)

