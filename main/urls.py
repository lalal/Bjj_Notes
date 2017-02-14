"""
alok_2017_class_tracker URL Configuration
"""

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

import views as home_views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', home_views.home, name='index'), 
    url(r'^contact/', home_views.contact, name='contact'), 
    url(r'^about/', home_views.about, name='about'), 
    url(r'^faq/', home_views.faq, name='faq'), 
    url(r'^notes/', include('notes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^register/', CreateView.as_view(template_name='register.html',
                       form_class=UserCreationForm,
                       success_url='/'), name='register'),
    
]
