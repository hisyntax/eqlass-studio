from django.shortcuts import render
from .models import Photo
from service.models import List_of_service
from contact.models import Contact, Instagram, FollowOnSocial
# Create your views here.
def photo(request):
    photo = Photo.objects.all()
    list = List_of_service.objects.all()
    contact = Contact.objects.first()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()
    content = {
        'photo':  photo,
        'list': list,
        'contact': contact,
        'instagram': instagram,
        'social': social
    }
    return render (request, 'photo.html', {'content': content})