

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Професии',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Humans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('biography', models.TextField(blank=None, verbose_name='Биография')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения записи')),
                ('is_published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('photo', models.ImageField(null=True, upload_to='media/%Y/%m/%d')),
                ('profession', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Humans.profession', verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Человека',
                'verbose_name_plural': 'Люди',
                'ordering': ['-create_at'],
            },
        ),
    ]
