from django.forms import ModelForm
from .models import myapp


class TodoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = myapp