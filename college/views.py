from django.shortcuts import redirect, render, get_object_or_404
from .models import Faculty
from .forms import FacultyForm


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
    # faculty_form = FacultyForm()
    if request.method == "POST":
        faculty_form = FacultyForm(request.POST, instance=faculty)
        if faculty_form.is_valid():
            faculty_form.save()
            return redirect("faculty_list")
    else:
        faculty_form = FacultyForm(instance=faculty)
    return render(request, "create_faculty.html", {"form": faculty_form})
