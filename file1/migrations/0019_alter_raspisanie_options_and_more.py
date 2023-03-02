# Generated by Django 4.1.3 on 2023-02-26 09:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0018_alter_raspisanie_payment_per_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raspisanie',
            options={'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписание'},
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='dop_otchisl_dekart',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Доп отчисление от школы В декарт'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='payment_per_class',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Стоимость за занятие'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='payment_per_month',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Стоимость за месяц'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='pedagog_fact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedagog_fact', to='file1.teachers', verbose_name='Педагоги'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='pedagog_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedagog_table', to='file1.teachers', verbose_name='Педагоги'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='file1.places', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='raspisanie',
            name='program_year',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), (3.0, '3'), (4.0, '4'), (5.0, '5'), (6.0, '6'), ('1 класс', '1 класс'), ('2 класс', '2 класс'), ('3 класс', '3 класс'), ('4 класс', '4 класс'), ('5 класс', '5 класс')], max_length=64, verbose_name='Программный возраст'),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where_to', models.CharField(blank=True, choices=[('сам->сам', 'сам->сам'), ('род->сам', 'род->сам'), ('род->род', 'род->род'), ('прод->род', 'прод->род'), ('прод->прод', 'прод->прод'), ('сам->род', 'сам->род')], default='', max_length=128, null=True, verbose_name='откуда/куда')),
                ('zachislenie', models.DateField(blank=True, null=True, verbose_name='Зачисление')),
                ('otchisl_table', models.DateField(blank=True, null=True, verbose_name='Отчисление табель')),
                ('otchisl_journal', models.DateField(blank=True, null=True, verbose_name='Отчисление журнал')),
                ('comments', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Коментарий')),
                ('where_to_pay', models.CharField(blank=True, choices=[('школа', 'школа'), ('декарт', 'декарт'), ('Декарт', 'Декарт')], max_length=256, null=True, verbose_name='Куда платить')),
                ('schet_num', models.CharField(max_length=256, verbose_name='Номер счета')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.clients', verbose_name='Клиент')),
                ('id_group_fact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_group_fact', to='file1.raspisanie', verbose_name='Группа факт')),
                ('id_group_table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_group_table', to='file1.raspisanie', verbose_name='Группа табель')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]