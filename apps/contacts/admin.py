from django.contrib import admin
from apps.contacts.models import Contacts,Contact_detail

# Register your models here.
admin.site.register(Contacts)
admin.site.register(Contact_detail)
