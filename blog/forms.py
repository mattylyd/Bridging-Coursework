from django import forms
from django.forms import DateInput

from .models import Post

class PostForm(forms.ModelForm):
    forms.ChoiceField(choices=[("Achievements","Achievements"),("Education", "Education"),("Work Experience","Work Experience")], required=True)
    class Meta:
        model = Post
        fields = ('tag', 'title', 'text', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }