# Generated by Django 4.2 on 2023-05-09 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_happys_remove_home_owner_en_remove_home_owner_ru'),
    ]

    operations = [
        migrations.RenameField(
            model_name='happys',
            old_name='pircture',
            new_name='picture',
        ),
    ]
