# Generated by Django 2.2.1 on 2019-05-29 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190529_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='hello',
            new_name='title',
        ),
    ]
