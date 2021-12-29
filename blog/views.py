from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import RegistrationForm, LoginUserForm, CreatePostForm
from .models import Post, Comment, AdminInformation
import datetime

def index(request):
	all_users = User.objects.filter(is_staff = 0)
	all_posts = Post.objects.filter(user = request.user.id).count()
	all_admin_inf = AdminInformation.objects.all()
	return render(request, 'index.html', {'all_users': all_users, 'all_posts': all_posts, 'all_admin_inf':all_admin_inf })

def registrationUser(request):
	all_admin_inf = AdminInformation.objects.all()
	form = RegistrationForm(data=request.POST)
	if form.is_valid():
		form.save()
		return redirect('blog:loginUser')
	else:
		return render(request, 'registration.html', {'form': form, 'all_admin_inf':all_admin_inf})

def loginUser(request):
	all_admin_inf = AdminInformation.objects.all()
	form = LoginUserForm(request=request, data=request.POST)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect('blog:index')
	else:
		return render(request, 'login.html', {'form': form, 'all_admin_inf':all_admin_inf})

def logoutUser(request):
	logout(request)
	return redirect('blog:index')

def viewProfile(request, user_id):
	all_admin_inf = AdminInformation.objects.all()
	user = User.objects.get(id = user_id)
	posts = Post.objects.all().filter(user_id = user_id)
	all_posts = Post.objects.filter(user = request.user.id).count()
	return render(request, 'profile.html', {'user': user, 'posts': posts, 'all_posts': all_posts, 'all_admin_inf':all_admin_inf })

def viewPost(request, user_id, post_id):
	all_admin_inf = AdminInformation.objects.all()
	user = User.objects.get(id = user_id)
	post = Post.objects.get(id = post_id)
	comments = Comment.objects.all().filter(post_id = post_id)
	all_posts = Post.objects.filter(user = request.user.id).count()
	return render(request, 'viewPost.html', {'post': post, 'user': user, 'comments': comments, 'all_posts': all_posts, 'all_admin_inf':all_admin_inf}) 

def createPost(request):
	all_admin_inf = AdminInformation.objects.all()
	form = CreatePostForm(data=request.POST)
	if form.is_valid():
		post_title = form.cleaned_data.get('post_title')
		post_text = form.cleaned_data.get('post_text')
		pub_date = datetime.datetime.now()
		author_first_name = request.user.first_name
		author_last_name = request.user.last_name
		user_id = request.user.id
		Post.objects.create(post_title = post_title, post_text = post_text, pub_date = pub_date, author_first_name = author_first_name, author_last_name = author_last_name, user_id = user_id)
		return HttpResponseRedirect( reverse('blog:viewProfile', args = [request.user.id]))
	else:
		return render(request, 'createPost.html', {'form': form, 'all_admin_inf':all_admin_inf})

def leave_comment(request, user_id, post_id):
	post = Post.objects.get(id = post_id)
	first_name = request.user.first_name
	last_name = request.user.last_name
	post.comment_set.create(author_first_name=first_name, author_last_name=last_name, comment_text = request.POST['text'])
	return HttpResponseRedirect( reverse('blog:viewPost', args=[user_id, post_id]))