from django.shortcuts import render
from .models import Contact , Instagram, FollowOnSocial
from service.models import List_of_service
# Create your views here.
def contact(request):
    contact = Contact.objects.first()
    list = List_of_service.objects.all()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()

    content = {
        'contact': contact,
        'list': list,
        'instagram': instagram,
        'social': social
    }
    return render (request, 'contact.html', {'content': content})
