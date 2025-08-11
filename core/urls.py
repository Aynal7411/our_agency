from django.urls import path
from .views import home, offer_page, about_page, contact_page, career_list


urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('offer/', offer_page, name='offer'),  # Offer page URL
    path('about/', about_page, name='about'),  # About page URL
    path('contact/', contact_page, name='contact'),  # Contact page URL
    path('career/', career_list, name='career_list'),  # Career list URL
]