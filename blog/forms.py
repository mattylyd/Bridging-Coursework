from django import forms
from django.forms import DateTimeInput

from .models import CV,Blog

class CVForm(forms.ModelForm):
    forms.ChoiceField(choices=[("About Me","About Me"),("Achievements","Achievements"),("Education", "Education"),("Work Experience","Work Experience")], required=True)
    # start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={}))
    # end_date = forms.DateField(widget=forms.widgets.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = CV
        fields = ('tag', 'title', 'text', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
            'end_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }
        # widgets = {
        #     'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        #     'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #
        # }

class BlogForm(forms.ModelForm):
    # start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={}))
    # end_date = forms.DateField(widget=forms.widgets.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = Blog
        fields = ( 'title', 'text')


        # widgets = {
        #     'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        #     'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #
        # }
