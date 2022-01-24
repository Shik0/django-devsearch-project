from django.forms import ModelForm
from .views import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link','source_link', 'tags']