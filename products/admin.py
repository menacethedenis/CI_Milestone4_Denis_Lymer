from django.contrib import admin
from .models import Product, Category, Turntable, Headphones

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class TurntableAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'belt_type',
        'colour',
    )

    ordering = ('sku',)


class HeadphonesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'earphone_type',
        'colour',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Turntable, TurntableAdmin)
admin.site.register(Headphones, HeadphonesAdmin)
