from django import forms
from .models import User


class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())
    overview = forms.CharField(widget=forms.Textarea)
    brief_overview = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields =(
            'title',
            'author',
            'overview',
            'brief_overview',
        )