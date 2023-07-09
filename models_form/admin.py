from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'birthday']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_author']
