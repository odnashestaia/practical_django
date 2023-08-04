# Generated by Django 4.1.7 on 2023-07-24 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_alter_post_likes_post_alter_post_save_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.TextField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('like_comment', models.ManyToManyField(blank=True, related_name='likes_blog_comment', to=settings.AUTH_USER_MODEL)),
                ('name_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_blog', to='blog.post')),
                ('reply_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies_comment', to='blog.comment')),
            ],
        ),
    ]