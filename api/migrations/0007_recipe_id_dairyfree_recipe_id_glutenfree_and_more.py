# Generated by Django 4.1.2 on 2022-10-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_recipe_id_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_id',
            name='dairyFree',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe_id',
            name='glutenFree',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe_id',
            name='vegan',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe_id',
            name='vegetarian',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
