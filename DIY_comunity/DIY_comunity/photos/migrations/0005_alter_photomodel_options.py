# Generated by Django 4.2.4 on 2023-08-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photomodel_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photomodel',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]