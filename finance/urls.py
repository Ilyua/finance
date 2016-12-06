from django.conf.urls import url
from finance  import views 

urlpatterns = [
	#url(r'^$', views.Main,name = 'Main'),
	 url(r'^register/$', views.RegisterFormView.as_view()),
	'''url(r'^account_create/account/(?P<nameacc>\w+)/charge_view/$', views.charge_view, name='charge_view'),
	url(r'^account_create/$', views.account_create,name = 'account_create'),
	url(r'^account_create/account/(?P<nameacc>\w+)/success/$', views.success, name='success'),
	url(r'^charge_choose_acc/$', views.charge_choose_acc, name='charge_choose_acc'),
	url(r'^charge_choose_acc/account/(?P<nameacc>\w+)/charge_view/$', views.charge_view, name='charge_view'),
	url(r'^charge_choose_acc/account/(?P<nameacc>\w+)/charge_view/charge_create/$', views.charge_create, name='charge_create'),'''
]