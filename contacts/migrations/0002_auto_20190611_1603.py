# Generated by Django 2.2.1 on 2019-06-11 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ser_id',
            new_name='user_id',
        ),
    ]
