# Generated by Django 2.2 on 2019-05-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
