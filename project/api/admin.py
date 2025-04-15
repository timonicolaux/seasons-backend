from django.contrib import admin
from .models import MonthModel

@admin.register(MonthModel)
class MonthAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
