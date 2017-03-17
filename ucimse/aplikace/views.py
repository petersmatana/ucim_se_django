from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import UserForm
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']

            return HttpResponseRedirect('/form_result')
    else:
        form = NameForm()
    return render(request, 'templejta.html', {'form': form})


def form_result(request):
    t = get_template('form_result.html')
    context = {
        'meta': request.META,
    }
    if 'subject' in request.POST:
        context['subject'] = request.POST['subject']
    if 'message' in request.POST:
        context['message'] = request.POST['message']
    c = Context(context)
    return HttpResponse(t.render(c))


def custom_form(request):
    return render(request, 'custom_form.html', {'form': UserForm()})
