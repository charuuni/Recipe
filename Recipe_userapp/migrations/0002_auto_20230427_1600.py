# Generated by Django 3.2.18 on 2023-04-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='recipe',
        ),
    ]
