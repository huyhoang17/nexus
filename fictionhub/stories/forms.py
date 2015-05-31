from django.forms import ModelForm
from django import forms

from .models import Story, Chapter, Comment


class StoryForm(ModelForm):
    class Meta:
        model = Story
        exclude = ['author', 'slug', 'score', 'published',]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'})
        }

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        exclude = ['slug', 'score', 'published', 'story', 'number',]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'story', 'parent', 'slug', 'score', 'published',] 
        
