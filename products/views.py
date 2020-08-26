from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse
from .models import Product
from .models import User
from .models import Form

# Create your views here.
def logine(request):
    users = User.objects.all()
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        '''user = authenticate(username=username,password=password)'''

        if username == 'admin' and password == 'test':
            return redirect("admin")
        if User.objects.filter(username='username', password='password'):
            return redirect("index")
        '''if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.info(request,"Please provide valid username and password!!!")
            return redirect("black")
            #return HttpResponse("invalid")'''

    else:
        return render(request,'login.html')

    '''user = User.objects.all()
    
    return render(request,'login.html',{'user':user})'''

def black(request):
    return render(request,'black.html')

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'signup.html', {'form':form})

def contact(request):
    if request.method =='POST':
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        s = Form(email=email,subject=subject,message=message)
        s.save()

    return render(request,'contact.html')

def admin(request):
    products = Product.objects.all()
    return render(request,'admin.html',{'products':products})

def admin_add(request):
    return render(request,'add.html')

def update_id_catch(request):
    return render(request,'update_id_catch.html')

def admin_update(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            n=request.POST.get('id')
            products = Product.objects.filter(id=n)
            return render(request,'update.html',{'products':products})
        else:
            return render(request,'update_id_catch.html')
    else:
            return render(request,'update_id_catch.html')

def admin_delete(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            n=request.POST.get('id')
            Product.objects.filter(id=n).delete()
            return redirect("admin")
    else:
        return render(request,'delete.html')


def admin_add(request):
        if request.method == 'POST':
            if request.POST.get('id') and request.POST.get('name') and request.POST.get('price') and request.POST.get('stock') and request.POST.get('image'):
                post=Product()
                post.id= request.POST.get('id')
                post.name= request.POST.get('name')
                post.price= request.POST.get('price')
                post.stock= request.POST.get('stock')
                post.image= request.POST.get('image')
                post.save()
                
                return redirect("admin")
            else:
                return redirect("admin_add")
                

        else:
                return render(request,'add.html')

def registration(request):
    return render(request,'user_reg.html')

def registration(request):
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('password'):
                post=User()
                post.username= request.POST.get('username')
                post.password= request.POST.get('password')
                post.save()
                return redirect("login")
            else:
                return redirect("registration")
                

        else:
                return render(request,'user_reg.html')

'''def admin_update(request):
        if request.method == 'POST':
            if request.POST.get('id') and request.POST.get('name') and request.POST.get('price') and request.POST.get('stock') and request.POST.get('image'):
                post=Product()
                post.id= request.POST.get('id')
                post.name= request.POST.get('name')
                post.price= request.POST.get('price')
                post.stock= request.POST.get('stock')
                post.image= request.POST.get('image')
                post.save()
                
                return redirect("admin")
            else:
                return redirect("admin_update")
                

        else:
                return render(request,'update.html')'''

'''def admin_add(request):
    if request.method == "POST" or None:
        form = MyForm(request.POST or None)
        if  form.is_valid():
            form.save()
            return render(request,'admin.html',{'form':form})
        else:
            form = MyForm()
            return render(request, 'add.html',{'form':form})
    else:
        form = MyForm()
        return render(request, 'add.html')'''

