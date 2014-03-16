# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from playground.blog.models import Category
import datetime


register = template.Library()

@register.filter
@stringfilter
def replace_whitespace(value, arg):
    return arg.join(value.split())

"""
Napisz filtr zliczacz powtórzeń znaku podanego w template.
"""



# @register.tag
# def current_time(parser, token):
#     try:
#         # split_contents() knows not to split quoted strings.
#         tag_name, format_string = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
#     if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
#         raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
#     return CurrentTimeNode(format_string[1:-1]) #ścinamy quoty

# class CurrentTimeNode(template.Node):
#     def __init__(self, format_string):
#         self.format_string = format_string
#     def render(self, context):
#         return datetime.datetime.now().strftime(self.format_string)


@register.tag
def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token() #tag endupper nie zostanie usunięty bez tego polecenia - spowoduje to template error
    return UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

register.simple_tag(lambda x: x - 1, name='minusone')

@register.inclusion_tag("template_stuff/categories.html")
def categories():
    categories = Category.objects.all()
    return locals()

"""
Zadania:
- przerobić tag categories tak by pokazywał wszystkie posty dla danej kategorii.
- napisz tag change_to_trolol, który zmieni cały tekst pomiędzy tym tagiem na trololol gdzie lol ma się powtarzać tyle razy ile jest słów w tym tekście.
- napisz prosty tag który potęguje daną liczbę do potęgi podanej w templatetagu
np. {% pow post.count 4 %}
"""

