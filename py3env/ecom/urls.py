#import
from django.conf.urls import url, patterns, include
from . import views
#from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


#Have to make url entry for myapp just over here.
urlpatterns = [
# Home page is renamed as about page.
#   url(r'^home$', TemplateView.as_view(template_name='home.html'), name="home"),
    #Favicon
    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
            permanent=False),
        name="favicon"
    ),
    url(r'^$', views.product_list, name='product_list'),
]

