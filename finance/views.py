from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import ChargeForm,AccountForm
from .models import Charge, Account,Profile


def Main(request):
	return render(request, 'root.html',{'info': "Start page"})
def UserRegister(FormView):
	pass	
def UserLogin():
	pass
def UserLogout():
	pass
def ProfileEdit(request):
	profile = Profile.objects.get_or_create(user=request.user)
	
	return render(request, 'profile.html',{'info': "Profile"})
	
def AccountList(request):
	Profile = get_object_or_404(Profile, user = request.user)
	#Profile.account_set.all()
	return render (request,'account.html',{'form': nameacc})

def Account(request,nameacc):
	return render(request, 'account.html',{'name': nameacc})

def AccountStat():
	pass
def AccountReport():
	pass
def AccountCreate(request):
	profile = get_object_or_404(Profile, user = request.user)
	if request.method == 'POST':

		form = AccountForm(request.POST)
		print(1)
		if form.is_valid():
			print(2)
			a = form.save(commit=False)
			print(3)
			a.account = profile
			print(4)
			a.accountNumber = a.id
			print(5)
			a.save()
			print(6)
			return redirect('Account', nameacc = a.name)
			
	else:
		form = AccountForm()
	return render(request, 'account_create.html',{'form': form})
	
	
			
def AccountEdit():
	pass
def AccountDelete(request,nameacc):
		account = Account.objects.get(profile__user=request.user)
		account.delete()
		return render(request, 'profile.html',{'info': "Profile"}) 
def ChargeCreate():
	pass
def ChargeEdit():
	pass
def ChargeDelete():
	pass
def UserList():
	pass
def UserEdit():
	pass	
def UserDelete():
	pass

























































'''

if request.method == 'POST':
			form = AccountForm(request.POST)
			if form.is_valid():
				Account = form.save(commit = False)
				Account.account = get_object_or_404(Profile, user = request.user)
				Account.accountNumber = Account.id
				Account.save()
				return redirect('Account', nameacc = Account.name)
				
	else:
		form = AccountForm()
	return render(request, 'account_create.html',{'form': form})
			


def root(request):
	for val in Account.objects.all():
		print(val.name)
	#Account.objects.all().delete()
	return render(request, 'root.html',{'info': "Start page"})
def charges(request):
	if request.method == 'POST':
		#a = Charge.objects.get(pk=1)
		form = ChargeForm(request.POST)
		info = ''
		if form.is_valid():
			info = 'ф'
			value = form.save()
			for val in Charge.objects.all():
				print(val.value)
				

		return render(request, 'charges.html',{'info': info})

	else:
		info = ''
		form = ChargeForm()
	return render(request, 'charges.html',{'info': info})


def success(request,nameacc):
	account = get_object_or_404(Account, name = nameacc)
	return render(request, 
					'success.html',
					{'info':'Account   '+account.name+'  succesfully create!'
					})

# urlpattern - url(r'^/charges/(?P<pk>\d+)/$', views.charge_view, name='charge_view')

# template (charge.html):
## {{ charge.account.name }}<br>
## #{{ charge.pk }}<br>
## {{ charge.value }} RUR<br>

def charge_view(request,nameacc):

	account = get_object_or_404(Account, name = nameacc)
	return render(
		request, 'charge_view.html',
		{'form': account.charges}
	)

# urlpattern - url(r'^/accounts/(?P<name>\d+)/charge_create/$', views.charge_create, name='charge_create')

# template (charges.html)
## <form action="{% url 'charge_create' %}" method="post">
##   {% csrf_token %}
##   {{ form }} <!-- equal <input type="number" name="value"> -->
##   <button type="submit">Create</button>
## </form>
#d#ef account_change(request):
def charge_choose_acc(request):
	if request.method == 'POST':
			form = AccountForm(request.POST)
			if form.is_valid():
				Account = form.save(commit=False)
				return redirect('charge_view', nameacc = Account.name)
				#return redirect('/account/(?P<nameacc>\d)/charge_view/$', nameacc = Account.name)
				#return render(request, 
					#'success.html',
					#{'info':'Account   '+Account.name+'  succesfully create!'
					 
					#})
	else:
		form = AccountForm()
	return render(
			request, 'charge_choose_acc.html',
			{'form': form})

def account_create(request):
	if request.method == 'POST':
			form = AccountForm(request.POST)
			if form.is_valid():
				Account = form.save()
				Account.save()
				
				return redirect('success', nameacc = Account.name)
				#return redirect('/account/(?P<nameacc>\d)/charge_view/$', nameacc = Account.name)
				#return render(request, 
					#'success.html',
					#{'info':'Account   '+Account.name+'  succesfully create!'
					 
					#})
	else:
		form = AccountForm()
	return render(
			request, 'account_create.html',
			{'form': form})
#
def charge_create(request, nameacc):
	account = get_object_or_404(Account, name=nameacc)
	if request.method == 'POST':
		form = ChargeForm(request.POST)
		if form.is_valid():
			new_charge = form.save(commit=False)
			new_charge.account = account
			new_charge.save()
			return redirect('charge_view', nameacc )#= nameacc)
	else:
		form = ChargeForm()
	return render(
		request, 'charge_create.html',
		{'form': form}
	)'''
