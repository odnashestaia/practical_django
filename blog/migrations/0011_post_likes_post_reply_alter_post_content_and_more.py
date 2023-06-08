# Generated by Django 4.1.7 on 2023-04-03 14:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='postcomment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_ok', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='не более 5000 символов', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]