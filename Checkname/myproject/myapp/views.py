from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Checkname
from django.contrib import messages

# Create your views here.
def index(request):
    all_checkname = Checkname.objects.all()
    return render(request,"index.html",{"all_checkname" : all_checkname})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        #Receive data
        name = request.POST["name"]
        date = request.POST["date"]
        
        #Save data
        checkname = Checkname.objects.create(
            name=name,
            date=date
        )
        checkname.save()
        messages.success(request,"Your data already saved")

        #Back to
        return redirect("/")
    
    else :
        return render(request, "form.html")

def edit(request,person_id):
   if request.method == "POST":
       checkname = Checkname.objects.get(id=person_id)
       checkname.name = request.POST["name"]
       checkname.date = request.POST["date"]
       checkname.save()
       messages.success(request,"Updated")
       return redirect("/")
   else:
   #get the data to diplay in edit form
       checkname = Checkname.objects.get(id=person_id)
       return render(request,"edit.html",{"checkname":checkname})
   
def delete(request,checkname_id):
    checkname = Checkname.objects.get(id=checkname_id)
    checkname.delete()
    messages.success(request,"deleted")
    return redirect("/")