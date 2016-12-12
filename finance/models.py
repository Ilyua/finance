

from django.conf import settings

from django.db import models
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)#?
	
class Account(models.Model):
	name = models.CharField(max_length=200)
	account = models.ForeignKey(Profile)#,related_name='accounts')#, on_delete=models.CASCADE)#тут сливу навешивают
	#accountNumber =  models.IntegerField()
  
class Charge(models.Model):
	account = models.ForeignKey(Account, related_name='charges') # DB -> account_id
	transactedAt = models.DateTimeField(default=timezone.now)
	amount = models.DecimalField(max_digits=5, decimal_places=2)

