from .models import *
 
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        tasks = Task_about.objects.all()
        return context