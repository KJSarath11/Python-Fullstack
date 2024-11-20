from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    a=requests.get("https://restcountries.com/v2/all")
    data=a.json()
    return render(request,"index.html",{'data':data})

def display_all(request):
    data1=None
    if request.method=="POST":
        search=request.POST.get('search-bar')
        a=requests.get(f"https://restcountries.com/v2/name/{search}")
        data1=a.json()
    return render(request,"display.html",{'data1':data1})

