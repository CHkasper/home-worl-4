from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 3'
    )
    image4 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 4'
    )

    title_video = models.CharField(
        max_length=155,
        verbose_name='Заголовок Видео'
    )
    description_video = models.CharField(
        max_length=255,
        verbose_name='Описание Видео'
    )
    url_video = models.URLField(
        verbose_name='Ссылка на видео'
    )
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Баннера'

class Text(models.Model):
    text = models.CharField(
        max_length=50,
        verbose_name='Текст'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Текс'

class Image(models.Model):
    image = models.ImageField(
        upload_to='image',
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to='image',
        verbose_name='Фото 2'
    )

    class Meta:
        verbose_name_plural = 'Фото'