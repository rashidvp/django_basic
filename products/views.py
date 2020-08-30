from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

def logine(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin')
        else:
            return redirect('index')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(username)
        if user is not None:
            if username == 'admin' and password =='test':
                auth.login(request,user)
                return redirect('admin')

            else:
                auth.login(request,user)
                return redirect('index')
        else:
            messages.error(request, 'Invalid username/password!')
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'login.html')

def black(request):
    return render(request,'black.html')

@login_required(login_url='/')
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

@login_required(login_url='/')
def admin(request):
    products = Product.objects.all()
    return render(request,'admin.html',{'products':products})

@login_required(login_url='/')
def admin_add(request):
    return render(request,'add.html')

def update_id_catch(request):
    return render(request,'update_id_catch.html')

@login_required(login_url='/')
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

@login_required(login_url='/')
def admin_delete(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            n=request.POST.get('id')
            Product.objects.filter(id=n).delete()
            return redirect("admin")
    else:
        return render(request,'delete.html')


@login_required(login_url='/')
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
            messages.error(request,"Enter Valid Detail")
            return redirect("admin_add")
            

    else:
            return render(request,'add.html')

def registration(request):
    return render(request,'user_reg.html')

def registration(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('login')
        else:
            return redirect('login')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        dic={"username":username,"email":email}
        if password1==password2:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            return redirect('login')
        else:
            messages.error(request,"Password Incorrect")
            return render(request,"user_reg.html",dic)
    else:
            return render(request,"user_reg.html")
            

@login_required(login_url='/')
def admin_search(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            n=request.POST.get('id')
            products = Product.objects.filter(id=n)
            return render(request,'admin.html',{'products':products})
        else:
            return render(request,'admin.html')
    else:
            return render(request,'admin.html')

@login_required(login_url='/')
def user_search(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            n=request.POST.get('id')
            products = Product.objects.filter(name=n)
            return render(request,'index.html',{'products':products})
        else:
            return render(request,'index.html')
    else:
            return render(request,'index.html')

def logout(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    request.session.flush()
    auth.logout(request)
    return redirect('login')

@login_required(login_url='/')
def user_list(request):
    users = User.objects.filter(is_superuser=False)
    return render(request,'user_list.html',{'users':users})