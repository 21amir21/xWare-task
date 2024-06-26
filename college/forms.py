from django.forms import ModelForm
from .models import Faculty


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        labels = {
            "F_name": "Faculty Name",
        }
