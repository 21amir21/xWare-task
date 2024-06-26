from django.forms import ModelForm
from .models import Faculty, Department, Subjects


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        labels = {
            "F_name": "Faculty Name",
        }


class SubjectForm(ModelForm):
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
