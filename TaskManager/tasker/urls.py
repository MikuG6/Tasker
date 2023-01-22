from django.urls import path

from . import views
from .views import TaskerHome, TaskDeleteView, RegisterUser, LoginUser, logout_user, UsersProfile

urlpatterns = [
	path("", TaskerHome.as_view(), name="home"),
	path("account/register/", RegisterUser.as_view(), name="register"),
	path("account/login/", LoginUser.as_view(), name="login"),
	path("account/logout/", logout_user, name="logout"),
	path("account/profile/", UsersProfile.as_view(), name="profile"),
	path("tasks/", views.TaskView.as_view(), name="tasks"),
	path("tasks/<int:task_pk>/users/<int:user_pk>/add", views.TaskAddUserView.as_view(), name="add_user"),
	path("tasks/<int:task_pk>/users/<int:user_pk>/remove", views.TaskRemoveUserView.as_view(), name="remove_user"),
	path("tasks/<int:task_pk>/update", views.TaskUpdateView.as_view(), name="update_task"),
	path("tasks/<int:task_pk>/delete", views.TaskDeleteView.as_view(), name="delete_task"),
]
