# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     return render(request,'app/home.html')

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SanPham
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import CreateUserForm 

def home(request):
    sanphams = SanPham.objects.all()  # Lấy tất cả các sản phẩm từ bảng
    return render(request, 'app/home.html', {'sanphams': sanphams})


def hangHoa(request):
    sanphams = SanPham.objects.all()  # Lấy tất cả các sản phẩm từ bảng
    return render(request, 'app/hanghoa.html', {'sanphams': sanphams})

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'app/signup.html', context)


def loginPage(request):
    #if request.user.is_authenticated:
        #return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.info(request,'user or password not correct!')
    context = {}
    return render(request,'app/login.html',context)