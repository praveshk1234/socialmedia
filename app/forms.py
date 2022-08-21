from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, Profile
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password'})

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_img','caption']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname','dob','email','profile_img']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        