from django.forms import ModelForm
from django import forms
from .models import User, Profile, Address

class UserForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','role',)
        widgets = {
            'username':forms.TextInput(attrs={"class": "form-control", "placeholder":"Your Name e.g 'Akash' "}),
            'email':forms.EmailInput(attrs={"class": "form-control", "placeholder":"Add Your Email Address here @"}),
            'first_name':forms.TextInput(attrs={"class": "form-control",}),
            'last_name':forms.TextInput(attrs={"class": "form-control", }),
            'role':forms.Select(attrs={"class": "form-control fw-bold"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ProfileForm(ModelForm):
    #profile_pic = forms.ImageField()
    class Meta:
        model = Profile
        fields = ('image',)
        widgets = {
            'image':forms.FileInput(attrs={"class": "form-control","id":"formFile","type":"file"}),
        }

        
   

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('line1', 'city', 'state', 'pincode')
        widgets = {
            'line1':forms.TextInput(attrs={"class": "form-control", }),
            'city':forms.TextInput(attrs={"class": "form-control",}),
            'state':forms.TextInput(attrs={"class": "form-control", }),
            'pincode':forms.TextInput(attrs={"class": "form-control", }),
            
        }



class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    