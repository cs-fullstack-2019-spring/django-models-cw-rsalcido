from django.contrib import admin

# Register your models here.
#cluster both together to add to the admin account
from .models import Dog
from .models import Account


admin.site.register(Dog)
admin.site.register(Account)