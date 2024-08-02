from django.contrib import admin
from core.models import Meta, About, AboutImage, SectionName


@admin.register(Meta)
class AdminMeta(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('title', 'description', 'intro_text')}),
    )

    list_display = ('title', 'description', 'intro_text')
    list_editable = ('description', 'intro_text')
    search_fields = ('title', 'description', 'intro_text')


class AdminAboutImageInline(admin.TabularInline):
    model = AboutImage


@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    inlines = [
        AdminAboutImageInline
    ]
    fieldsets = (
        ('Информация', {
            'fields': ('name', 'left_content', 'right_content')}),
    )

    list_display = ('name',)


@admin.register(SectionName)
class AdminSectionName(admin.ModelAdmin):
    fieldsets = (
        ('Информация', {
            'fields': ('product_name', 'review_name')}),
    )

    list_display = ('product_name', 'review_name')