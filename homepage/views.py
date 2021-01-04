from django.shortcuts import render
from about.models import About
from .models import Top_photo, NoticeBoard, Video
from service.models import List_of_service
from contact.models import Contact, Instagram, FollowOnSocial
# Create your views here.
def index(request):
    about = About.objects.first()
    top = Top_photo.objects.first()
    list = List_of_service.objects.all()
    contact = Contact.objects.first()
    instagram = Instagram.objects.all()
    social = FollowOnSocial.objects.first()
    notice = NoticeBoard.objects.all() 
    video = Video.objects.first()
    content = {
        'about': about,
        'top': top,
        'list': list,
        'contact': contact,
        'instagram': instagram,
        'social': social,
        'notice': notice,
        'video':  video
    }
    return render (request, 'index.html', {'content': content})