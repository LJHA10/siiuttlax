from django.urls import path
from . import views


app_name = "period"
urlpatterns = [
    path('', views.period, name='period')
]