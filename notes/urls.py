from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [

    url(r'^$', views.notes_list, name='list'),
    url(r'^new$', views.notes_create, name='create'),
    url(r'^edit/(?P<pk>\d+)$', views.notes_update, name='update'),
    url(r'^delete/(?P<pk>\d+)$', views.notes_delete, name='delete'),
    url(r'^(?P<pk>[0-9]\d+)$', views.notes_detail, name='detail'),


#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<note_id>[0-9]+)/$', views.detail, name='detail'),
#    url(r'^new/$', views.create_note, name='create'),
#    url(r'^edit_note/(?P<note_id>[0-9]+)/', views.edit_note, name='edit'),
#    url(r'^delete_note/(?P<note_id>[0-9]+)/', views.delete_note, name='delete'),
    
]

