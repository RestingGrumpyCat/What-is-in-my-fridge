# Generated by Django 4.1.2 on 2022-10-29 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_recipe_id_spoonacularscore_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_id',
            name='summary',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]