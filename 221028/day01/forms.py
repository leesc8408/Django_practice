from django import forms
from .models import Day01


class artsForm(forms.ModelForm):
    class Meta:
        model = Day01
        fields = "__all__"
        labels = {
            "title": "제목",
            "content": "내용",
        }
