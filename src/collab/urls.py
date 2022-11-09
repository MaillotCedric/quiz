from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz', views.quiz, name='index'),
    path('test', views.test, name='test'),
    path('testquiz', views.testquiz, name='testquiz')
]