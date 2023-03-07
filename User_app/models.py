from django.db import models
from Admin_app.models import ADD_Products

class Registeration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone_no = models.IntegerField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Cart(models.Model):
    user_id = models.ForeignKey(Registeration,on_delete=models.CASCADE) 
    product_id = models.ForeignKey(ADD_Products,on_delete=models.CASCADE) 
    price = models.FloatField(default=0)
    quantity= models.IntegerField(default=0)  
    total = models.FloatField(default=0)
    status = models.IntegerField(default=0)

class checkout_data(models.Model):
    cart_id = models.ForeignKey(Cart,null=True,blank=True,default=None,on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    address = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class New_register(models.Model):
    new_username = models.CharField(max_length=20)
    new_email = models.EmailField()
    new_phone_no = models.IntegerField()
    new_password = models.CharField(max_length=20) 
    new_status = models.IntegerField(default=0)
    
   