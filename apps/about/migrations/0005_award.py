# Generated by Django 5.1.7 on 2025-03-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_delete_recog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='награда')),
                ('description', models.TextField(verbose_name='описание награды')),
                ('count', models.TextField(verbose_name='количество наград')),
            ],
        ),
    ]
