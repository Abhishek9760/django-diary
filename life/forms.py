from django import forms

from .models import DiaryModel

class DiaryForm(forms.ModelForm):
	class Meta:
		model = DiaryModel
		fields = ('your_day',)
