# Generated by Django 2.0.5 on 2018-05-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figure', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserImage',
            new_name='Image',
        ),
    ]