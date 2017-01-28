from __future__ import unicode_literals

import datetime
from django.db import models
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE
from django.utils import timezone
from django.forms import ModelForm, TextInput
from django import forms

class Notes(models.Model):
    note_title = models.TextField(verbose_name = 'Title', null=True)
    note_instructor = models.TextField(verbose_name = 'Instructor', null=True)
    note_date = models.DateTimeField(verbose_name = 'Session Date')

    note_text = models.TextField(verbose_name = 'Description')
    note_vid = models.CharField(max_length=100, verbose_name = 'Video Link', null=True)

    def __str__(self):
        return "%s - %s - %s" % (self.note_title, self.note_date, self.note_instructor)

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['note_title', 'note_instructor', 'note_date', 'note_vid', 'note_text']
        widgets = {
            'note_title': TextInput(),
            'note_instructor': TextInput(),
        }
