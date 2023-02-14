from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.Delete, name='delete'),
]
