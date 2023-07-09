from django.db import models
from django.urls import reverse

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.')
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    def get_author(self):
        return '\n'.join([p.name for p in self.author.all()])
