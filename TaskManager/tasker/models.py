from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
	title = models.CharField("Название задания", max_length=100)
	is_complete = models.BooleanField("Завершено", default=False)
	users = models.ManyToManyField(User, related_name="tasks")

	class Meta:
		verbose_name = "Задание"
		verbose_name_plural = "Задания"

	def __str__(self):
		return self.title
