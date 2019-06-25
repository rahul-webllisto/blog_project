from django import forms
from .models import *

class CreateArticleForm(forms.ModelForm):    
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'write description here'}))

    class Meta:
        model = Article
        fields = ['title', 'description']



class CreateCommentForm(forms.ModelForm):    
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add Comments'}))    

    class Meta:
        model = Comment
        fields = ['text']
