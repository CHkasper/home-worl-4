from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptio = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О нас'

class Team(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptio = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Команда'

class Award(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="награда"
    )  
    description = models.TextField(
        verbose_name="описание награды"
    )  
    count = models.TextField(
        verbose_name="количество наград"
    )  

    def __str__(self):
        return f"{self.title} ({self.count} Awards)"

class Need(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="мотивируеший предложения"
    )
    text = models.TextField(
        verbose_name="что ты можешь предложить"
    )
    def __str__(self):
        return f"{self.title} ({self.text})"

class Title(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="заголовок"
    )
    text = models.TextField(
        verbose_name="текст"
    )
    text2 = models.TextField(
        verbose_name="текст2"
    )
    class Meta:
        verbose_name_plural = 'Заголовок'
        
class Contact(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="контакт "
    )
    desc1 = models.TextField(
        verbose_name="описание"
    )
    desc2 = models.TextField(
        verbose_name="описание"
    )
    class Meta:
        verbose_name_plural = 'контакт'