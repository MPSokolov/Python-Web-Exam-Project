# Generated by Django 4.2.4 on 2023-08-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_categorymodel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
