from django.http import HttpResponse


def home_page(request):
    return HttpResponse('home page')

def hello(request):
    return HttpResponse('Hello Smonty! from Django.')
