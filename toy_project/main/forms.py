from django import forms
from django.db.models import fields
from django import forms
from .models import Write, Comment  # 나중에 작업할 때 comments 추가


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ('title', 'contents', 'images')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='')

    class Meta:
        model = Comment
        fields = ['content']
