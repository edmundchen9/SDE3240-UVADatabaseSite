# Generated by Django 4.1.1 on 2022-10-14 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_summary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='myUser',
        ),
    ]
