# Generated by Django 4.1.7 on 2023-04-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, help_text='не более 200 символов', max_length=200),
        ),
    ]
