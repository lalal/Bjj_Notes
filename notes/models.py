from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm, TextInput
from django import forms

class Notes(models.Model):
    note_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    note_title = models.TextField(verbose_name = 'Title', null=True)
    note_instructor = models.TextField(verbose_name = 'Instructor', null=True)
    note_date = models.DateTimeField(verbose_name = 'Session Date')

    note_text = models.TextField(verbose_name = 'Description')
    note_vid = models.CharField(max_length=100, verbose_name = 'Video Link', null=True, blank=True)
    note_category = models.CharField(max_length=100, verbose_name = 'Category', null=True)

    def __str__(self):
        return "%s - %s - %s" % (self.note_title, self.note_date, self.note_instructor)

#class Videos(models.Model):
#    video_note = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)
#    video_link = models.TextField(verbose_name = 'Video Link', null=True)
#    video_embed_link = models.TextField(verbose_name = 'Video Embed Link', null=True)
#
#    def __str__(self):
#        return "%s - %s - %s" % (self.video_note, self.video_link, self.video_embed_link)

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['note_title', 'note_instructor', 'note_date', 'note_category', 'note_vid', 'note_text']
        widgets = {
            'note_title': TextInput(attrs={'class': 'form-control'}),
            'note_instructor': TextInput(attrs={'class': 'form-control'}),
            'note_category': TextInput(attrs={'class': 'form-control'}),
            'note_vid': TextInput(attrs={'class': 'form-control'}),
            'note_date': TextInput(attrs={'class': 'form-control'}),
        }

    def clean_note_vid(self):
        data = self.cleaned_data['note_vid']
        if data != '' and not data.startswith('https://www.youtube.com/embed/'):
            raise forms.ValidationError('Not a youtube video, either leave blank or start with \'https://www.youtube.com/embed/\' instead of \'%(data)s\'',
                                  code='invalid', params={'data': data}) 
