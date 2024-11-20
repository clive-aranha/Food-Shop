from django import forms
from .models import Foodimages
# , Loginform

class UploadForms(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    category = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=True
    )
    cost = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=True
    )
    
    class Meta:
        model = Foodimages # Ensure the model name here matches your model
        fields = ['name', 'category', 'cost', 'images']


# Renamed the form class to avoid conflict
# class LoginForm(forms.ModelForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         required=True
#     )
#     password = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         required=True
#     )
    
#     class Meta:
#         model = Loginform  
#         fields = ['username', 'password']
