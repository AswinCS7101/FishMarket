from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from User_app.models import Registeration
from User_app.models import New_register
from User_app.models import checkout_data

def admin_login(request):
    return render(request,'admin_login.html')

def admin_registeration(request):
    return render(request,'admin_registeration.html')


    
def member_login(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        user = authenticate(request,username=username_r,password=password_r)
        if user is not None:
            login(request,user)
            return redirect('admin_index')
        else :
            return render(request,'admin_login.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request,'admin_login.html')   

def admin_logout(request):
    del request.session['uname']
    del request.session['uemail']
    del request.session['umobile']
    del request.session['username']
    del request.session['password']    
    del request.session['uid']
    return redirect('admin_index')         

def admin_index(request):
    c=ADD_Category.objects.count()
    p=ADD_Products.objects.count()
    r=ADD_Recipe.objects.count()
    u=Registeration.objects.count()
             
    return render(request,'admin_index.html',{'c':c,'p':p,'r':r,'u':u})

def add_category(request):
    return render(request,'add_category.html')    

def view_catagory(request):
    data = ADD_Category.objects.all()
    return render(request,'view_category.html',{'data':data})    

def adding_category(request):
    if request.method =='POST':
        name = request.POST.get('category_name')  
        desc = request.POST.get('category_description')
        img = request.FILES['category_image']
        data = ADD_Category(category_name=name,category_description=desc,category_image=img)
        data.save()

        return redirect('view_category')  
    
def edit_category(request,ID):
    data = ADD_Category.objects.filter(id=ID)
    return render(request,'edit_add_category.html',{'data':data})

def edit_add_category(request,Id):
    if request.method == 'POST':
        name = request.POST.get('category_name')  
        desc = request.POST.get('category_description')
        try:
            img_c = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = ADD_Category.objects.get(id=id).img

        ADD_Category.objects.filter(id=Id).update(category_name=name,category_description=desc,category_image=file)

        return redirect('view_category')

def delete_category(request,Id):
    ADD_Category.objects.filter(id=Id).delete()
    return redirect('view_category')


def add_product(request):
    data = ADD_Category.objects.all()
    return render(request,'add_product.html',{'data':data})   

def adding_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        category = request.POST.get('product_category') 
        quantity = request.POST.get('product_quantity')  
        price = request.POST.get('product_price')    
        img =request.FILES['product_image'] 
        data = ADD_Products(product_name=name,product_category=category,product_quantity=quantity,product_price= price,product_image=img )
        data.save()
        return redirect('view_products')

def view_products(request):
    data = ADD_Products.objects.all()
    return render(request,'view_products.html',{'data':data})

def add_recipe(request):
    return render(request,'add_recipe.html')  

def adding_recipe(request):      
    if request.method == 'POST':
        name = request.POST.get('recipe_name')
        ingredients= request.POST.get('recipe_ingredients') 
        instructions = request.POST.get('recipe_instructions') 
        img =request.FILES['recipe_image'] 
        data = ADD_Recipe(recipe_name=name,recipe_ingredients=ingredients,recipe_instructions=instructions,recipe_image=img )
        data.save()
        return redirect('view_recipe')

def view_recipe(request):
    data = ADD_Recipe.objects.all()
    return render(request,'view_recipe.html',{'data':data})

def view_users(request):
    data =Registeration.objects.all()
    return render(request,'view_users.html',{'data':data})

def new_admin_register(request):
    data = New_register.objects.all()
    return render(request,'new_admin_register.html',{'data':data})

def approve_user(request,ID):
    New_register.objects.filter(id=ID).update(new_status=1)
    return redirect('new_admin_register')

def user_delete(request,Id):
    New_register.objects.filter(id=Id).delete()
    return redirect('new_admin_register')

def check_out_table(request):
    data = checkout_data.objects.all()
    return render(request,'check_out_table.html',{'data':data})