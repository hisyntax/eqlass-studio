from django.shortcuts import render
from .models import About
from service.models import List_of_service
from contact.models import Contact, Instagram, FollowOnSocial
# Create your views here.
def about(request):
    about = About.objects.first()
    list = List_of_service.objects.all()
    contact = Contact.objects.first()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()
    content = {
        'about': about,
        'list': list,
        'contact': contact,
        'instagram': instagram,
        'social': social
    }
    return render (request, 'about.html', {'content':content})