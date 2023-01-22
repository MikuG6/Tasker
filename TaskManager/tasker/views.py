from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView, TemplateView

from .forms import *
from .utils import *


class TaskerHome(ListView):
	model = Task
	template_name = "tasker/index.html"
	context_object_name = "tasks"


class TaskView(FormView):
	model = Task
	template_name = "tasker/add_task.html"

	def post(self, request, *args, **kwargs):
		title = request.POST["title"]
		task = Task.objects.create(title=title)
		task.users.add(request.user)
		return redirect("home")


class TaskUpdateView(TemplateView):
	queryset = Task.objects.all()
	success_url = reverse_lazy("home")

	def post(self, request, *args, **kwargs):
		task = get_object_or_404(Task, pk=kwargs["task_pk"])
		task.is_complete = not task.is_complete
		task.save()
		return redirect("home")


class TaskDeleteView(DeleteView):
	model = Task
	success_url = reverse_lazy("home")

	def post(self, request, *args, **kwargs):
		task = get_object_or_404(Task, pk=kwargs["task_pk"])
		task.delete()
		return redirect("home")


class RegisterUser(DataMixin, CreateView):
	form_class = UserCreationForm
	template_name = "tasker/register.html"
	success_url = reverse_lazy("home")

	def get_context_data(self, *, objects_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = "Регистрация")
		return dict(list(context.items())+list(c_def.items()))

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect("home")


class LoginUser(DataMixin, LoginView):
	form_class = AuthenticationForm
	template_name = "tasker/login.html"
	success_url = reverse_lazy("home")

	def get_context_data(self, *, objects_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = "Авторизация")
		return dict(list(context.items())+list(c_def.items()))


def logout_user(request):
	logout(request)
	return redirect("login")


class UsersProfile(ListView):
	model = Task
	template_name = "tasker/user_profile.html"
	context_object_name = "user_data"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# сортировка тасок по id
		context["order_tasks"] = Task.objects.all().order_by("id")
		# возращает список тасков которые относятся к этому пользователю
		context["tasks_list"] = Task.objects.filter(users__username=self.request.user)
		context["tasks_dict"] = Task.objects.values("title")
		return context


class TaskAddUserView(CreateView):
	queryset = Task.objects.all()

	def post(self, request, *args, **kwargs):
		task = get_object_or_404(Task, pk=kwargs["task_pk"])
		user = get_object_or_404(User, pk=kwargs["user_pk"])
		task.users.add(user)
		return redirect("home")


class TaskRemoveUserView(DeleteView):
	model = Task
	success_url = reverse_lazy("home")

	def post(self, request, *args, **kwargs):
		task = get_object_or_404(Task, pk=kwargs["task_pk"])
		user = get_object_or_404(User, pk=kwargs["user_pk"])
		task.users.remove(user)
		return redirect("home")
