from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter document title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your content...'}),
        }
