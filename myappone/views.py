from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import employeedetail

# Create your views here.

def home(request):
    return render(request,'home1.html') 


def register(request):
    if request.method == "POST":
        #creating user
        if request.POST['pass1'] == request.POST['pass2']:
            #checking wheather password and confirm password is same
            #now check if a previous user exsits
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'login1.html',{'error':"User already Exsists"})
            #if user does not exist
            except User.DoesNotExist:
                user = User.objects.create_user (username=request.POST['username'],
                password = request.POST['pass1'],email= request.POST['email'],first_name = request.POST['fname'],last_name = request.POST['lname'])
                #redirect to login page
                auth.login(request,user)
                return redirect ('login1.html',request)
        else:
            return render(request,'register1.html',{'error':"passwords Don't Match"})
    else:
        return render(request,'register1.html')

def login(request):
    if request.method == "POST":
        #check if a user exists
        #with username and password
        userid = request.POST['username']
        passwordl = request.POST['pass1']
        #check user exists
        user = auth.authenticate(username= userid , password = passwordl)
        #if user exists login
        if user is not None:
            auth.login(request,user)
            return redirect('empretrive.html', request)  
        #if user not exists
        else:
            return render(request,'register1.html',{"error1":"No user exsits kindly Register here "})
    #if method is not post
    else:
        return render(request,'login1.html')


def logout(request):    
    auth.logout(request)
    return redirect ('home1.html',request)

def base1(request):
    return render(request,'base1.html')
    
def home1(request):
    return render(request,'home1.html')

def register1(request):
    return render(request,'register1.html')

def empadd(request):
    if request.method == 'POST':
            empid = request.POST.get('Emp_Id_name')
            empname = request.POST.get('Empname_name')
            emplname = request.POST.get('Emplname_name')
            designation = request.POST.get('EmpDesignation_name')
            contact = request.POST.get('EmpContactNo_name')
            joiningdate = request.POST.get('Empjoindate_name')
            Esalary = request.POST.get('Empsalary_name')
            Egmail = request.POST.get('Empgmail_name')
            Empadd = employeedetail( empid=empid, empname=empname, emplname=emplname, designation=designation, contact=contact, joiningdate=joiningdate, Esalary=Esalary, Egmail=Egmail)
            Empadd.save()
            return render(request,'empadd.html',{"empaddnote":"Successfully Added Employee"})
    elif not request.user.is_authenticated:
        return redirect('login1.html')
    else:
        return render(request,'empadd.html',{"empnotaddnote":"No Employee Added Try Again"})

def employee_list(request):
    if not request.user.is_authenticated:
        return redirect('login1.html')
    else:
        employee_details = employeedetail.objects.all()
        return render(request, 'empretrive.html',{'employee_details': employee_details})


def delete_data(request,empid):
    if not request.user.is_authenticated:
        return redirect('login1.html')
    else:
        employeedetail.objects.filter(id=empid).delete()
        return redirect('empretrive')

def edit_data(request,empid):
    my_emp_data = employeedetail.objects.get(id=empid)
    my_emp_data.joiningdate = str(my_emp_data.joiningdate) 
    return render(request, 'empedit.html',{'my_emp_data':my_emp_data})

def update_data(request,empid):
    my_emp_data = employeedetail.objects.get(id=empid)
    my_emp_data.empid= request.POST['Emp_Id_name']     
    my_emp_data.empname= request.POST['Empname_name']
    my_emp_data.emplname = request.POST['Emplname_name']   
    my_emp_data.designation = request.POST['EmpDesignation_name']
    my_emp_data.contact = request.POST['EmpContactNo_name']
    my_emp_data.joiningdate = request.POST['Empjoindate_name']
    my_emp_data.Esalary = request.POST['Empsalary_name']
    my_emp_data.Egmail = request.POST['Empgmail_name']
    my_emp_data.save()
    return redirect('empretrive')
        

def defaultpage(request):
    if not request.user.is_authenticated:
        return redirect('login1.html')
    else:
        return render(request,'default.html')
    
def update_empadd(request):
    return redirect('empadd.html')

def update_empret(request):
    return redirect('empretrive')

def update_default(request):
    return redirect('default')