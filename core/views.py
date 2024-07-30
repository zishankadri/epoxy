from django.shortcuts import render
from .models import GalleryItem
from django.conf import settings
from django.http import JsonResponse

import os


def home(request): 
    # language = request.COOKIES.get('language', 'en')
    # if not language: language="en"
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')

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

    return render(request, f"{ language }/home.html", context)


def contact(request):
    # language = request.COOKIES.get('language', 'en')
    # if not language: language="en"
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')
    
    return render(request, f"{ language }/contact.html")


def gallery(request):
    # language = request.COOKIES.get('language', 'en')
    # if not language: language="en"
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')

    gallery_items = GalleryItem.objects.all().order_by('rank')

    context = {
        'gallery_items': gallery_items,
    }

    return render(request, f"{ language }/gallery.html", context)


def about_us(request):
    # language = request.COOKIES.get('language', 'en')
    # if not language: language="en"
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')

    return render(request, f"{ language }/about_us.html")


def check_media(request, item_id, origin):
    language = request.COOKIES.get('language', 'en')
    if not language: language="en"

    item = GalleryItem.objects.get(id=item_id)

    if origin == "home":
        origin = "/#gallery"
    elif origin == "gallery":
        origin = "/gallery/"

    context = {
        "item": item,
        "origin": origin
    }
    # prefered_language = #sessions ...
    # return render(request, f"{ prefered_language }/check_media.html", context)
    return render(request, f"{ language }/check_media.html", context)


# APIs
def change_lang(request):
    lang_code = request.GET.get('lang_code')

    if lang_code and lang_code in settings.MY_LANGUAGES:
        response = JsonResponse({"message": "Language preference set"})
        # response.set_cookie(settings.MY_LANGUAGE_COOKIE_NAME, lang_code, max_age=365*24*60*60)
        request.session[settings.MY_LANGUAGE_COOKIE_NAME] = lang_code

        return response
    else:
        return JsonResponse({"error": f"Invalid language code {lang_code} "}, status=400)