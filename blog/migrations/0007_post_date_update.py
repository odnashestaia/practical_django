# Generated by Django 4.1.7 on 2023-04-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
