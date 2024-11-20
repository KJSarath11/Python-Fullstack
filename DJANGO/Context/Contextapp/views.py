from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "Name":"Strawhat",
        "Games":["BGMI","Free Fire","Ludo","AmongUs","Templerun","SubwaySurfers"],
        "Student_details":{"sarath":88,"jins":91,"nibin":99,"salman":86,"rithik":95},
        "star1":"1*",
        "star2":"2*"
    }
    return render(request,"index.html",context)



# students who fot above 85 and 1* rating
# [sarath] get [86]marks and [1*] rating

# for loop and if condition
