# Generated by Django 3.2.18 on 2023-04-27 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_userapp', '0002_auto_20230427_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='message1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='name1',
        ),
    ]
