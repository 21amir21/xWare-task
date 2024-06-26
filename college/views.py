from django.shortcuts import redirect, render, get_object_or_404
from .models import Faculty, Department, Subjects
from .forms import FacultyForm, SubjectForm, SubjectsForm


def faculty_list(request):
    faculty_listi = Faculty.objects.all()
    context = {
        "faculty_list": faculty_listi,
    }
    return render(request, "faculty.html", context)


def create_or_edit_faculty(request, pk=None):
    if pk:
        faculty = get_object_or_404(Faculty, pk=pk)
    else:
        faculty = Faculty()

    if request.method == "POST":
        faculty_form = FacultyForm(request.POST, instance=faculty)
        if faculty_form.is_valid():
            faculty_form.save()
            return redirect("faculty_list")
    else:
        faculty_form = FacultyForm(instance=faculty)
    return render(request, "create_edit_faculty.html", {"form": faculty_form})


def departments_list(request):
    departments = Department.objects.all()
    return render(request, "departments.html", {"departments": departments})


def create_or_edit_department(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = Department()

    if request.method == "POST":
        department_form = SubjectForm(request.POST, instance=department)
        if department_form.is_valid():
            department_form.save()
            return redirect("departments_list")
    else:
        department_form = SubjectForm(instance=department)
    return render(request, "create_edit_department.html", {"form": department_form})


def subjects_list(request):
    subjects = Subjects.objects.all()
    return render(request, "subjects.html", {"subjects": subjects})


def create_or_edit_subject(request, pk=None):
    if pk:
        subject = get_object_or_404(Subjects, pk=pk)
    else:
        subject = Subjects()

    if request.method == "POST":
        subject_form = SubjectsForm(request.POST, instance=subject)
        if subject_form.is_valid():
            subject_form.save()
            return redirect("subjects_list")
    else:
        subject_form = SubjectsForm(instance=subject)
    return render(request, "create_edit_subject.html", {"form": subject_form})
