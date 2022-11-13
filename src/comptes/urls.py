from django.urls import path
from . import views

urlpatterns = [
    path('new_bdd', views.index, name='index'),
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout')
]
