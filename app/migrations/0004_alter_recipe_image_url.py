# Generated by Django 4.1.2 on 2023-06-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_recipe_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.ImageField(blank=True, default='media/images/default.jpg', null=True, upload_to='media/images/'),
        ),
    ]
