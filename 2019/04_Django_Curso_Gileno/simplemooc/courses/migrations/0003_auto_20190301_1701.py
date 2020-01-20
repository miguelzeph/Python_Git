# Generated by Django 2.1.7 on 2019-03-01 20:01

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190228_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('new_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o Curso'),
        ),
    ]
