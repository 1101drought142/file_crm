from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import Http404
from django.apps import apps
from .logic import xlxs_loader, xlxs_loader_year_program, xlxs_loader_raspisanie, xlxs_loader_groups
models = {
    model.__name__: model for model in apps.get_app_config("file1").get_models()
}
class StartLoadPage(TemplateView):
    template_name = "xlsx_load_start.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StartLoadPage, self).get_context_data(*args, **kwargs)
        context["models"] = { model.__name__: model._meta.verbose_name.title() for model in apps.get_app_config("file1").get_models() }
        return context
        
class LoadSettingsPage(TemplateView):
    template_name = "xlxs_load.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LoadSettingsPage, self).get_context_data(*args, **kwargs)
        if (models.get(kwargs["model_name"])):
            cur_model = models.get(kwargs["model_name"])
            
            context["model_title"] = cur_model._meta.verbose_name.title()
            context["fields"] = cur_model._meta.fields[1::] 
            #context["fields_many_to_many"] = cur_model._meta.many_to_many
            context["slug"] = kwargs["model_name"]
            return context
        else:
            raise Http404

class LoadSettingsResult(View):

    def post(self, request, *args, **kwargs):
        cur_model = models.get(kwargs["model_name"])
        xlsx_file = request.FILES['table']
        if (cur_model.__name__ == "Year_Program"):
            objects = xlxs_loader_year_program(xlsx_file)
        elif (cur_model.__name__ == "Raspisanie"):
            objects = xlxs_loader_raspisanie(xlsx_file)
        elif (cur_model.__name__ == "Groups"):
            objects = xlxs_loader_groups(xlsx_file)        
        else:
            objects = xlxs_loader(cur_model, xlsx_file)
        return render(request, "xlxs_load_result.html",
            {
                "objects" : objects,
                "fields" : cur_model._meta.fields,
                "model_name" : kwargs["model_name"].lower(),
                "model_title" : cur_model._meta.verbose_name.title()
            }
        )


class HomePage(TemplateView):
    template_name = "xlsx_load_start.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["models"] = { model.__name__: model._meta.verbose_name.title() for model in apps.get_app_config("file1").get_models() }
        return context


