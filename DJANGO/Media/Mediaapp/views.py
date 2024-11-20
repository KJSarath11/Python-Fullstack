from django.shortcuts import render,redirect
from .forms import mediaform
from .models import media

# Create your views here.
def index(request):
    if request.method=="POST":
        form=mediaform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("display")
    else:
        form=mediaform()
    return render(request,"index.html",{"form":form})

def view_image(request):
    display=media.objects.all()
    return render(request,"display.html",{"display":display})