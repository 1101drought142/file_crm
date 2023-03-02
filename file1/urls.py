from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('xlxs_load/', views.StartLoadPage.as_view(), name='catalog'),
    path('xlxs_load/<slug:model_name>/', views.LoadSettingsPage.as_view(), name='catalog'),
    path('xlxs_load/form/<slug:model_name>/', views.LoadSettingsResult.as_view(), name='catalog'),

]
