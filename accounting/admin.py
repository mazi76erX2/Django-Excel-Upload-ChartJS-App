from django.contrib import admin
from .models import Accounting


@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    pass
