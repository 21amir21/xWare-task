from django.urls import path
from . import views

urlpatterns = [
    path("faculty/", views.faculty_list, name="faculty_list"),
    path("faculty/create/", views.create_or_edit_faculty, name="create_faculty"),
    path("faculty/edit/<int:pk>/", views.create_or_edit_faculty, name="edit_faculty"),
    path("departments/", views.departments_list, name="departments_list"),
    path(
        "departments/create/", views.create_or_edit_department, name="create_department"
    ),
    path(
        "departments/edit/<int:pk>/",
        views.create_or_edit_department,
        name="edit_department",
    ),
    path("subjects/", views.subjects_list, name="subjects_list"),
    path("subjects/create/", views.create_or_edit_subject, name="create_subject"),
    path("subjects/edit/<int:pk>", views.create_or_edit_subject, name="edit_subject"),
]
