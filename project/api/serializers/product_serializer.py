from rest_framework import serializers
from api.models import ProductModel
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
	name = serializers.CharField(min_length=1, max_length=20, required=True)
	image_link = serializers.URLField(min_length=10, max_length=100, validators=[UniqueValidator(queryset=ProductModel.objects.all())])

	class Meta:
			model = ProductModel
			fields = ['id', 'name', 'image_link']
