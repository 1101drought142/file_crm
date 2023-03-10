# Generated by Django 4.1.3 on 2023-02-09 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название школы')),
                ('school_id', models.CharField(max_length=64, unique=True, verbose_name='ID школы')),
                ('okpo', models.CharField(max_length=64, verbose_name='ОКПО')),
                ('headmaster', models.CharField(max_length=128, verbose_name='Директор')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.DeleteModel(
            name='Shools',
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Карточка клиента', 'verbose_name_plural': 'Карточки клиентов'},
        ),
        migrations.AlterModelOptions(
            name='dohodi',
            options={'verbose_name': 'Карточка клиента', 'verbose_name_plural': 'Карточки клиентов'},
        ),
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name': 'Подразделение школы', 'verbose_name_plural': 'Подразделения школ'},
        ),
        migrations.AlterModelOptions(
            name='recomendation',
            options={'verbose_name': 'Рекомендация', 'verbose_name_plural': 'Рекомендации'},
        ),
        migrations.AlterModelOptions(
            name='reqviziti',
            options={'verbose_name': 'Рекзвизит', 'verbose_name_plural': 'Резквизиты'},
        ),
        migrations.AlterModelOptions(
            name='reqviziti_2',
            options={'verbose_name': 'Реквизит 2', 'verbose_name_plural': 'Реквизиты 2'},
        ),
        migrations.AlterModelOptions(
            name='sotrudniki',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='spisok_reqviziti',
            options={'verbose_name': 'Реквзит', 'verbose_name_plural': 'Список реквизитов'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name': 'Педагог', 'verbose_name_plural': 'Педагоги'},
        ),
        migrations.AlterModelOptions(
            name='themes',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterModelOptions(
            name='weektable',
            options={'verbose_name': 'График недель', 'verbose_name_plural': 'График недель'},
        ),
        migrations.AlterModelOptions(
            name='what_have_we_learned',
            options={'verbose_name': 'Чему мы научились', 'verbose_name_plural': 'Чему мы научились'},
        ),
        migrations.AlterModelOptions(
            name='zadania',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterModelOptions(
            name='zp_prepod',
            options={'verbose_name': 'Зп преподователю', 'verbose_name_plural': 'Зп преподавателям'},
        ),
        migrations.RemoveField(
            model_name='places',
            name='school_name',
        ),
        migrations.AddField(
            model_name='clients',
            name='child_name',
            field=models.CharField(default='', max_length=128, verbose_name='ФИО ребенка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='discount',
            field=models.FloatField(verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='home_address',
            field=models.CharField(max_length=512, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='name',
            field=models.CharField(max_length=128, verbose_name='ФИО родителя'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='special_id',
            field=models.CharField(max_length=64, unique=True, verbose_name='Дополнительное ID'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='classes_count',
            field=models.IntegerField(verbose_name='Количество занятий'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.clients', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='full_name',
            field=models.CharField(max_length=128, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='month',
            field=models.CharField(max_length=128, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='dohodi',
            name='summ',
            field=models.IntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='places',
            name='address',
            field=models.CharField(max_length=512, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='places',
            name='contact',
            field=models.CharField(max_length=256, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='places',
            name='place_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='ID подразделения'),
        ),
        migrations.AlterField(
            model_name='recomendation',
            name='link',
            field=models.CharField(max_length=512, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='recomendation',
            name='recom_text',
            field=models.TextField(verbose_name='Текст рекомендации'),
        ),
        migrations.AlterField(
            model_name='recomendation',
            name='task_id',
            field=models.CharField(max_length=128, verbose_name='ID задания'),
        ),
        migrations.AlterField(
            model_name='reqviziti',
            name='couunt',
            field=models.IntegerField(verbose_name='шт'),
        ),
        migrations.AlterField(
            model_name='reqviziti',
            name='couunt_komp',
            field=models.IntegerField(verbose_name='шт для комп'),
        ),
        migrations.AlterField(
            model_name='reqviziti',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='active',
            field=models.BooleanField(verbose_name='Активный?'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='present',
            field=models.BooleanField(verbose_name='Является подарком?'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='reqs_2_id',
            field=models.CharField(max_length=64, verbose_name='ID реквизита'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='reqvizit_count_present',
            field=models.IntegerField(verbose_name='Кол-во реквизита для подарка'),
        ),
        migrations.AlterField(
            model_name='reqviziti_2',
            name='start_count',
            field=models.IntegerField(verbose_name='Стоимость в звездах'),
        ),
        migrations.AlterField(
            model_name='sotrudniki',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sotrudniki',
            name='sotrud_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='ID сотрудника'),
        ),
        migrations.AlterField(
            model_name='spisok_reqviziti',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='spisok_reqviziti',
            name='reqs_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='ID реквзита'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='date',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='email',
            field=models.CharField(max_length=64, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(max_length=128, verbose_name='ФИО полностью'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name_min',
            field=models.CharField(max_length=64, verbose_name='ФИО сокращенно'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='phone',
            field=models.CharField(max_length=64, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='subs',
            field=models.CharField(max_length=256, verbose_name='Подписи'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='teacher_id',
            field=models.CharField(max_length=128, verbose_name='ID педагога'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='cat_main',
            field=models.CharField(max_length=128, verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='id_cat_main',
            field=models.CharField(max_length=128, verbose_name='ID главной категории'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='id_sub_cat',
            field=models.CharField(max_length=128, verbose_name='ID темы'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='id_sub_sub_cat',
            field=models.CharField(max_length=128, verbose_name='ID ПодТемы'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='sub_cat',
            field=models.CharField(max_length=128, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='themes',
            name='sub_sub_cat',
            field=models.CharField(max_length=128, verbose_name='ПодТема'),
        ),
        migrations.AlterField(
            model_name='weektable',
            name='date',
            field=models.DateField(verbose_name='Главный файл'),
        ),
        migrations.AlterField(
            model_name='weektable',
            name='status',
            field=models.CharField(max_length=128, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='weektable',
            name='week_day',
            field=models.CharField(max_length=128, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='what_have_we_learned',
            name='task_id',
            field=models.CharField(max_length=64, verbose_name='ID задания'),
        ),
        migrations.AlterField(
            model_name='what_have_we_learned',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='description',
            field=models.TextField(verbose_name='Описание задания'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='field',
            field=models.CharField(max_length=128, verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='main_file',
            field=models.CharField(max_length=512, verbose_name='Главный файл'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='number',
            field=models.IntegerField(verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='pdf_file',
            field=models.CharField(max_length=512, verbose_name='PDF файл'),
        ),
        migrations.RemoveField(
            model_name='zadania',
            name='reqs',
        ),
        migrations.AlterField(
            model_name='zadania',
            name='subject',
            field=models.CharField(max_length=128, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='subsubject',
            field=models.CharField(max_length=128, verbose_name='Подтема'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='task_id',
            field=models.IntegerField(verbose_name='ID задания'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='task_name',
            field=models.CharField(max_length=128, verbose_name='Название задания'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='typ',
            field=models.CharField(max_length=128, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_ind_min',
            field=models.IntegerField(verbose_name='ЗП индивидуальное мин'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_ochno',
            field=models.IntegerField(verbose_name='ЗП очно'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_ochno_min',
            field=models.IntegerField(verbose_name='ЗП очно мин'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_online_min',
            field=models.IntegerField(verbose_name='ЗП онлайн мин'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_online_sad',
            field=models.IntegerField(verbose_name='ЗП онлайн сад'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_online_school',
            field=models.IntegerField(verbose_name='ЗП онлайн школа'),
        ),
        migrations.AlterField(
            model_name='zp_prepod',
            name='zp_podrabotka_hour',
            field=models.IntegerField(verbose_name='ЗП подработка час'),
        ),
        migrations.AlterField(
            model_name='places',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.schools', verbose_name='ID школы'),
        ),
        migrations.AddField(
            model_name='zadania',
            name='reqs',
            field=models.ManyToManyField(to='file1.reqviziti', verbose_name='Раздел'),
        ),
    ]
