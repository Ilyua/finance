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
	accs = Account.objects.filter(account__user=request.user)
	a.objects()
	return render (request,'account.html',{'form': nameacc})

def Acc(request,nameacc):#был конфликт с названием модели
	#p = get_object_or_404(Profile, user = request.user)
	accs = Account.objects.filter(account__user=request.user)
	a = get_object_or_404(accs, name = nameacc)
		#a = p.account_set.all().get(name = nameacc)
	
	
	
	return render(request, 'account.html',{'name': nameacc})

def AccountStat(request):
	pass
def AccountReport():
	pass
def AccountCreate(request):
	profile = get_object_or_404(Profile, user = request.user)
	if request.method == 'POST':

		form = AccountForm(request.POST)
		
		if form.is_valid():
			
			a = form.save(commit=False)
			
			a.account = profile
			
			a.accountNumber = a.id
			
			a.save()
			#print(type(a.name))
			return redirect('Account', nameacc = a.name)

	else:
		form = AccountForm()
	return render(request, 'account_create.html',{'form': form})
	
	
			
def AccountEdit(request,nameacc):
	accs = Account.objects.filter(account__user=request.user)
	a = get_object_or_404(accs, name = nameacc)
	if request.method == 'POST':

		form = AccountForm(request.POST)
		
		if form.is_valid():
			
			f = form.save(commit=False)
			a.name = f.name
			a.save()
			#a.account = profile
			
			#a.accountNumber = a.id#не знаю как лучше
			
			
			#print(type(a.name))
			return redirect('Account', nameacc = a.name)

	else:
		form = AccountForm()
	return render(request, 'account_edit.html',{'form': form})

def AccountDelete(request,nameacc):
		p = get_object_or_404(Profile, user = request.user)
		a = p.account_set.all().get(name = nameacc)

		#Account.objects.get(profile__user=request.user)
		#a = account.objects.get(name = nameacc)
		a.delete()
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
