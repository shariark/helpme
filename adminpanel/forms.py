from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib.auth.models import User
from post.models import post



class edit_post(forms.ModelForm):
    status=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    

    class Meta:
        model = post
        fields = ('status',)

    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)