from django.urls import path
from . import views

urlpatterns = [
    path("faculty/", views.faculty_list, name="faculty_list"),
    path("faculty/create/", views.create_or_edit_faculty, name="create_faculty"),
    path("faculty/edit/<int:pk>/", views.create_or_edit_faculty, name="edit_faculty"),
]
