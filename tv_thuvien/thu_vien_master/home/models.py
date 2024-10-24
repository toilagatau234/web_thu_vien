from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class SanPham(models.Model):
    idsanPham = models.IntegerField(primary_key=True)
    tenSanPham = models.CharField(max_length=255)
    hinhAnh = models.CharField(max_length=255)  
    maTheLoai = models.CharField(max_length=50)

    class Meta:
        db_table = 'sanpham' 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']

