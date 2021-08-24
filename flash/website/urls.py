from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reset_points', views.reset, name="reset"),
    path('add', views.add, name="add"),
    path('subtract', views.subtract, name="subtract"),
    path('multiply', views.multiply, name="multiply"),
    path('divide', views.divide, name="divide"),
]
