# Generated by Django 4.1.5 on 2023-02-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0004_registeration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeration',
            old_name='fullname',
            new_name='Username',
        ),
    ]
