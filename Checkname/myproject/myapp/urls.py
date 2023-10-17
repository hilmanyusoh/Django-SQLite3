from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about',views.about),
    path('form', views.form),
    path('edit/<checkname_id>',views.edit),
    path('delete/<checkname_id>',views.delete)
   
]