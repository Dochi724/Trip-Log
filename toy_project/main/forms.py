from django import forms
from django.db.models import fields
from .models import Write, Comment  # 나중에 작업할 때 comments 추가


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='')

    class Meta:
        model = Comment
        fields = ['content']
    
    