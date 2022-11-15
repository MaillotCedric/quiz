from django.urls import path
from . import views

urlpatterns = [
    path('<id_chef>', views.index, name='index_home_cds'),
    path('<id_chef>/test', views.importQuiz, name='importation'),
    path('<id_chef>/activation', views.activation, name='activation'),
    path('<id_chef>/desactivation', views.desactivation, name='desactivation'),
    path('quiz', views.quiz, name='quiz'),
    path('<id_chef>/testImportAuto', views.testImportAuto, name="testImportAuto")
]