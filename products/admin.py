from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)  # this sorts products by SKU
    # needs to be a tuple since it's possible to sort on multiple columns
    # to reverse it, we can add a '-' infront of 'sku'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
# Register new classes above alongside their respective models
admin.site.register(Category, CategoryAdmin)
