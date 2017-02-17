from django.http import HttpResponse
from django.template import Template, Context


def _home_page_template():
    template_string = """tohle je <b>{{ name }}</b> templejta<br><br>
a ted nejaky polozky:
<ul>{% for item in items %}
<li>{{ item }}</li>
{% endfor %}</ul>
"""
    return template_string


def home_page(request):
    t = Template(_home_page_template())
    context = {
        'name': 'smontyho',
        'items': [1, 2, 3, 4],
    }
    c = Context(context)
    return HttpResponse(t.render(c))


def hello(request):
    t = Template(_home_page_template())
    context = {
        'name': 'Django Rainhard',
        'items': ['e', 'h', 'g', 'd', 'a', 'e'],
    }
    c = Context(context)
    return HttpResponse(t.render(c))

