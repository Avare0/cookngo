# Generated by Django 2.2 on 2019-05-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20190526_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='diff',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], null=True),
        ),
    ]