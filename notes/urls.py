from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<note_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.create_note, name='create'),
    url(r'^edit_note/(?P<note_id>[0-9]+)/', views.edit_note, name='edit'),
    url(r'^delete_note/(?P<note_id>[0-9]+)/', views.delete_note, name='delete'),
    
]

