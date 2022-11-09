from django.urls import path
from . import views

urlpatterns = [
    path('<id_collaborateur>', views.index, name='home_collab')
]
