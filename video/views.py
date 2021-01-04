from django.shortcuts import render
from service.models import List_of_service
from contact.models import Contact, Instagram, FollowOnSocial
from .models import Upload_video
# Create your views here.
def video(request):
    list = List_of_service.objects.all()
    contact = Contact.objects.first()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()
    video = Upload_video.objects.all()
    content = {
        'list': list,
        'contact': contact,
        'instagram': instagram,
        'social': social,
        'video': video
    }
    return render(request, 'video.html', {'content': content})