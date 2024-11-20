from django.shortcuts import render, HttpResponse, redirect
from .models import student
from .forms import studentform

# Create your views here.
def index(request):
    var=student.objects.all()
    context={
        'var':var
    }
    return render(request,"index.html",context)
    # if request.method == "POST":
    #     form = studentform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("Data added successfully")  # You can also use redirect to a success page if needed.
    #     else:
    #         return HttpResponse("Form data is invalid")  # Optional: Handle invalid form scenario explicitly.
    # else:
    #     form = studentform()  # Initialize the form for GET requests.
    
    # return render(request, "index.html", {'form': form},context)

def list(request):
    var=student.objects.all()
    context={
        'var':var
    }
    return render(request, "list.html",context)