from django.contrib import admin
from django.utils.html import format_html

from .models import *

class RecomendationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recomendation._meta.fields]
admin.site.register(Recomendation, RecomendationAdmin)

class ReqvizitiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reqviziti._meta.fields]
admin.site.register(Reqviziti, ReqvizitiAdmin)

class ZadaniaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zadania._meta.fields]
admin.site.register(Zadania, ZadaniaAdmin)

class WeekTableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WeekTable._meta.fields]
admin.site.register(WeekTable, WeekTableAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Clients._meta.fields]
admin.site.register(Clients, ClientsAdmin)

class DohodiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dohodi._meta.fields]
admin.site.register(Dohodi, DohodiAdmin)

class PlacesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Places._meta.fields]
admin.site.register(Places, PlacesAdmin)

class TeachersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teachers._meta.fields]
admin.site.register(Teachers, TeachersAdmin)

class ThemesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Themes._meta.fields]
admin.site.register(Themes, ThemesAdmin)

class Spisok_ReqvizitiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Spisok_Reqviziti._meta.fields]
admin.site.register(Spisok_Reqviziti, Spisok_ReqvizitiAdmin)

class SotrudnikiAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sotrudniki._meta.fields]
admin.site.register(Sotrudniki, SotrudnikiAdmin)

class Zp_PrepodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zp_Prepod._meta.fields]
admin.site.register(Zp_Prepod, Zp_PrepodAdmin)

class SchoolsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Schools._meta.fields]
admin.site.register(Schools, SchoolsAdmin)

class What_have_we_learnedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in What_have_we_learned._meta.fields]
admin.site.register(What_have_we_learned, What_have_we_learnedAdmin)


class Reqviziti_2Admin(admin.ModelAdmin):
    list_display = [field.name for field in Reqviziti_2._meta.fields]
admin.site.register(Reqviziti_2, Reqviziti_2Admin)


class Year_ProgramAdmin(admin.ModelAdmin):
    model = Year_Program
    list_display = [
        "iexact_year", 
        "week_number", 
        "idformat", 
        "task__field", 
        "task__subject",
        "task__subsubject",
        "task__task_name",
        "task_str_id",
        "dz_str_id",
        "task__main_file",
        "raska_online_link",
        "dz__main_file",
        "recom__link",
        "object_count",
        "object_number"
        ]

    @admin.display(description='Раздел', ordering='task__field')
    def task__field(self, obj):
        try:
            return obj.task.field
        except:
            return "-"
    
    @admin.display(description='Тема', ordering='task__subject')
    def task__subject(self, obj):
        try:
            return obj.task.subject
        except:
            return "-"

    @admin.display(description='Подтема', ordering='task__subsubject')
    def task__subsubject(self, obj):
        try:
            return obj.task.subsubject
        except:
            return "-"

    @admin.display(description='Название задания', ordering='task__task_name')
    def task__task_name(self, obj):
        try:
            return obj.task.task_name
        except:
            return "-"

    @admin.display(description='Гл файл', ordering='task__main_file')
    def task__main_file(self, obj):
        try:
            if (obj.task.pdf_file):
                return format_html(f"<a href='{obj.task.pdf_file}'>Ссылка</a>") #bj.task.pdf_file
            else:
                raise ValueError()
        except:
            return "-"
    
    @admin.display(description='Дз', ordering='dz__main_file')
    def dz__main_file(self, obj):
        try:
            if (obj.dz.pdf_file != ""):
                return format_html(f"<a href='{obj.dz.pdf_file}'>Ссылка</a>")
            else:
                raise ValueError()
        except:
            return "-"

    @admin.display(description='Реком', ordering='recom__link')
    def recom__link(self, obj):
        try:
            if (obj.recom.link != ""):
                return format_html(f"<a href='{obj.recom.link}'>Ссылка</a>")
            else:
                raise ValueError()
        except:
            return "-"
            
    @admin.display(description='Рас-ка онлайн', ordering='raska_online_link')
    def raska_online_link(self, obj):
        try:
            if (obj.raska_online != ""):
                return format_html(f"<a href='{obj.raska_online}'>Ссылка</a>")
            raise ValueError()
        except:
            return "-"

    @admin.display(description='Кол-во', ordering='object_count')
    def object_count(self, obj):
        count = self.model.objects.filter(
            iexact_year=obj.iexact_year, 
            idformat = obj.idformat, 
            task_str_id = obj.task_str_id
        ).count()
        return str(count)

    @admin.display(description='Номер', ordering='object_number')
    def object_number(self, obj):
        object_list = self.model.objects.filter(
            iexact_year=obj.iexact_year, 
            idformat = obj.idformat, 
            task_str_id = obj.task_str_id
        )
        for i, o in enumerate(object_list):
            if o == obj:
                return str(i + 1)

    def get_queryset(self, request):
        return super(Year_ProgramAdmin, self).get_queryset(request).select_related(
            'task', 'dz', "recom")        
admin.site.register(Year_Program, Year_ProgramAdmin)

class RaspisanieAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Raspisanie._meta.fields]
    list_display.extend(["group_id"])
admin.site.register(Raspisanie, RaspisanieAdmin)

admin.site.register(Groups)

class OtrabotkaAdmin(admin.ModelAdmin):
    list_per_page = 900
admin.site.register(Otrabotka, OtrabotkaAdmin)


admin.site.register(Gifts)