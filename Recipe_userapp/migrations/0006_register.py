# Generated by Django 3.2.18 on 2023-04-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_userapp', '0005_rename_contactdb_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('name1', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
