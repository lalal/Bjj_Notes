from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.notes_list, name='list'),
    url(r'^new$', views.notes_create, name='create'),
    url(r'^edit/(?P<pk>\d+)$', views.notes_update, name='update'),
    url(r'^delete/(?P<pk>\d+)$', views.notes_delete, name='delete'),
    url(r'^(?P<pk>\d+)', views.notes_detail, name='detail'),
]

