import datetime
from django import forms
from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError,MultipleObjectsReturned 
from django.forms import ModelForm
from .models import Charge,Account,Profile




class ProfileFrom(ModelForm):
	class Meta:
		model = Profile
		fields = ['user']

class ChargeForm(ModelForm):
	class Meta:
		model = Charge
		fields = ['amount','transactedAt']	

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = ['name']#,'account','accountNumber']
		
	def clean_name(self):
		temp = self.cleaned_data.get('name')
		#try:
		#	accs = Account.objects.filter(account__user=self.request.user)
		#	a = accs.get(name = nameacc)
		#except MultipleObjectsReturned :
		#	raise ValidationError("Такой аккаунт уже создавался в вашем профиле")

		return temp