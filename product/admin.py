from django.contrib import admin
from product.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('name', 'slug', 'content', 'price', 'published', 'image')}),
    )

    list_display = ('slug', 'name', 'price', 'published' )
    list_editable = ( 'name', 'price', 'published' )
    list_filter = ('published', )
    search_fields = ('name', 'content',)