from django.urls import path
from . import views
from .views import TaskerHome, TaskDeleteView, RegisterUser, LoginUser, logout_user, UsersProfile

urlpatterns = [
	path('', TaskerHome.as_view(), name = 'home'),
	path('add', views.add, name = 'add'),
	path('add/', views.add_page, name = 'add_page'),
	# path('add_to_user', views.add_add_user, name = 'add_to_user'),
	path('register/', RegisterUser.as_view(), name = 'register'),
	path('login/', LoginUser.as_view(), name = 'login'),
	path('loglog/', logout_user, name = 'logout'),
	path('accounts/profile/', UsersProfile.as_view(), name = 'profile'),
	path('update/<int:task_id>/', views.update, name = 'update'),
	path('delete/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'delete'),
	path('accounts/profile/<int:task_id>', views.add_to_user, name = 'add_to_user'),
]