from django import template
import hashlib
register = template.Library()


@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)


@register.filter(name='md5')
def md5_string(value):
    return hashlib.md5(str(value).encode('utf-8')).hexdigest()
