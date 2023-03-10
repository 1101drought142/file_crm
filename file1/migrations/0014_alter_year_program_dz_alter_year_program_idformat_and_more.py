# Generated by Django 4.1.3 on 2023-02-23 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0013_year_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year_program',
            name='dz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dz', to='file1.zadania'),
        ),
        migrations.AlterField(
            model_name='year_program',
            name='idformat',
            field=models.CharField(choices=[('oчно', 'oчно'), ('oнлайн', 'oнлайн')], max_length=64, verbose_name='Формат факт'),
        ),
        migrations.AlterField(
            model_name='year_program',
            name='iexact_year',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6'), ('1 класс', '1 класс'), ('2 класс', '2 класс'), ('3 класс', '3 класс'), ('4 класс', '4 класс')], max_length=64, verbose_name='Пр.Возраст'),
        ),
        migrations.AlterField(
            model_name='year_program',
            name='recom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recom', to='file1.recomendation'),
        ),
        migrations.AlterField(
            model_name='year_program',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='file1.zadania'),
        ),
    ]
