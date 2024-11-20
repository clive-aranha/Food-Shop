from django.shortcuts import render, redirect
from .models import Foodiee
from .models import Foodimages,Wishlist,Cart,FoodReview,CartItem
from .forms import UploadForms# Updated form import


from django.contrib.auth.decorators import login_required


# def Home(request):
#     Foodiees = Foodiee.objects.all()
#     context = {"Foodiee": Foodiees}
#     return render(request, "Home.html", context)

def Home(request):
    Foodiees = Foodimages.objects.all()
    context = {"Foodiee": Foodiees}
    return render(request, "Home.html", context)

def About(request):
    return render(request, "About.html")

# @login_required
@login_required(login_url="/Login")
def Upload(request):
    if request.method == 'POST':
        form = UploadForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForms()

    return render(request, "Upload.html", {'form': form})

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

def LoginView(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)  
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)  #session
                return redirect('home')
            else:
                return render(request,"login.html", {'form': form})
    else:
        form = AuthenticationForm() 
        return render(request,"login.html", {'form': form})

def signup_user(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"Signup.html", {'form': form})

    else:
        form=UserCreationForm()
        return render(request,"Signup.html", {'form': form})

def logout_user(request):
    logout(request) #session
    return redirect('home')


from django.shortcuts import get_object_or_404
def product_view(request,id):
    product=get_object_or_404(Foodimages,id=id)
    review_obj=FoodReview.objects.filter(product=product)
    return render(request, "Product.html",{'product':product,"review_obj":review_obj})

#simpleone
# def wish_list(request,id):
#     user=request.user
#     product=Foodimages.objects.get(id=id)
#     obj1=Wishlist(user=user)
#     obj1.save()
#     obj1.product.add(product)
#     obj1.save()
#     return redirect("home")

#modified
# def wish_list(request,id):
#     product=Foodimages.objects.get(id=id)
#     obj1,created=Wishlist.objects.get_or_create(user=request.user)
#     obj1.product.add(product)
#     obj1.save()
#     return redirect("home")

def wish_list(request, id):
    product = Foodimages.objects.get(id=id)
    
    # Retrieve or create a Wishlist object for the user
    obj1, created = Wishlist.objects.get_or_create(user=request.user)
    
    # If there are multiple wishlists for the user, get the first one
    if not created:
        obj1 = Wishlist.objects.filter(user=request.user).first()
    
    # Add the product to the wishlist
    obj1.product.add(product)
    obj1.save()
    return redirect("home")





from django.shortcuts import redirect, get_object_or_404
from .models import Foodimages, Wishlist

#modified add to cart
# def cart_list(request,id):
#     #check user has cart or not
#     user_cart,created=Cart.objects.get_or_create(user=request.user)
#     #fetch product with given id
#     product=Foodimages.objects.get(id=id)
#     #create cart with cart items using user and product
#     cart_item,created=CartItem.objects.get_or_create(user=user_cart,product=product)
#     cart_item.product=product
#     cart_item.save()
#     return redirect("home")


def cart_list(request, id):
    # Check if the user has a cart or not
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    # If there are multiple carts for the user, get the first one
    if not created:
        user_cart = Cart.objects.filter(user=request.user).first()
    
    # Fetch the product with the given ID
    product = Foodimages.objects.get(id=id)
    
    # Create cart items using the user cart and product
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
    cart_item.product = product
    cart_item.save()
    
    return redirect("home")


# def wish_list(request, id):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Ensure the user is logged in

#     user = request.user
#     product = get_object_or_404(Foodimages, id=id)
    
#     # Create or get the Wishlist object for the user
#     wishlist, created = Wishlist.objects.get_or_create(user=user)
    
#     # Add the product to the wishlist
#     wishlist.product.add(product)

#     # Redirect to the home page after adding the product
#     return redirect('home')

# def cart_list(request,id):
#     user=request.user
#     product = get_object_or_404(Foodimages, id=id)
    
#     # Create or get the Wishlist object for the user
#     cart, created = Cart.objects.get_or_create(user=user)
    
#     # Add the product to the wishlist
#     cart.product.add(product)

#     # Redirect to the home page after adding the product
#     return redirect('home')



# def SampleClass():
#     def __init(self,x,y):
#         self.x=x
#         self.y=y
#     def save(self):
#         print("Save")
# obj1=SampleClass(10,20)
# obj1.save()



# def show_wishlist(request):
#     user=request.user
#     products=Wishlist.objects.get(user=user)
#     return render(request,"ShowWishlist.html",{"viewproduct":products.product.all()})

# @login_required

@login_required(login_url="/Login")
def show_wishlist(request):
    user = request.user  # Get the logged-in user
    wishlists = Wishlist.objects.filter(user=user)  # Get all wishlists for the user

    # Create a list of dictionaries containing products and their associated wishlist IDs
    products_with_wishlists = []
    for wishlist in wishlists:
        for product in wishlist.product.all():  # Loop through all products in the wishlist
            products_with_wishlists.append({
                'product': product,
                'wishlist_id': wishlist.id  # Include the wishlist ID for removal
            })

    # Pass the data to the template
    return render(request, "ShowWishlist.html", {"viewproduct": products_with_wishlists})

# @login_required
@login_required(login_url="/Login")
#show list of cart item
def show_cartlist(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items=CartItem.objects.filter(cart=cart)
    return render(request,"Cartlist.html",{"user_products": cart_items})

def remove_wish(request, wishlist_id, product_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    product = get_object_or_404(Foodimages, id=product_id)

    # Remove the product from the wishlist
    wishlist.product.remove(product)

    # Redirect back to the wishlist
    return redirect('showwish')
    
from django.http import JsonResponse

def show_api(request):
    # message = {
    #     "data1":"Hey this is my data",
    #     "data2":"Hey this is my data",
    #     "data3":"Hey this is my data"
    #     } 
    start_text=request.GET.get('parameter1')
    FoodName=Foodimages.objects.filter(name__startswith=start_text).first() 
    if FoodName:
        message={
            "FoodName":FoodName.name,
            "name":"Hey this is my data"
        }
    else:
        message={
            "name":"data is not found"
    }
    return JsonResponse(message)