from django.urls import path
from django.urls import re_path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('about_us/', views.about_us, name="about_us"),
    path('check_media/<str:item_id>/<str:origin>', views.check_media, name="check_media"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)