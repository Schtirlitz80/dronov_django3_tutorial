from django.contrib import admin

from .models import Bb, Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


# Register your models here.
admin.site.register(Bb, BdAdmin)
admin.site.register(Rubric)
