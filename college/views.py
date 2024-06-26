from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Faculty, Department, Professor, Student, Subjects, Exams
from .forms import (
    FacultyForm,
    DepartmentForm,
    SubjectsForm,
    CourseForm,
    StudentForm,
    ProfessorForm,
    ExamsForm,
)


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
        department_form = DepartmentForm(request.POST, instance=department)
        if department_form.is_valid():
            department_form.save()
            return redirect("departments_list")
    else:
        department_form = DepartmentForm(instance=department)
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


def courses_list(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def create_or_edit_course(request, pk=None):
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = Course()

    if request.method == "POST":
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            return redirect("courses_list")
    else:
        course_form = CourseForm(instance=course)
    return render(request, "create_edit_course.html", {"form": course_form})


def students_list(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def create_or_edit_student(request, pk=None):
    if pk:
        student = get_object_or_404(Student, pk=pk)
    else:
        student = Student()

    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect("students_list")
    else:
        student_form = StudentForm(instance=student)
    return render(request, "create_edit_student.html", {"form": student_form})


def professors_list(request):
    professors = Professor.objects.all()
    return render(request, "professors.html", {"professors": professors})


def create_or_edit_professor(request: HttpRequest, pk=None):
    if pk:
        professor = get_object_or_404(Professor, pk=pk)
    else:
        professor = Professor()

    if request.method == "POST":
        professor_form = ProfessorForm(request.POST, request.FILES, instance=professor)
        if professor_form.is_valid():
            professor_form.save()
            return redirect("professors_list")
    else:
        professor_form = ProfessorForm(instance=professor)
    return render(request, "create_edit_professor.html", {"form": professor_form})


def exams_list(request):
    exams = Exams.objects.all()
    return render(request, "exams.html", {"exams": exams})


def create_or_edit_exam(request: HttpRequest, pk=None):
    if pk:
        exam = get_object_or_404(Exams, pk=pk)
    else:
        exam = Exams()

    if request.method == "POST":
        exam_form = ExamsForm(request.POST, instance=exam)
        if exam_form.is_valid():
            exam_form.save()
            return redirect("exams_list")
    else:
        exam_form = ExamsForm(instance=exam)
    return render(request, "create_edit_exam.html", {"form": exam_form})


"""
Retriving Single Object by its ID
"""


def department_view(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, "department_detail.html", {"department": department})


def subject_view(request, subject_id):
    subject = get_object_or_404(Subjects, id=subject_id)
    return render(request, "subject_detail.html", {"subject": subject})


def course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "course_detail.html", {"course": course})


def student_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "student_detail.html", {"student": student})


def professor_view(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    return render(request, "professor_detail.html", {"professor": professor})
