from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
  
class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=20, label='логин')
	first_name = forms.CharField(max_length=32, label='имя')
	last_name=forms.CharField(max_length=32, label='фамилия')
	email=forms.EmailField(max_length=64, label='почта')
	password1=forms.CharField(widget=forms.PasswordInput(), label='пароль')
	password2=forms.CharField(widget=forms.PasswordInput(), label='повторите пароль')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		labels = {
    		'username': 'логин',
    		'first_name': 'Имя',
    		'last_name': 'Фамилия',
    		'email': 'Почта',
    		'password1': 'пароль',
    		'password2': 'подтверждение пароля',
    	}

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='пароль')

    class Meta:
    	model = User
    	fields = ['username', 'password']
    	labels = {
    		'username': 'логин',
    		'password': 'пароль',
    	}

class CreatePostForm(forms.ModelForm):
	post_title = forms.CharField(max_length=50, label='заголовок')
	post_text = forms.CharField(max_length=200, label='текст')

	class Meta:
		model = Post
		fields = ('post_title', 'post_text')