# Generated by Django 4.2 on 2023-05-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0016_alter_blogimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(blank=True, default='media/blog/default_image.jpeg', upload_to='blog'),
        ),
    ]
