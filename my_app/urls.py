from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
