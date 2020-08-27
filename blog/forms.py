from django import forms
from django.forms import DateInput

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }