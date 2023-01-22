from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        tasks = Task.objects.all()
        return context