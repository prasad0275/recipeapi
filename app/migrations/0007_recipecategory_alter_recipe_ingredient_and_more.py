# Generated by Django 4.1.2 on 2023-06-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_recipe_dislike_recipe_like_recipe_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='app.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(blank=True, to='app.recipecategory'),
        ),
    ]