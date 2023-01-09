from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task_about
from django.views.decorators.http import require_http_methods

def index(request):
	obj = Task_about.objects.all()
	context = {
		'obj_list': obj,
		'title': 'Главная страница'
	}
	print(obj)
	return render(request, 'tasker/index.html', context)

@require_http_methods(['POST'])
def add(request):
	title = request.POST['title']
	task = Task_about(title = title)
	task.save()
	return redirect('index')

def update(request, task_id):
	task = Task_about.objects.get(id = task_id)
	task.is_complite = not(task.is_complite)
	task.save()
	return redirect('index')

def delete(request, task_id):
	task = Task_about.objects.get(id = task_id)
	task.delete()
	return redirect('index')