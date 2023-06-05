from django.contrib import admin
from blog.models import Post


# admin.site.register(Post) простой пример добавления в админку моделей

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_update', 'author']  # колонки в списке в админке в постах
    prepopulated_fields = {'slug': ('title',)}  # автоматическое подставление sluga при заполнении базы
