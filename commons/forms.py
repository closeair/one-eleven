from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from django.forms import extras
from .models import Document


class DocumentForm(forms.ModelForm):
  uploaded_file = forms.FileField(widget=AdminFileWidget, label='File to be uploaded')
  class Meta:
    model = Document
    labels = {
      'name': 'What is this file being uploaded for?',
    }
    fields = ['name', 'uploaded_file',]