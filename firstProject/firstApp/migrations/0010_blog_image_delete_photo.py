# Generated by Django 4.2 on 2023-05-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0009_remove_blog_image_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]