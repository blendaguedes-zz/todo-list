from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add_todo/', views.add_todo, name='add_todo'),
  path('mark_done/<int:todo_id>', views.mark_done, name='mark_done'),
  path('delete/<int:todo_id>', views.delete, name='delete'),

]
