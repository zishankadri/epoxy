from django import template

from django.template import Template, Context
register = template.Library()

import magic

@register.filter(name='get_file_type')
def get_file_type(filename):
    print(type(filename))

    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filename)

    print("file_type", file_type)

    if file_type.startswith('video'):
        return "video"
    
    elif file_type.startswith('image'):
        return "image"

@register.filter(name='split_dot')
def split_dot(value):
    return value.rsplit('.', 1)[1]

