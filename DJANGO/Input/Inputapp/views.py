from django.shortcuts import render, redirect

# created model is imported here
from Inputapp.models import studentss


# Create your views here.
def index(request):
    student = studentss.objects.all()
    # database retrieves each and every data(here-student) from the students table.The result is typically a QuerySet, which is a list-like collection of database objects.

    context = {
        "student_list": student  # allows to access the data within HTML using 'student_list'
    }
    # context is a dictionary that hold the data to be passed to the templates

    return render(request, "index.html", context)


def list(request, pk):
    # student=students.objects.all() this is for al objects retrieving
    student = studentss.objects.get(id=pk)  # this is to retrieve only the particular id
    context1 = {"student_details": student}
    if request.method == "POST":
        student.delete()
        return redirect("home")
    return render(request, "list.html", context1)


def edit(request, pk):
    student = studentss.objects.get(id=pk)
    if request.method == "POST":
        student.name = request.POST.get("NAME")
        student.age = request.POST.get("AGE")
        student.phno = request.POST.get("PH")
        student.save()
        return redirect("home")
    return render(request, "edit.html", {"student": student})
