# Generated by Django 4.1.2 on 2022-10-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_recipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_id',
            name='spoonacularScore',
        ),
        migrations.AlterField(
            model_name='recipe_id',
            name='summary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
