# Generated by Django 4.1.3 on 2023-02-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0008_alter_dohodi_classes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='address',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='places',
            name='contact',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Контакт'),
        ),
    ]
