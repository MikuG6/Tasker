from django.db import models

class Task_about(models.Model):
	title = models.CharField('Название задания', max_length = 100)
	is_complite = models.BooleanField('Завершено', default = False)

	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задания'

	def __str__(self):
		return self.title
