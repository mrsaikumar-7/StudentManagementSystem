from django.shortcuts import render,redirect
from django.http import HttpResponse
from student.models import register,library
from .forms import libraryForm

# Create your views here.

def studentRegister(request):
    if request.method == 'POST':
        
        Vname = request.POST['Name']
        Vmail = request.POST['Mail']
        Vbranch = request.POST['Branch']
        Vdob = request.POST['Dob']
        Vgender = request.POST['Gender']
        Vage = request.POST['Age']
        Vpassword = request.POST["Psw"]
        
        obj = register(studentName = Vname, mail=Vmail, gender = Vgender,dob=Vdob, age = Vage,branch=Vbranch ,password = Vpassword)
        obj.save()
        return redirect('data')
    return render(request, 'studentregister.html')


def studentData(request):
    data = register.objects.all()
    return render(request,'result.html',{'data' : data})


def studentUpdate(request,uid):
    student = register.objects.get(id=uid)
    if request.method == 'POST':
        
        student.studentName = request.POST['Name']
        student.mail = request.POST['Mail']
        student.branch = request.POST['Branch']
        student.dob = request.POST['Dob']
        student.gender = request.POST['Gender']
        student.age = request.POST['Age']
        student.password = request.POST["Psw"]
        student.save()
        return redirect('data')
    
    return render(request,'studentUpdate.html',{'student' :student })

def studentDelete(request,uid):
    student = register.objects.get(id=uid)
    student.delete()
    return redirect('data')

def library(request):
    fm = libraryForm()
    if request.method == 'POST':
        fm = libraryForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
        else:
            return HttpResponse('data is invalid')
        
    return render(request,'library.html',{'form':fm})

def home(request):
   return render(request,'base.html')
        