from django.contrib import admin
from .models import Humans, Profession

class HumansAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'name', 'biography', 'create_at', 'photo', 'is_published')
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ('id', 'name')
    list_editable = ('profession', 'is_published')


admin.site.register(Humans, HumansAdmin)

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id','title']
    search_fields = ['title']


admin.site.register(Profession, ProfessionAdmin)
