# Generated by Django 4.1.3 on 2023-03-02 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0021_alter_otrabotka_options_otrabotka_message_group_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateField()),
                ('gifts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.reqviziti')),
                ('sotr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.sotrudniki')),
            ],
        ),
    ]
