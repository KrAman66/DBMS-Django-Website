from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from random import randint
from authenticate.models import UserProfile


class TeacherForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username',widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Useriname'}))
    password = forms.CharField(label='Enter your Password',widget=forms.widgets.PasswordInput)
    email = forms.EmailField(label='Enter email ID',required=True,widget=forms.widgets.EmailInput(attrs={'Placeholder':'Enter Email'}))
    first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter First name'}))
    last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Last name'}))

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','password','email',)

class TeacherProfileChange(UserChangeForm): #inheriting
    email = forms.EmailField(label="Enter email id",required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Enter email'}))
    username = forms.CharField(disabled=True)
    password = None
    class Meta:
        model = User
        fields = ('username','email','password') # attribute from the auth_user table inside dbsqlite



class StudentForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', widget=forms.widgets.TextInput(attrs={'placeholder':"just the mailbox name of the email"}))
    password = forms.CharField(label='Enter your Password',widget=forms.widgets.PasswordInput(attrs={'placeholder':"first 3 letters of student's name @ student's birthyear"}))
    email = forms.EmailField(label='Enter email ID',required=True,widget=forms.widgets.EmailInput(attrs={'Placeholder':'Enter Email'}))
    # first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter First name'}))
    # last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Enter Last name'}))
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileChange(UserChangeForm): #inheriting
    email = forms.EmailField(label="Enter email id",required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Enter email'}))
    username = forms.CharField(disabled=True)
    password = None
    class Meta:
        model = User
        fields = ('username','email','password') # attribute from the auth_user table inside dbsqlite


class UserProfileChange(UserChangeForm): #inheriting
    email = forms.EmailField(label="Enter email id",required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Enter email'}))
    username = forms.CharField(disabled=True)
    password = None
    class Meta:
        model = User
        fields = ('username','email','password') # attribute from the auth_user table inside dbsqlite


class StudentMedia(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)
