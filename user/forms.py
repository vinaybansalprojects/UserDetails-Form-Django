from django import forms
from .models import Snippet
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
import datetime


class SnippetForm(forms.ModelForm):
	birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),initial=datetime.date.today)
	def clean_birthday(self):
		dob = self.cleaned_data['birthday']
		today = date.today()
		if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
			raise forms.ValidationError('Must be at least 18 years old to register')
		return dob
	class Meta:
		model = Snippet
		fields = ('name','birthday','email','phone')