from django.conf.urls import url
from finance  import views 
#from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.Main,name = 'Main'),
	url(r'^accounts/profile/$', views.ProfileEdit,name = 'Profile'),
	url(r'^accounts/profile/account_list/$', views.AccountList,name = 'AccountList'),
	url(r'^accounts/profile/account_create/$',views.AccountCreate,name = 'AccountCreate'),
	url(r'^accounts/profile/account_change/$',views.AccountChange,name = 'AccountChange'),
	url(r'^accounts/profile/(?P<nameacc>\w+)/$',views.Acc ,name = 'Account'),
	url(r'^accounts/profile/(?P<nameacc>\w+)/account_delete/$',views.AccountDelete ,name = 'AccountDelete'),
	url(r'^accounts/profile/(?P<nameacc>\w+)/account_edit/$',views.AccountEdit ,name = 'AccountEdit'),
	url(r'^accounts/profile/(?P<nameacc>\w+)/charge_create/$',views.ChargeCreate ,name = 'ChargeCreate'),



	
]