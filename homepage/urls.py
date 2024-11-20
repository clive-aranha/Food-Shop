from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="home"),
    path('About/', views.About, name='About'),
    path('Upload/', views.Upload, name='upload_images'),
    path('Login/', views.LoginView, name='login'),
    path('Logout/', views.logout_user, name='logout'),
    path('SignUp/', views.signup_user, name='signup'), 
    path('Product/<int:id>', views.product_view, name='product'),  
    path('addwish/<int:id>', views.wish_list, name='addwish'), 
    path('addcart/<int:id>', views.cart_list, name='addcart'),
    path('ShowWishlist/', views.show_wishlist, name='showwish'),
    path('Cartlist/', views.show_cartlist, name='cartwish'),
    path('remove_wish/<int:wishlist_id>/<int:product_id>/', views.remove_wish, name='removewish'),
    path('dummy/', views.show_api, name='dummy'),
]   

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)