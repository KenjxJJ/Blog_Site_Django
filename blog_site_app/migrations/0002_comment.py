# Generated by Django 3.1.6 on 2021-02-18 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_site_app.blogpost')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
