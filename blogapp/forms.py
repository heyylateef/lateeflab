from django import forms
from django.forms import ModelForm
from .models import Blogpost

class DateInput(forms.DateInput): #Defines class that'll render a datepicker on HTML form
    input_type = 'date'


class CreatePostForm(ModelForm):
    model = Blogpost
    fields = ['title', 'content', 'status']