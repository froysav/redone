# Generated by Django 4.2 on 2023-04-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='name_home',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='home',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='home',
            name='place',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='taking_time',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
