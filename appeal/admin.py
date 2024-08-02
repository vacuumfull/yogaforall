from django.contrib import admin
from appeal.models import Appeal

@admin.register(Appeal)
class AdminAppeal(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('name', 'email', 'phone', 'content', 'file', 'is_checked')}),
    )

    list_display = ('name', 'email', 'phone', 'is_checked', 'created_at')
    list_editable = ('is_checked',)
    list_filter = ('is_checked', )
    search_fields = ('name', 'email',)