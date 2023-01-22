from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task_about
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from .forms import *
from .utils import *

class TaskerHome(ListView):
	model = Task_about
	template_name = 'tasker/index.html'
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['order_tasks'] = Task_about.objects.all().order_by('id')
		context['user1'] = self.request.user
		context['tasks_list'] = Task_about.objects.filter(user__username = self.request.user)
		context['tasks_dict'] = list(Task_about.objects.values_list('title', flat=True))
		return context
# def index(request):
# 	obj = Task_about.objects.all()
# 	context = {
# 		'obj_list': obj,
# 		'title': 'Главная страница'
# 	}
# 	print(obj)
# 	return render(request, 'tasker/index.html', context)

def add_page(request):
	return render(request, 'tasker/add_task.html')

@require_http_methods(['POST'])
def add(request):
	title = request.POST['title']
	task = Task_about(title = title)
	task.save()
	return redirect('home')

def update(request, task_id):
	task = Task_about.objects.get(id = task_id)
	task.is_complite = not(task.is_complite)
	task.save()
	return redirect('home')

class TaskDeleteView(DeleteView):
	model = Task_about
	success_url = reverse_lazy('home')

# def delete(request, task_id):
# 	task = Task_about.objects.get(id = task_id)
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
	model = Task_about
	template_name = 'tasker/user_profile.html'
	context_object_name = 'user_data'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['order_tasks'] = Task_about.objects.all().order_by('id') #сортировка тасков по id
		context['user1'] = self.request.user #текущий пользователь
		context['tasks_list'] = Task_about.objects.filter(user__username = self.request.user) #возращает список тасков которые относятся к этому пользователю
		context['tasks_dict'] = Task_about.objects.values('title')
		return context

def add_to_user(request, task_id):
	task = Task_about.objects.get(id = task_id)
	request.user.task_about_set.add(task)
	return redirect('home')