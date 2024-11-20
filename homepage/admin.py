from django.contrib import admin
from .models import Foodiee
from .models import Foodimages
from .models import FoodReview,CartItem
# from .models import Loginform

# Register your models here.
admin.site.register(Foodiee)
class FoodUploadAdmin(admin.ModelAdmin):
    list_display={'name','category','cost','images'}
    fields=['name','category','cost','images']

admin.site.register(Foodimages)
# admin.site.register(Loginform)

from .models import Wishlist
from .models import Cart


admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(FoodReview)
admin.site.register(CartItem)

