from django.db import models
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(verbose_name='nomi', max_length=255)
    description = CKEditor5Field(verbose_name='izohi')
    price = models.IntegerField(verbose_name='Narxi')
    category = models.ForeignKey('apps.Category', CASCADE, verbose_name='categoryasi')


class Image(models.Model):
    product = models.ForeignKey('apps.Product', CASCADE)
    image = models.ImageField(verbose_name='Rasm')


class Post(models.Model):
    user = models.ForeignKey('auth.User', CASCADE)
    title = models.TextField(verbose_name='Sarlavha')
    body = models.TextField(verbose_name='Tana')


class Comment(models.Model):
    post = models.ForeignKey('apps.Post', CASCADE, verbose_name='user_id')
    name = models.CharField(max_length=255, verbose_name='nomi')
    email = models.CharField(max_length=255, verbose_name='emaili')
    body = models.TextField(verbose_name='tanasi')


class Album(models.Model):
    user = models.ForeignKey('auth.User', CASCADE, verbose_name='user_id')
    title = models.TextField(verbose_name='sarlavha')


class Photo(models.Model):
    album = models.ForeignKey('apps.Album', CASCADE, verbose_name='album_id')
    title = models.TextField(verbose_name='sarlavha')
    url = models.TextField(verbose_name='urli')
    thumbnail_url = models.TextField(verbose_name='eskiz URL manzili')


class Todo(models.Model):
    user = models.ForeignKey('auth.User', CASCADE, verbose_name='user_id')
    title = models.TextField(verbose_name='sarlavha')
    completed = models.BooleanField(verbose_name='yakunlandi')


class People(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='ism')
    last_name = models.CharField(max_length=50, verbose_name='sharif')
    photo = models.ImageField(upload_to='people')
    professional = models.CharField(max_length=50, verbose_name='kasb')
