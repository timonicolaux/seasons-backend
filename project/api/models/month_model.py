from django.db import models

class MonthModel(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=10, unique=True)
	products = models.ManyToManyField("api.ProductModel", related_name="months", blank=True)

	def __str__(self):
		return self.id
