from django.shortcuts import render
from .models import GalleryItem
from django.conf import settings
from django.http import JsonResponse
from .forms import ContactForm
from django.contrib import messages

import os

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils.html import format_html


def home(request): 
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Send an email to sales@epoxy.com for a new submission
            send_contact_email(contact)

            messages.success(request, "Thank you for reaching out!")
        else:
            messages.error(request, form.errors)

        messages.success(request, "Thank you for reaching out!")

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

    form = ContactForm()

    context = {
        'form': form,

        'image_files': image_files,
        'static_url': settings.STATIC_URL + 'images/' + 'colors/',
        'gallery_items': gallery_items,
    }

    return render(request, f"{ language }/home.html", context)


def contact(request):
    language = request.session.get(settings.MY_LANGUAGE_COOKIE_NAME, 'en')

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()

            # Send an email to sales@epoxy.com for a new submission
            send_contact_email(contact)

            messages.success(request, "Thank you for reaching out!")
        else:
            messages.error(request, form.errors)

    form = ContactForm()

    context = {
        'form': form,
    }
    
    return render(request, f"{ language }/contact.html", context)


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


def send_contact_email(contact):
    # Properly formatted HTML content with a table
    html_content = format_html("""
    <html>
    <body style="color: #444444;">
        <h2>New Submission on Epoxy214.com</h2>
        <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse;">
            <tr>
                <th style="text-align: left;">Full Name</th>
                <td>{}</td>
            </tr>
            <tr>
                <th style="text-align: left;">Email</th>
                <td>{}</td>
            </tr>
            <tr>
                <th style="text-align: left;">Phone</th>
                <td>{}</td>
            </tr>
            <tr>
                <th style="text-align: left;">Preferred Contact Method</th>
                <td>{}</td>
            </tr>
            <tr>
                <th style="text-align: left;">Message</th>
                <td>{}</td>
            </tr>
        </table>
    </body>
    </html>
    """, contact.full_name, contact.email, contact.phone, contact.get_contact_method_display(), contact.message)

    email = EmailMessage(
        'New submission on Epoxy214.com',
        html_content,
        'sales@epoxy214.com',  # From email
        ['sales@epoxy214.com'],  # Recipient email
    )

    email.content_subtype = "html"  # To send HTML content

    # Attach the uploaded file
    if contact.image:
        email.attach_file(contact.image.path)

    # Send the email
    email.send()


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
    

