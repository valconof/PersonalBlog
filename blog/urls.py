from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('registration/', views.registrationUser, name = 'registrationUser'),
	path('login/', views.loginUser, name = 'loginUser'),
	path('logoutUser/', views.logoutUser, name = 'logoutUser'),
	path('<int:user_id>/', views.viewProfile, name = 'viewProfile'),
	path('<int:user_id>/<int:post_id>/', views.viewPost, name = 'viewPost'),
	path('<int:user_id>/<int:post_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
	path('createPost/', views.createPost, name = 'createPost'),
	]