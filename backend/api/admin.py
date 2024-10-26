from django.contrib import admin
from .models import Contributor, Charity, Donation

# Register your models here.

admin.site.register(Contributor)
admin.site.register(Charity)
admin.site.register(Donation)