from django.forms import ModelForm
from .models import biaoge
from .models import images

class SquirrelForm(ModelForm):
    class Meta:
        model = biaoge
        fields = '__all__'

class SquirrelImages(ModelForm):
    class Meta:
        model = images
        fields = '__all__'
