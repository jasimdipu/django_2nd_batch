# Generated by Django 3.1.7 on 2021-04-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_remove_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='relation.Tag'),
        ),
    ]
