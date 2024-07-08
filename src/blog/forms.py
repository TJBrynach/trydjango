from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        fields = [
            'title',
            'content',
            'active',
        ]