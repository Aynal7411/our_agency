from django.shortcuts import render
from .models import Skill, Offer_list, Employe
# Create your views here.
def home(request):
    skill_list=Skill.objects.all()
    return render(request, 'core/home.html',{'skill_list':skill_list})

def offer_page(request):
    offers=Offer_list.objects.all()
    return render(request, 'core/offer.html', {'offers': offers})

def about_page(request):
    employees = Employe.objects.all()
    return render(request, 'core/about.html', {'employees': employees})
    

def contact_page(request):
    return render(request, 'core/contact.html')
from .models import Career

def career_list(request):
    careers = Career.objects.filter(is_active=True).order_by('-posted_date')
    return render(request, 'core/career_list.html', {'careers': careers})