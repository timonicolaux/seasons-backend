from rest_framework import serializers
from api.models import MonthModel
from api.serializers.product_serializer import ProductSerializer

class MonthSerializer(serializers.ModelSerializer):
	name = serializers.CharField(min_length=1, max_length=10, required=True)
	products = serializers.SerializerMethodField()

	class Meta:
		model = MonthModel
		fields = ['id', 'name', 'products']

	def get_products(self, obj):
		category_map = {}

		for product in obj.products.all():
			category = product.category
			if category not in category_map:
				category_map[category] = []
			category_map[category].append(ProductSerializer(product).data)

		return { "categories": category_map }

class MonthMinimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = MonthModel
		fields = ['id', 'name']
