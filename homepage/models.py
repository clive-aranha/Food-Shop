from django.db import models
from django.utils import timezone

# Model for Foodiee
class Foodiee(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    
    #created = models.DateTimeField(auto_now_add=True)  # Set once when created
    #updated = models.DateTimeField(auto_now=True)  # Update on every save

    

# Model for Foodimages
class Foodimages(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField()
    cost = models.FloatField()
    images = models.ImageField(upload_to="foodimages/")

    
    #created = models.DateTimeField(auto_now_add=True)  # Set once when created
    #updated = models.DateTimeField(auto_now=True)  # Update on every save

    

# Model for LoginForm
# class Loginform(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.TextField()
    
    #created = models.DateTimeField(auto_now_add=True)  # Set once when created
    #updated = models.DateTimeField(auto_now=True)  # Update on every save


#wishlist and cart
from django.contrib.auth.models import User


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #whatever related is chanegd
    product=models.ManyToManyField(Foodimages)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)


class FoodReview(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     product=models.ForeignKey(Foodimages,on_delete=models.CASCADE)
     review_text=models.TextField()
     rating=models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,6)])

#simple
# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE) #whatever related is chanegd
#     product=models.ManyToManyField(Foodimages)
#     created = models.DateTimeField(auto_now_add=True)  # Set once when created
#     updated = models.DateTimeField(auto_now=True)  

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #whatever related is chanegd
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True)  



class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True) #whatever related is chanegd
    product=models.ForeignKey(Foodimages,on_delete=models.CASCADE)
    cart_count=models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)  # Set once when created
    updated = models.DateTimeField(auto_now=True) 

    
