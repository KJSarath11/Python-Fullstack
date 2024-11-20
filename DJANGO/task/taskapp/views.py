from django.shortcuts import render, redirect
from .models import student  # Make sure your model is correctly named
from .forms import studentForm  # Ensure your form is defined properly

def index(request):
    """Render the form for adding students and handle the form submission."""
    form = studentForm()  # Cre`ate an empty form instance

    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            student_instance = form.save()  # Save the student to the database
            # Redirect to the display view with the name and course of the added student
            return redirect('display', name=student_instance.name, course=student_instance.course)

    # Fetch all students to show on the index page (if needed)
    data = student.objects.all()
    return render(request, 'index.html', {'form': form, 'data': data})

def display(request, name, course):
    """Display the latest added student."""
    context = {'name': name, 'course': course}
    return render(request, 'display.html', context)

def view_all(request):
    """Display all registered students."""
    students = student.objects.all()  # Fetch all students from the database
    context = {'students': students}
    return render(request, 'view_all.html', context)
