from django.urls import path
from . import views

urlpatterns = [
    path("users", views.get_users, name="index_users"),
    path("add", views.add_users, name="index_add")
]
