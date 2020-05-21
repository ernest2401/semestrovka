from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

class Ad(models.Model):
    title = models.CharField(max_length = 50,verbose_name="Товар")
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    content = models.TextField(null=True,blank=True,verbose_name='Описание')
    price = models.FloatField(null=True,blank=True,verbose_name='Цена')
    publish = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric',null = True,on_delete=models.PROTECT,verbose_name='Рубрика')
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='bboard/',blank=True,null=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked',blank=True)

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = 'Объявление'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ad:ad_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

class Rubric(models.Model):
    name = models.CharField(max_length = 20,db_index = True,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Рубрика'
        verbose_name_plural ="Рубрики"
        ordering = ['name']

class Comment(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.SET_NULL,null=True,blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural ="Комментарии"
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.ad)

class Wish(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Автор')
    body = models.TextField(verbose_name="Отзыв")
    number = models.CharField(max_length=20,verbose_name="Номер телефона")

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural ="Отзывы"

    def __str__(self):
        return self.body
