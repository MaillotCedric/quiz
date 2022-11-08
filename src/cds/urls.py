from django.urls import path
from . import views

urlpatterns = [
    path('<id_chef>', views.index, name='index_home_cds'),
    path('test', views.importQuiz, name='importation'),
]