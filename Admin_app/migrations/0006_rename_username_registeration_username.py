# Generated by Django 4.1.5 on 2023-02-27 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0005_rename_fullname_registeration_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeration',
            old_name='Username',
            new_name='username',
        ),
    ]