from django.contrib import admin
from .models import MonthModel, ProductModel

@admin.register(MonthModel)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_products')
    search_fields = ('name',)
    filter_horizontal = ('products',)
    ordering = ('id',)

    def display_products(self, obj):
        return ", ".join(p.name for p in obj.products.all())
    display_products.short_description = 'Produits'

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_link', 'category', 'display_months')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('name',)

    def display_months(self, obj):
        return ", ".join(m.name for m in obj.months.all())
    display_months.short_description = "Mois associés"
