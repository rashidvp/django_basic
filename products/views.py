from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.urls import reverse
from .models import Product
from .models import User
from .models import Form

# Create your views here.
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = User.objects.all()
        user = auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            message.info(request,"Invalid Credentials")
            return redirect('login')

    else:
        return render(request,'login.html')

    '''user = User.objects.all()
    
    return render(request,'login.html',{'user':user})'''

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def contact(request):
    if request.method =='POST':
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        s = Form(email=email,subject=subject,message=message)
        s.save()

    return render(request,'contact.html')
