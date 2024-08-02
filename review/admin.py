from django.contrib import admin
from review.models import Review

@admin.register(Review)
class ReviewProduct(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('name', 'content', 'date', 'image', 'published')}),
    )

    list_display = ('name', 'image', 'published' )
    list_editable = ( 'image', 'published'  )
    list_filter = ('published', )
    search_fields = ('name', 'content',)