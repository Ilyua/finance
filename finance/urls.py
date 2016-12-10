from django.conf.urls import url
from finance  import views 

urlpatterns = [
	url(r'^$', views.Main,name = 'Main'),
	 
	
]