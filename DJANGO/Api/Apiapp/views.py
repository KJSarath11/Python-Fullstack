from django.shortcuts import render,redirect
from rest_framework.decorators import api_view  #
from .models import Travel  #
from .serializer import Tserial  #
from rest_framework.response import Response  #


# Create your views here.
@api_view(["get", "post"])
def index(request):
    # GET METHOD
    if request.method == "GET":
        a = Travel.objects.all()
        serializer = Tserial(a, many=True)
        return Response(serializer.data)

    # POST METHOD
    if request.method == "POST":
        a = Tserial(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)


@api_view(["get", "put","delete"])
def update(request,pk):
    a = Travel.objects.get(id=pk)
    if request.method == "GET":
        serializer = Tserial(a)
        return Response(serializer.data)

    if request.method == "PUT":
        b = Tserial(instance=a, data=request.data)
        if b.is_valid():
            b.save()
            return Response(b.data)
        
    if request.method=="DELETE":
        a.delete()
        return redirect("home")
