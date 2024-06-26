from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

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
    path("courses/", views.courses_list, name="courses_list"),
    path("courses/create/", views.create_or_edit_course, name="create_course"),
    path("courses/edit/<int:pk>", views.create_or_edit_course, name="edit_course"),
    path("exams/", views.exams_list, name="exams_list"),
    path("exams/create/", views.create_or_edit_exam, name="create_exam"),
    path("exams/edit/<int:pk>", views.create_or_edit_exam, name="edit_exam"),
    path("students/", views.students_list, name="students_list"),
    path("students/create/", views.create_or_edit_student, name="create_student"),
    path("students/edit/<int:pk>", views.create_or_edit_student, name="edit_student"),
    path("professors/", views.professors_list, name="professors_list"),
    path("professors/create/", views.create_or_edit_professor, name="create_professor"),
    path(
        "professors/edit/<int:pk>",
        views.create_or_edit_professor,
        name="edit_professor",
    ),
    path("departments/<int:department_id>", views.department_view),
    path("subjects/<int:subject_id>", views.subject_view),
    path("courses/<int:course_id>", views.course_view),
    path("students/<int:student_id>", views.student_view),
    path("professors/<int:professor_id>", views.professor_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
