from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin
from myapp.models import Account

# Register your models here.

TokenAdmin.raw_id_fields = ['user']

admin.site.register([
    Account
])
