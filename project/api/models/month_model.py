from django.db import models

class MonthModel(models.Model):
	id = models.PositiveBigIntegerField(primary_key=True)
	name = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name
