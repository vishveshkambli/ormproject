from django.shortcuts import render,redirect

# Create your views here.
from .models import Emp


def homef(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        age=request.POST.get('age')
        address=request.POST.get('address')
        e=Emp()
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect('/')
    else:    
        return render(request,'addemp.html')

from .form import EmpForm, EmpForm2, AccountForm
  
def add_emp2(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        d={'form':f}
        return render(request,'addemp2.html',d)
    
def add_emp3(request):
    if request.method=='POST':
        f=EmpForm2(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm2
        d={'form':f}
        return render(request,'addemp3.html',d)
    
def add_account(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm
        d={'form':f}
        return render(request,'addaccount.html',d)
    
def emp_list(request):
    emp=Emp.objects.all()
    context={'el':emp}
    return render(request,'emplist.html', context)

def delete1_emp(request):
    eid=request.GET.get('id')
    Emp.objects.get(id=eid)
    emp=Emp.objects.get(id=eid)
    emp.delete()
    
    return redirect('/emplist ')

def delete2_emp(request,id):
    
    emp=Emp.objects.get(id=id)
    emp.delete()
    
    return redirect('/emplist')

def edit_emp(request,id):
    emp=Emp.objects.get(id=id)
    if request.method=='POST':
       f=EmpForm(request.POST,instance=emp)
       f.save()
       return redirect('/emplist') 
    else:
        f=EmpForm(instance=emp)
        d={'form':f}
        return render(request,'addemp2.html',d)