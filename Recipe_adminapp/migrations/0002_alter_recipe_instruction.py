# Generated by Django 3.2.18 on 2023-04-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(max_length=1000),
        ),
    ]
