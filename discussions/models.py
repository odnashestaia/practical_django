from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from pytils.translit import slugify


class Discussion(models.Model):
    class Meta:
        verbose_name = 'Дискуссия'
        verbose_name_plural = 'Дискуссии'

    title = models.CharField(max_length=200, help_text="не более 200 символов", db_index=True)
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов')
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # null=True что бы могли писать не зарегистрированые пользователи
    # в url при использовании slug обязательно добавляем id + get_absolute_url()
    slug = models.SlugField(max_length=50)  # , unique=True добавить потом
    likes = models.ManyToManyField(User, related_name='discussion_comment', blank=True)
    saves_posts = models.ManyToManyField(User, related_name='save_discussions', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussion(self):
        return self.likes.count()

    def total_saves_discussions(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # методы модели
    def __str__(self):
        return self.title

