# Generated by Django 3.1.6 on 2021-02-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site_app', '0011_auto_20210224_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_image_post',
            field=models.ImageField(default='images/default_blog_image.jpg', upload_to='images/'),
        ),
    ]
