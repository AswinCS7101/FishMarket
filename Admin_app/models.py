from django.db import models



class ADD_Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='sample',default='null.jpeg')

class ADD_Products(models.Model):
    product_name = models.CharField(max_length=20)
    product_category = models.CharField(max_length=10)
    product_quantity = models.IntegerField()
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to='sample')

    def __str__(self):
        return self.product_name

 
class ADD_Recipe(models.Model):
    recipe_name = models.CharField(max_length=20)
    recipe_ingredients = models.TextField()
    recipe_instructions = models.TextField()  
    recipe_image = models.ImageField(upload_to ='sample')  