from django.db import models

class Humans(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    biography = models.TextField(blank=None, verbose_name='Биография')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения записи')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', null=True, verbose_name='Фото')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-create_at']

class Profession(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Профессия')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Професии'
        ordering = ['title']
