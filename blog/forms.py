from django import forms
from .models import Category, Post
from mptt.fields import TreeNodeChoiceField

class PostWriteForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all(), level_indicator='-')

    class Meta:
        model = Post
        fields = [
            'subject',
            'content',
            'category',
        ]
