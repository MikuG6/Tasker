from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .utils import *


class TaskerHome(ListView):
	model = Task
	template_name = 'tasker/index.html'
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = Task.objects.all().order_by('id')
		return context


# def index(request):
# 	obj = TaskAbout.objects.all()
# 	context = {
# 		'obj_list': obj,
# 		'title': 'Главная страница'
# 	}
# 	print(obj)
# 	return render(request, 'tasker/index.html', context)


def page_add_task(request):
	return render(request, 'tasker/add_task.html')


@require_http_methods(['POST'])
def add_task(request):
	title = request.POST['title']
	task = Task.objects.create(title=title)
	task.users.add(request.user)
	return redirect('home')


def update(request, task_id):
	task = Task.objects.get(id=task_id)
	task.is_complete = not task.is_complete
	task.save()
	return redirect('home')


class TaskDeleteView(DeleteView):
	model = Task
	success_url = reverse_lazy('home')


# def delete(request, task_id):
# 	task = TaskAbout.objects.get(id = task_id)
# 	task.delete()
# 	return redirect('index')


class RegisterUser(DataMixin, CreateView):
	form_class = UserCreationForm
	template_name = 'tasker/register.html'
	success_url = reverse_lazy('home')

	def get_context_data(self, *, objects_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'Регистрация')
		return dict(list(context.items())+list(c_def.items()))

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('home')


class LoginUser(DataMixin, LoginView):
	form_class = AuthenticationForm
	template_name = 'tasker/login.html'
	success_url = reverse_lazy('home')

	def get_context_data(self, *, objects_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'Авторизация')
		return dict(list(context.items())+list(c_def.items()))


def logout_user(request):
	logout(request)
	return redirect('login')


class UsersProfile(ListView):
	model = Task
	template_name = 'tasker/user_profile.html'
	context_object_name = 'user_data'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# сортировка тасок по id
		context['order_tasks'] = Task.objects.all().order_by('id')
		# возращает список тасков которые относятся к этому пользователю
		context['tasks_list'] = Task.objects.filter(users__username=self.request.user)
		context['tasks_dict'] = Task.objects.values('title')
		return context


def add_user(request, task_id):
	task = Task.objects.get(id=task_id)
	request.user.tasks.add(task)
	return redirect('home')


def remove_user(request, task_id):
	task = Task.objects.get(id=task_id)
	request.user.tasks.remove(task)
	return redirect('home')
