from django.shortcuts import render
from .models import Wedding, Other, List_of_service
from contact.models import Contact, Instagram, FollowOnSocial
# Create your views here.
def service(request):
    wedding = Wedding.objects.first()
    other = Other.objects.first()
    contact = Contact.objects.first()
    list = List_of_service.objects.all()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()
    content = {
        'wedding': wedding,
        'other': other,
        'list':list,
        'contact': contact,
        'instagram': instagram,
        'social': social
    }
    return render (request, 'services.html',{'content': content})