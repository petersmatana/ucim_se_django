from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template


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


def template(request):
    t = get_template('example.html')
    context = {
        'jak_to_funguje': 'dobry',
    }

    if 'q' in request.GET:
        context['q'] = request.GET['q']

    c = Context(context)
    return HttpResponse(t.render(c))


def _url_page_template():
    template_string = """request.path() = {{ request_path }}
    <br>
    request.get_host() = {{ request_gethost }}
    <br>
    request.get_full_path() = {{ full_path }}
    <br>
    request.is_secure() = {{ request_is_secured }}
    <br>
    request.META = {{ request_meta }}
    """
    return template_string


def url_page(request):
    t = Template(_url_page_template())
    context = {
        'request_path': request.path,
        'request_gethost': request.get_host(),
        'full_path': request.get_full_path(),
        'request_is_secured': request.is_secure(),
        'request_meta': request.META,
    }
    c = Context(context)
    return HttpResponse(t.render(c))
