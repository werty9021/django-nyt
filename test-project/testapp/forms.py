from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms

from . import models

class TestModelForm(forms.ModelForm):

    class Meta:
        model = models.TestModel
        fields = ('name',)
