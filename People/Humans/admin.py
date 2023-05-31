from django.contrib import admin
from .models import Humans

class HumansAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'biography', 'create_at', 'is_published')
    list_display_links = ['id','name']
    search_fields = ['name']


admin.site.register(Humans, HumansAdmin)
