from django.db import models

class ProductModel(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=20, unique=True)
	image_link = models.URLField(max_length=100, unique=True)
	category = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.name
