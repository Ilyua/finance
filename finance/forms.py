import datetime
from django import forms
from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Charge,Account,Profile



class ProfileFrom(ModelForm):
	class Meta:
		model = Profile
		fields = ['user']

class ChargeForm(ModelForm):
	class Meta:
		model = Charge
		fields = ['account','transactedAt','amount']	

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = ['name']#,'account','accountNumber']
		
	def clean_name(self):
		temp = self.cleaned_data.get('name')
		return temp