from django.forms import ModelForm
from .models import Faculty, Department, Professor, Student, Subjects, Course, Exams
from django import forms


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        labels = {
            "F_name": "Faculty Name",
        }


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {
            "D_name": "Department Name",
            "F_id": "Faculty ID",
        }


class SubjectsForm(ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
        labels = {
            "Sub_name": "Subject Name",
            "Sub_code": "Subject Code",
            "F_id": "Faculty",
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "Sub_id": "Subject",
            "P_id": "Professor ID",
        }
        widgets = {
            "Duration": forms.TimeInput(format="%H:%M:%S", attrs={"type": "time"}),
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "F_Name": "First Name",
            "L_Name": "Last Name",
            "F_Phone": "First Phone",
            "L_Phone": "Last Phone",
            "Birth_Date": "Birth Date",
        }
        widgets = {
            "Birth_Date": forms.DateInput(attrs={"type": "date"}),
        }


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"
        labels = {
            "F_id": "Faculty",
            "D_id": "Department",
            "F_Name": "First Name",
            "L_Name": "Last Name",
        }


class ExamsForm(ModelForm):
    class Meta:
        model = Exams
        fields = "__all__"
        labels = {
            "C_id": "Course",
        }
        widgets = {
            "Date": forms.DateInput(attrs={"type": "date"}),
            "Time": forms.TimeInput(attrs={"type": "time"}),
            "Duration": forms.TextInput(attrs={"placeholder": "HH:MM:SS"}),
        }
