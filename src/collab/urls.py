from django.urls import path
from . import views

urlpatterns = [
    path('<id_collaborateur>', views.index, name='home_collab'),
    path('<id_collaborateur>/quiz', views.quiz, name='index'),
    path('test', views.test, name='test'),
    path('<id_collaborateur>/testquiz', views.testquiz, name='testquiz'),
    path('<id_collaborateur>/resultatquiz', views.resultatquiz, name='resultatquiz')
]
