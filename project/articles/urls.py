from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("detail/<int:pk>", views.HomeDetailView.as_view(), name="detail_page"),
    path("edit-page" , views.edit_page , name="edit_page")
]
