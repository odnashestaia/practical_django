from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver

from pytils.translit import slugify

""" варианты авто заполнения slug, которые не работают с кирилицей """
# from django.template.defaultfilters import slugify
# from django.utils.text import slugify


"""
вариант автоперевода с кирилицы на латиницу рабочий грамоский вариант лучше использовать pytils

from django.template.defaultfilters import slugify as django_slugify
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):

    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))
"""


class Post(models.Model):
    # мета опции
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    # поля моделей
    title = models.CharField(max_length=200, help_text='не более 200 символов',
                             db_index=True)  # в скобках опции\настройки моделей
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов') стандартное добавление контента

    content = RichTextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов')
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # null=True что бы могли писать не зарегистрированые пользователи
    # в url при использовании slug обязательно добавляем id + get_absolute_url()
    slug = models.SlugField(max_length=50)  # , unique=True добавить потом
    likes_post = models.ManyToManyField(User, related_name='post_comment', blank=True)
    save_posts = models.ManyToManyField(User, related_name='save_posts', blank=True)

    # reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # методы моделей
    def total_likes(self):
        # подсчет лайков
        return self.likes_post.count()

    def total_save(self):
        # подсчет сохранены постов
        return self.save_posts.count()

    def get_absolute_url(self):
        # даеться уникальный url для постов (пример: users_id/post_slug)
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        # вывод названия поста в админке
        return self.title


@receiver(pre_save, sender=Post)
# сигнал создание слага перед сохранением в базу
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
