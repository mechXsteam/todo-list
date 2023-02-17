from django import forms

from .models import TodoItem


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title']
        labels = {'title': ''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
