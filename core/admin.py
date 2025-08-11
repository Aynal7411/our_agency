from django.contrib import admin
from .models import Skill, Offer_list, Employe, Career

admin.site.register(Skill)       # Register the Skill model
admin.site.register(Offer_list)  # Register the Offer_list model
admin.site.register(Employe)     # Register the Employe model
admin.site.register(Career)      # Register the Career model
