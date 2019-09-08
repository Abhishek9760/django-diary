from django import forms
from django.db import models

from .models import DiaryModel

class DiaryForm(forms.ModelForm):
	class Meta:
		model = DiaryModel
		fields = ('your_day', 'adventure')
		widgets = {
            'your_day': forms.Textarea(attrs={'placeholder': 'Write what did you do today!', 'class': 'editable medium-editor-textarea extra'}),
            'adventure': forms.Textarea(attrs={'placeholder': 'Any adventure you experience? otherwise leave it!', 'class': 'editable medium-editor-textarea extra'}),
        }
