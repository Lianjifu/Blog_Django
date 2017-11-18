from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title','created_time','modified_time','excerpt','category','author']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


