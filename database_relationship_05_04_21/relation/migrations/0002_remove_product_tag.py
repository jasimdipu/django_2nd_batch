# Generated by Django 3.1.7 on 2021-04-05 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
    ]
