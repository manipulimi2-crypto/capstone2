from django.shortcuts import render,redirect
from app.models import students
# Create your views here.
def index(request):
    data=students.objects.all()
    return render(request,'app/index.html',{"data":data})
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        quary=students(name=name,email=email,age=age,gender=gender)
        quary.save()
        return redirect('/')
    return render(request,'app/index.html')
def updateData(request,id):
    d=students.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        x=students.objects.get(id=id)
        x.name=name
        x.email=email
        x.age=age
        x.gender=gender
        x.save()
        return redirect('/')
    return render(request,'app/edit.html',{"d":d})
def deleteData(request,id):
    d=students.objects.get(id=id)
    d.delete()
    return redirect('/')

