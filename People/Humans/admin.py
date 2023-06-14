from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Humans, Profession


@admin.register(Humans)
class HumansAdmin(admin.ModelAdmin):
    list_display = 'id', 'profession', 'name', 'biography', 'create_at', 'get_photo', 'is_published'
    list_display_links = 'id', 'name'
    search_fields = 'name',
    list_filter = 'id', 'name'
    list_editable = 'profession', 'is_published'
    fields = 'profession', 'name', 'biography', 'create_at', 'get_photo', 'photo', 'is_published'
    readonly_fields = 'get_photo', 'create_at'

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="40">')
        else:
            return 'Фото отсутствует'


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_display_links = 'id', 'title'
    search_fields = 'title',


admin.site.site_header = 'Страница администратора'
admin.site.site_title = 'Страница администратора'
