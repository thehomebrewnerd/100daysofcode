# Generated by Django 2.0 on 2018-01-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='progress',
        ),
        migrations.AddField(
            model_name='post',
            name='thoughts',
            field=models.TextField(default='default text'),
            preserve_default=False,
        ),
    ]