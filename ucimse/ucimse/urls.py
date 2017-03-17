from django.conf.urls import url
# from django.contrib import admin
from ucimse.views import hello, home_page, url_page, template
from aplikace.views import get_name, form_result, custom_form

urlpatterns = [
    url(r'^$', home_page),
    # url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello),
    url(r'^template', template),
    url(r'^urlpage/', url_page),

    # forms...
    url(r'get_name/', get_name),
    url(r'form_result/', form_result),
    url(r'custom_form/', custom_form),
]
