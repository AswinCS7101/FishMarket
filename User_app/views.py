from django.shortcuts import render,redirect
from . models import *
from Admin_app.models import ADD_Products
from Admin_app.models import ADD_Category
from Admin_app.models import ADD_Recipe
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def user_index(request):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    c=0
    u = request.session.get('uid')
    data3 = Cart.objects.filter(user_id = u,status=0)
    for i in data3 :
        c +=1
    return render(request,'user_index.html',{'data':data,'data2':data2,'c':c})

def user_view_recipe(request):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    data3= ADD_Recipe.objects.all()
    return render(request,'user_view_recipe.html',{'data3':data3,'data':data,'data2':data2})

def add_registeration(request):
    if request.method == 'POST':
        username =request.POST.get('username')     
        email = request.POST.get('email')  
        phone_no = request.POST.get('phoneno') 
        password =request.POST.get('password')
        data = Registeration(username=username,email=email,phone_no=phone_no,password=password)  
        data.save()
        return redirect('user_login')

def user_login(request):
    return render(request,'user_login.html')

def user_member_login(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if Registeration.objects.filter(username=username_r,password=password_r).exists():
            data = Registeration.objects.filter(username=username_r,password=password_r).values('username','email','phone_no','id').first()
            request.session['uname'] = data['username']
            request.session['uemail'] = data['email']
            request.session['umobile'] = data['phone_no']
            request.session['username'] = username_r
            request.session['password'] = password_r
            request.session['uid'] = data['id']
            return redirect('user_index')
        else:
            return render(request,'user_login.html',{'msg':'Sorry ! Invalid Credentials'})

def user_registeration(request):
    return render(request,'user_registeration.html')

def user_logout(request):
    del request.session['uname']
    del request.session['uemail']
    del request.session['umobile']
    del request.session['username']
    del request.session['password']    
    del request.session['uid']
    return redirect('user_index')  

def single_product(request,ID):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    data3 = ADD_Products.objects.filter(id=ID)
    u = request.session.get('uid')
    c = Cart.objects.filter(user_id = u,status=0).count()
    return render(request,'single_product.html',{'data3':data3,'data2':data2,'data':data,'c':c})

def user_cart(request):
    
    data2 = ADD_Category.objects.all()
    u = request.session.get('uid')
    data = Cart.objects.filter(user_id=u,status=0)
    c = Cart.objects.filter(user_id = u,status=0).count()
    s = Cart.objects.filter(user_id = u,status=0).aggregate(Sum('total'))
    return render(request,'user_cart.html',{'data':data,'data2':data2,'s':s,'c':c})

def add_to_cart(request,Id):
    if 'uid' in request.session:
        products_id = ADD_Products.objects.get(id=Id)
        userID = request.POST.get('userID')
        users_ID = Registeration.objects.get(id=userID)
        price = request.POST.get('price')
        qty =   request.POST.get('qty') 
        total = request.POST.get('total')
        data = Cart(product_id= products_id,user_id=users_ID,price=price,quantity=qty,total=total)
        data.save()
        return redirect('user_cart')
    else:
        return redirect('user_login')
    
def cart_delete(request,ID):
    Cart.objects.filter(id=ID).delete()
    return redirect('user_cart')

def check_out(request):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    u = request.session.get('uid')
    c = Cart.objects.filter(user_id = u,status=0).count()
    data3 = Cart.objects.filter(user_id=u,status=0)
    s = Cart.objects.filter(user_id = u,status=0).aggregate(Sum('total'))
    return render(request,'check_out.html',{'data3':data3,'data2':data2,'data':data,'s':s,'c':c})


def checking_out(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        u = request.session.get('uid')
        data = Cart.objects.filter(user_id=u,status=0)
        for i in data:
            cart = checkout_data(cart_id=Cart.objects.get(id=i.id),name=full_name, address = address,phone_no=phone_no,email=email,order=i.product_id.product_name )
            cart.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('user_index')    

def filter_category(request,filter):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    u = request.session.get('uid')
    c = Cart.objects.filter(user_id = u,status=0).count()
    f = ADD_Products.objects.filter(product_category = filter)
    return render(request,'filtered_category.html',{'f':f,'data':data,'data2':data2,'c':c})


def only_category(request):
    data2 = ADD_Category.objects.all()
    return render(request,'only_category.html',{'data2':data2})

def add_new_registeration(request):
    if request.method == 'POST':
        username =request.POST.get('username')     
        email = request.POST.get('email')  
        phone_no = request.POST.get('phoneno') 
        password =request.POST.get('password')
        data = New_register(new_username=username,new_email=email,new_phone_no=phone_no,new_password=password)  
        data.save()
        return redirect('new_admin_register')
    
def only_products(request):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    return render(request,'Only_products.html',{'data':data,'data2':data2})

def new_user_login(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if New_register.objects.filter(new_username=username_r,new_password=password_r,new_status=1).exists():
            return redirect('user_index')
        else:
            return render(request,'new_login.html',{'msg':'Status not Approved'})
        

@csrf_exempt        
def cart_update(request):
    if request.method == 'POST':
        cartid = request.POST.get('pid')
        q = request.POST.get('quantity')
        print(q)
        p = request.POST.get('price')
        total = float(q) * float(p)
        print(total)
        Cart.objects.filter(id=cartid).update(quantity=q,total=total)
    return HttpResponse()    

def contact(request):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    u = request.session.get('uid')
    c = Cart.objects.filter(user_id = u,status=0).count()
    return render(request,'contact.html',{'data':data,'data2':data2,'c':c})

def view_single_recipe(request,ID):
    data = ADD_Products.objects.all()
    data2 = ADD_Category.objects.all()
    data3 = ADD_Recipe.objects.filter(id=ID)
    return render(request,'view_single_recipe.html',{'data3':data3,'data2':data2,'data':data})