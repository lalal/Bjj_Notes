from __future__ import unicode_literals

import datetime
from django.db import models
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE
from django.utils import timezone
from django.forms import ModelForm
from django import forms

class Notes(models.Model):
    note_text = models.TextField()
    note_date = models.DateTimeField('Session Date')
    note_vid = models.CharField(max_length=100)

    def __str__(self):
        return self.note_text

class NotesForm(ModelForm):

    #note_text = forms.CharField(widget=TinyMCE())
    note_date = forms.DateField()
    class Meta:
        model = Notes
        fields = ['note_text', 'note_date', 'note_vid']
