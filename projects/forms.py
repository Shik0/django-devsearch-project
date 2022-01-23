from django.forms import ModelForm
from .views import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'