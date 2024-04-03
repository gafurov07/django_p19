from _ast import Import

from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.models import Category, Product, Image, Post, Comment, Album, Photo, Todo, People

admin.site.unregister(User)
admin.site.unregister(Group)


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductImageStackedInline(admin.StackedInline):
    model = Image
    extra = 1
    min_num = 1
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']
    search_fields = ['name', 'category']
    autocomplete_fields = ['category']
    inlines = [ProductImageStackedInline]


class PostCommentStackedInline(admin.StackedInline):
    model = Comment
    extra = 1
    min_num = 1
    max_num = 10


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'title', 'body']
    search_fields = ['user_id']
    # autocomplete_fields = ['user_id']
    inlines = [PostCommentStackedInline]


class PhotoStackedInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user']
    # autocomplete_fields = ['user']
    inlines = [PhotoStackedInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['album', 'title', 'url', 'thumbnail_url']
    search_fields = ['album']
    # autocomplete_fields = ['album']


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'completed']
    search_fields = ['user']
    # autocomplete_fields = ['user']


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'photo', 'professional']
