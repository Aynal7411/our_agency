from django.contrib import admin
from .models import Skill, Offer_list, Employe

admin.site.register(Skill)  # Register the Skill model in the admin interface
# Register your models here.
admin.site.register(Offer_list)  # Register the Offer_list model in the admin interface
admin.site.register(Employe)  # Register the Employe model in the admin interface