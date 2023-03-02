from django.shortcuts import render,redirect
from .forms import facultyRegister
from faculty.models import facultyMember
def register(request):
    
    if request.method =='POST': 
        fm= facultyRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['mail']
            br = fm.cleaned_data['branch']
            print(nm)
            print(em)
            print(br)
            fm.save()
            return redirect('facultyData')
    else:
        fm = facultyRegister()
    return render(request,'facultyRegister.html',{'form':fm})

def facultyData(request):
    data= facultyMember.objects.all()
    return render(request, 'facultyData.html',{'data':data})

def facultyUpdate(request,uid):
    member = facultyMember.objects.get(id = uid)
    print('the member to be updated is ')
    print(member)
    
    if request.method == 'POST':
        fm = facultyRegister(request.POST,instance=member)
        if fm.is_valid():
            
            fm.save()
            return redirect('facultyData')
    else:
        fm = facultyRegister(instance=member)
    return render(request, 'facultyUpdate.html',{'form':fm,'member':member})
            # Create your views here.


def facultyDelete(request,uid):
    member = facultyMember.objects.get(id = uid)
    member.delete()
    return redirect('facultyData')