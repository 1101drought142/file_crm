from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Recomendation(models.Model):
    task_id = models.CharField(max_length=128, verbose_name="ID задания")
    recom_text = models.TextField(verbose_name="Текст рекомендации")
    link=models.CharField(max_length=512, verbose_name="Ссылка")
    
    def __str__(self):
        return self.task_id
    
    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"


class Reqviziti(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    couunt = models.IntegerField(verbose_name="шт")
    couunt_komp = models.IntegerField(verbose_name="шт для комп")
    class Meta:
        verbose_name = "Рекзвизит"
        verbose_name_plural = "Резквизиты"

    def __str__(self):
        return self.name

class Zadania(models.Model):
    field = models.CharField(max_length=128, verbose_name="Раздел")
    subject = models.CharField(max_length=128, verbose_name="Тема")
    subsubject = models.CharField(max_length=128, verbose_name="Подтема")
    typ = models.CharField(max_length=128, verbose_name="Тип")
    task_name = models.CharField(max_length=128, verbose_name="Название задания",blank=True, null=True, default="")
    description = models.TextField(verbose_name="Описание задания",blank=True, null=True, default="")
    number = models.IntegerField(verbose_name="Номер")
    task_id = models.CharField(verbose_name="ID задания", max_length=128)
    main_file = models.CharField(max_length=512, verbose_name="Главный файл", blank=True, null=True, default="")
    pdf_file = models.CharField(max_length=512, verbose_name="PDF файл", blank=True, null=True, default="")
    reqs_text = models.CharField(max_length=512, verbose_name="Реквизиты текст",blank=True, null=True, default="" )
    reqs = models.ManyToManyField(Reqviziti, verbose_name="Реквизиты")
    def __str__(self):
        return self.task_name
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

class WeekTable(models.Model):
    date = models.DateField(verbose_name="Главный файл")
    week_day = models.CharField(max_length=128, verbose_name="День недели")
    status = models.CharField(max_length=128, verbose_name="Статус",blank=True, null=True, default="")
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name = "График недель"
        verbose_name_plural = "График недель"

class Clients(models.Model):
    special_id = models.CharField(max_length=64, verbose_name="Дополнительное ID", unique=True)
    name = models.CharField(max_length=128, verbose_name="ФИО родителя",blank=True, null=True, default="")
    phone = models.CharField(max_length=256, verbose_name="Номер телефона",blank=True, null=True, default="")
    child_name = models.CharField(max_length=128, verbose_name="ФИО ребенка",blank=True, null=True, default="")
    birthday = models.DateField(verbose_name="День рождения", blank=True, null=True, default=now)
    discount = models.FloatField(verbose_name="Скидка", blank=True, null=True, default=0)
    home_address = models.CharField(max_length=512, verbose_name="Адрес", blank=True, null=True)
    def __str__(self):
        return self.child_name
    class Meta:
        verbose_name = "Карточка клиента"
        verbose_name_plural = "Карточки клиентов"

class Dohodi(models.Model):
    date = models.DateField(verbose_name="Дата")
    summ = models.IntegerField(verbose_name="Сумма")
    full_name = models.CharField(max_length=128, verbose_name="Полное имя")
    classes_count = models.IntegerField(verbose_name="Количество занятий", blank=True, null=True, default=0)
    month = models.CharField(max_length=128, verbose_name="Месяц")
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="ID клиента")
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доходы"

class Schools(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название школы")
    school_id = models.CharField(max_length=64, verbose_name="ID школы", unique=True)
    okpo = models.CharField(max_length=64, verbose_name="ОКПО", blank=True, null=True, default="")
    headmaster = models.CharField(max_length=128, verbose_name="Директор", blank=True, null=True, default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

class Places(models.Model):
    name = models.CharField(max_length=512, verbose_name="Название")
    address = models.CharField(max_length=512, verbose_name="Адрес", blank=True, null=True, default="")
    contact = models.CharField(max_length=256, verbose_name="Контакт", blank=True, null=True, default="")
    place_id = models.CharField(max_length=128, verbose_name="ID подразделения", unique=True)
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name="ID школы")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Подразделение школы"
        verbose_name_plural = "Подразделения школ"

class Teachers(models.Model):
    teacher_id = models.CharField(max_length=128, verbose_name="ID педагога")
    phone = models.CharField(max_length=64, verbose_name="Номер телефона")
    date = models.DateField(verbose_name="День рождения")
    name = models.CharField(max_length=128, verbose_name="ФИО полностью")
    name_min = models.CharField(max_length=64, verbose_name="ФИО сокращенно")
    email=models.CharField(max_length=64, verbose_name="Почта", blank=True, null=True, default="")
    subs = models.CharField(max_length=256, verbose_name="Подписи", blank=True, null=True, default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Педагог"
        verbose_name_plural = "Педагоги"

class Themes(models.Model):
    cat_main = models.CharField(max_length=128, verbose_name="Раздел")
    id_cat_main = models.CharField(max_length=128, verbose_name="ID главной категории")
    sub_cat = models.CharField(max_length=128, verbose_name="Тема")
    id_sub_cat = models.CharField(max_length=128, verbose_name="ID темы")
    sub_sub_cat = models.CharField(max_length=128, verbose_name="ПодТема")
    id_sub_sub_cat = models.CharField(max_length=128, verbose_name="ID ПодТемы")
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
    def __str__(self):
        return self.sub_sub_cat

class Spisok_Reqviziti(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    reqs_id = models.CharField(max_length=128, verbose_name="ID реквзита", unique=True)
    class Meta:
        verbose_name = "Список Реквзит"
        verbose_name_plural = "Список реквизитов"
    def __str__(self):
        return self.name

class Sotrudniki(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    sotrud_id = models.CharField(max_length=128, verbose_name="ID сотрудника", unique=True)
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
    def __str__(self):
        return self.name
    

class Zp_Prepod(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    zp_ochno = models.IntegerField(verbose_name="ЗП очно")
    zp_ochno_min = models.IntegerField(verbose_name="ЗП очно мин")
    zp_online_sad = models.IntegerField(verbose_name="ЗП онлайн сад")
    zp_online_school = models.IntegerField(verbose_name="ЗП онлайн школа")
    zp_podrabotka_hour = models.IntegerField(verbose_name="ЗП подработка час")
    zp_online_min = models.IntegerField(verbose_name="ЗП онлайн мин")
    zp_ind_min = models.IntegerField(verbose_name="ЗП индивидуальное мин")
    class Meta:
        verbose_name = "Зп преподователю"
        verbose_name_plural = "Зп преподавателям"
    def __str__(self):
        return self.teacher.name


class What_have_we_learned(models.Model):
    task_id = models.CharField(max_length=64, verbose_name="ID задания")
    text = models.TextField(verbose_name="Текст")
    class Meta:
        verbose_name = "Чему мы научились"
        verbose_name_plural = "Чему мы научились"
    def __str__(self):
        return self.text


class Reqviziti_2(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    reqs_2_id = models.CharField(max_length=64, verbose_name="ID реквизита")
    present = models.BooleanField(verbose_name="Является подарком?", blank=True, null=True, default=False)
    start_count = models.IntegerField(verbose_name="Стоимость в звездах", blank=True, null=True, default=0)
    reqvizit_count_present = models.IntegerField(verbose_name="Кол-во реквизита для подарка", blank=True, null=True, default=0)
    active = models.BooleanField(verbose_name="Активный?", blank=True, null=True, default=False)
    class Meta:
        verbose_name = "Реквизит 2"
        verbose_name_plural = "Реквизиты 2"
    def __str__(self):
        return self.name
"""
class Protiv_Publicaii
"""


class Year_Program(models.Model):
    CHOICES = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('1 класс', '1 класс'),
        ('2 класс', '2 класс'),
        ('3 класс', '3 класс'),
        ('4 класс', '4 класс'),
        ('5 класс', '5 класс'),
    )
    CHOICES_FORMAT = (
        ("очно", "oчно"),
        ("онлайн", "oнлайн"),
    )
    iexact_year = models.CharField("Пр.Возраст", max_length=64, choices = CHOICES)
    week_number = models.CharField("№ неделм план", max_length=64)
    idformat = models.CharField("Формат факт", max_length=64, choices = CHOICES_FORMAT)
    task_str_id = models.CharField("ID задания", max_length=64, blank=True, null=True, default="")
    dz_str_id = models.CharField("ID дз", max_length=64, blank=True, null=True, default="")
    raska_online = models.CharField("Рас-ка онлайн", max_length=128, blank=True, null=True, default="")
    task = models.ForeignKey(Zadania, on_delete=models.CASCADE, blank=True, null=True, related_name='task')
    dz = models.ForeignKey(Zadania, on_delete=models.CASCADE, blank=True, null=True, related_name='dz')
    recom = models.ForeignKey(Recomendation, on_delete=models.CASCADE, blank=True, null=True, related_name='recom')

    class Meta:
        verbose_name = "Программа на год"
        verbose_name_plural = "Программа на год"

    def __str__(self):
        return self.iexact_year + self.week_number + self.idformat


class Raspisanie(models.Model):
    CHOICES = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        (3.0, '3'),
        (4.0, '4'),
        (5.0, '5'),
        (6.0, '6'),
        ('1 класс', '1 класс'),
        ('2 класс', '2 класс'),
        ('3 класс', '3 класс'),
        ('4 класс', '4 класс'),
        ('5 класс', '5 класс'),
    )
    CHOICES_FORMAT = (
        ("очно", "oчно"),
        ("онлайн", "oнлайн"),
    )
    CHOICES_WEEK_DAY = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
    )
    CHOICES_GROUP_TYPE = (
        ("школа", "школа"),
        ("сад", "сад"),
        ("инд", "инд"),
    )
    CHOICES_WHERE_TO_PAY = (
        ("школа", "школа"),
        ("декарт", "декарт"),
    )
    f = models.CharField("ф", max_length=128) #A
    week_day = models.CharField("День недели", max_length=128, choices = CHOICES_WEEK_DAY) #B
    time = models.CharField("Время", max_length=64) #D
    format_plan = models.CharField("Формат план", max_length=32, choices=CHOICES_FORMAT) #E
    program_year = models.CharField("Программный возраст", max_length=64, choices=CHOICES) #H
    place = models.ForeignKey(Places, verbose_name="Место", on_delete=models.CASCADE, blank=True, null=True) #X
    pedagog_table = models.ForeignKey(Teachers, verbose_name="Педагоги", on_delete=models.CASCADE, related_name='pedagog_table', blank=True, null=True) #AF
    kabinet = models.CharField("Кабинет для занятий",max_length=128) #L
    pedagog_fact = models.ForeignKey(Teachers, verbose_name="Педагоги", on_delete=models.CASCADE, related_name='pedagog_fact', blank=True, null=True) #AG
    gruop_type = models.CharField("Тип группы", max_length=256,choices=CHOICES_GROUP_TYPE) #N
    zoom_link = models.CharField("Ссылка зум", max_length=512, blank=True, null=True, default="") #O
    id_zoom = models.CharField("ID zoom", max_length=512, blank=True, null=True, default="") #P
    pass_zoom = models.CharField("Zoom pass", max_length=512, blank=True, null=True, default="") #Q
    journal = models.CharField("Журнал", max_length=512, blank=True, null=True, default="") #R
    start_date = models.DateField("Дата начала занятий", blank=True, null=True) #S
    start_program = models.IntegerField("Начало программы", default=1,
        validators=[MaxValueValidator(60), MinValueValidator(1)]) #U
    fict_group = models.BooleanField("Фиктивные группы") #V
    end_date = models.DateField("Дата окончания программы",  blank=True, null=True) #W
    otchisl = models.IntegerField("Отчисление от школы %", default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]) #Y
    where_pay = models.CharField("Куда оплата", max_length=128, choices=CHOICES_WHERE_TO_PAY) #Z
    tax = models.IntegerField("Налог", default=17, validators=[MaxValueValidator(100), MinValueValidator(1)]) #AA
    payment_per_class = models.IntegerField("Стоимость за занятие", default=0, validators=[MaxValueValidator(100), MinValueValidator(1)]) #AB
    payment_per_month = models.IntegerField("Стоимость за месяц", default=0, validators=[MaxValueValidator(100), MinValueValidator(1)]) #AC
    extra_payment = models.IntegerField("Дополнительные выплаты (Самозянатые)", default=0, validators=[MaxValueValidator(100), MinValueValidator(1)]) #AD
    mos_link = models.CharField("Ссылка на mos", default="", blank=True, null=True, max_length=512) #AE
    dop_otchisl_dekart = models.IntegerField("Доп отчисление от школы В декарт", default=0,
        validators=[MaxValueValidator(100), MinValueValidator(1)]) #AH
    @property
    def group_id(self):
        return "gr" + str(self.pk)
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
    def __str__(self):
        return self.f


class Groups(models.Model):
    CHOICES_WHERE_TO = (
        ("сам->сам", "сам->сам"), 
        ("род->сам", "род->сам"),
        ("род->род", "род->род"),
        ("прод->род", "прод->род"),
        ("прод->прод", "прод->прод"),
        ("сам->род" , "сам->род"),
    )
    CHOICES_WHERE_TO_PAY = (
        ("школа", "школа"),
        ("декарт", "декарт"),
        ("Декарт", "Декарт"),
    )
    where_to = models.CharField("откуда/куда", max_length=128, blank=True, null=True, default="", choices=CHOICES_WHERE_TO)
    zachislenie = models.DateField("Зачисление", blank=True, null=True)
    otchisl_table = models.DateField("Отчисление табель", blank=True, null=True)
    otchisl_journal = models.DateField("Отчисление журнал", blank=True, null=True)
    comments = models.CharField("Коментарий", blank=True, null=True, default="", max_length=256)
    id_group_fact = models.ForeignKey(Raspisanie, verbose_name="Группа факт", blank=True, null=True, related_name='id_group_fact', on_delete=models.CASCADE)
    where_to_pay = models.CharField(verbose_name="Куда платить", blank=True, null=True, choices=CHOICES_WHERE_TO_PAY, max_length=256)
    client_id = models.ForeignKey(Clients, verbose_name="Клиент", on_delete=models.CASCADE)
    schet_num = models.CharField("Номер счета", max_length=256)
    id_group_table = models.ForeignKey(Raspisanie, verbose_name="Группа табель", blank=True, null=True, related_name="id_group_table", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
    
class Otrabotka(models.Model):
    fio = models.CharField("ФИО ребенка",max_length=512)
    progul = models.DateField("Прогул", blank=True, null=True,)
    otrabotka = models.DateField("Отработка", blank=True, null=True)
    group_name_progul = models.CharField("Название группы (Прогул)", max_length=512, blank=True, null=True, default="")
    group_name_otrabotka = models.CharField("Название группы (Прогул)", max_length=512, blank=True, null=True, default="")
    status = models.CharField("Статус", max_length=256, blank=True, null=True, default="")
    message_for_pedagog_otr = models.CharField("Сообщ для педагога в группе отработка", max_length=512, blank=True, null=True, default="")
    message_date = models.DateField("Дата сообщения в обычную группу", blank=True, null=True)
    message_group_name = models.CharField("Название группы (сообщение)", blank=True, null=True, max_length=512)
    message_for_pedagog_obich = models.CharField("Сообщ для педагога в обычной группе", max_length=512, blank=True, null=True, default="")
    user_id = models.ForeignKey(Groups, verbose_name="ID ученика", blank=True, null=True, on_delete=models.SET_NULL)
    group_id = models.ForeignKey(Raspisanie, verbose_name="Id группы", blank=True, null=True,  on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Отработка"
        verbose_name_plural = "Отработка"

class Gifts(models.Model):
    sotr = models.ForeignKey(Sotrudniki, on_delete=models.CASCADE)
    gifts = models.ForeignKey(Reqviziti_2, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField()

class DeliveryAdmin(models.Model):
    create_date = models.DateField()
    child_name = models.CharField(max_length=256)
    gift = models.ForeignKey(Reqviziti_2, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

class Sklad(models.Model):
    name = models.DateField()
    count = models.IntegerField()
    rek_id = models.ForeignKey(Reqviziti_2, on_delete=SET_NULL, blank=True, null=True)
