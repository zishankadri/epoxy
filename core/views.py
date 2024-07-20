from django.shortcuts import render
from .models import GalleryItem
from django.conf import settings

import os


def home(request): 
    static_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'colors')
    image_files = []

    for filename in os.listdir(static_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            name, extension = os.path.splitext(filename)
            if ',' in name:
                main_name, code = name.split(',', 1)
                image_files.append({'main_name': main_name, 'code': code, 'url': filename})
            else:
                main_name, code = name, ''

    gallery_items = GalleryItem.objects.all().order_by('rank')[0:6]
    context = {
        'image_files': image_files,
        'static_url': settings.STATIC_URL + 'images/' + 'colors/',
        'gallery_items': gallery_items,
    }

    return render(request, "home.html", context)


def contact(request):
    return render(request, "contact.html")


def gallery(request):
    gallery_items = GalleryItem.objects.all().order_by('rank')

    context = {
        'gallery_items': gallery_items,
    }

    return render(request, "gallery.html", context)


def about_us(request):
    return render(request, "about_us.html")


def check_media(request, item_id, origin):
    item = GalleryItem.objects.get(id=item_id)

    if origin == "home":
        origin = "/#gallery"
    elif origin == "gallery":
        origin = "/gallery/"

    context = {
        "item": item,
        "origin": origin
    }
    
    return render(request, "check_media.html", context)