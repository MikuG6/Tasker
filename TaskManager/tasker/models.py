from django.db import models
from django import forms
from django.contrib.auth.models import User

class Task_about(models.Model):
	title = models.CharField('Название задания', max_length = 100)
	is_complite = models.BooleanField('Завершено', default = False)
	user = models.ManyToManyField(User)

	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задания'

	def __str__(self):
		return self.title

# class Task_user(models.Model):
# 	tasks = models.ForeignKey(Task_about, on_delete = models.CASCADE)
# 	users = models.ForeignKey(User, on_delete = models.CASCADE)


# class User(models.Model):
# 	nickname = models.CharField('Имя пользователя', max_length = 100)
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User