from django.urls import path
from . import views

urlpatterns = [
    path("users", views.get_users, name="index_users"),
    path("add", views.add_users, name="index_add"),
    path("delete", views.delete_user, name="index_delete"),
    path("secteurs", views.get_secteurs, name="index_secteurs")
]
