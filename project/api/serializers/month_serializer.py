from rest_framework import serializers
from api.models import MonthModel

class MonthSerializer(serializers.ModelSerializer):
	name = serializers.CharField(min_length=1, max_length=10, required=True)

	class Meta:
		model = MonthModel
		fields = ['id', 'name']
