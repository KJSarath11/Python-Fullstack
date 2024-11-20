from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #request.POST
    #.get to take inputs
    if request.method =="POST":
        firstnum=int(request.POST.get('first'))
        secondnum=int(request.POST.get('second'))
    # main feature
    if 'add' in request.POST:
        ADD=firstnum+secondnum
        return HttpResponse(f"The sum of {firstnum} + {secondnum} = {ADD}")
    #additional features
    if 'sub' in request.POST:
        SUB=firstnum-secondnum
        return HttpResponse(f"The difference of {firstnum} - {secondnum} = {SUB}")
    if 'mul' in request.POST:
        MUL=firstnum*secondnum
        return HttpResponse(f"The difference of {firstnum} * {secondnum} = {MUL}")
    if 'div' in request.POST:
        DIV=firstnum/secondnum
        return HttpResponse(f"The difference of {firstnum} / {secondnum} = {DIV}")
    if 'exp' in request.POST:
        EXP=firstnum**secondnum
        return HttpResponse(f"The difference of {firstnum} ^ {secondnum} = {EXP}")
    
    
    return render(request,"index.html")