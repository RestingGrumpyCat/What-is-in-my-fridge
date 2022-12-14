# Generated by Django 4.1.2 on 2022-10-29 11:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_image_url_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe_id',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('imageType', models.CharField(blank=True, max_length=20, null=True)),
                ('servings', models.IntegerField(blank=True, null=True)),
                ('readyInMinutes', models.IntegerField(blank=True, null=True)),
                ('license', models.CharField(blank=True, max_length=20, null=True)),
                ('sourceName', models.CharField(blank=True, max_length=100, null=True)),
                ('sourceUrl', models.CharField(blank=True, max_length=100, null=True)),
                ('spoonacularSourceUrl', models.CharField(blank=True, max_length=100, null=True)),
                ('aggregateLikes', models.IntegerField(blank=True, null=True)),
                ('healthScore', models.IntegerField(blank=True, null=True)),
                ('spoonacularScore', models.IntegerField(blank=True, null=True)),
                ('pricePerServing', models.IntegerField(blank=True, null=True)),
                ('extendedIngredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), size=None)),
            ],
        ),
    ]
