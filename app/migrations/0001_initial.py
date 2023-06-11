# Generated by Django 4.1.2 on 2023-05-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('cooking_time', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('ingredient', models.ManyToManyField(to='app.ingredient')),
            ],
        ),
    ]
