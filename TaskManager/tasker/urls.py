from django.urls import path

from . import views
from .views import TaskerHome, TaskDeleteView, RegisterUser, LoginUser, logout_user, UsersProfile

urlpatterns = [
	path('', TaskerHome.as_view(), name='home'),
	path('add', views.add_task, name='add_task'),
	path('add/', views.page_add_task, name='page_add_task'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('login/', LoginUser.as_view(), name='login'),
	path('loglog/', logout_user, name='logout'),
	path('accounts/profile/', UsersProfile.as_view(), name='profile'),
	path('update/<int:task_id>/', views.update, name='update'),
	path('delete/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
	path('accounts/profile/<int:task_id>/add', views.add_user, name='add_user'),
	path('accounts/profile/<int:task_id>/remove', views.remove_user, name='remove_user'),
]
