from django.contrib import admin
from .models import Author, Post, Category, Tag

class AuthorList(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Author, AuthorList)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)