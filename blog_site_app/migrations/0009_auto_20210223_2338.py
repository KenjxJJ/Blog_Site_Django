# Generated by Django 3.1.6 on 2021-02-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site_app', '0008_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='isLiked',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
