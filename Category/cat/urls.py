from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cat_id>',views.getCat,name='cat'),
]