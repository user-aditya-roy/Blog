# Generated by Django 2.0.5 on 2018-05-31 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blogposts'},
        ),
    ]