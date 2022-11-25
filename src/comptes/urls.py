from django.urls import path
from . import views

urlpatterns = [
    path('new_bdd', views.index, name='index'),
    path('remove_last', views.remove, name='remove_last'),
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout')
    # path('script', views.index, name='script')
]
