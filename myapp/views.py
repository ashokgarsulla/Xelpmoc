from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = UserCreationForm()
    return render(request, 'myapp/register.html',{'form':fm})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST )
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/calculate') 
        else:
            fm = AuthenticationForm()      
        return render (request, 'myapp/login.html',{'form':fm})
    else: 
        return HttpResponseRedirect('/calculate')      
    

def fib_series(x,y):
    n1 = x
    n2 = y
    c = 0
    series = []
    while c < x:
        series.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        c = c + 1
    return series

def calculate(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == "POST":
            num1 = int(request.POST["num1"])
            num2 = int(request.POST["num2"])
            if num1 < 5 or num2 < 5:
                messages.error(request, "Number must be greater than 5")
            else:
                n1 = fib_series(int(num1),int(num2))
                return render(request,'myapp/calculate.html',{'username':username,"num1":n1})
        return render(request,'myapp/calculate.html',{'username':username})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



    

