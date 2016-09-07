# -*- encoding: utf-8 -*-

from django import forms

from services.utils import _scheme_to_form
from .models import user


class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}

class DinamicForm(forms.Form):
    def __init__(self, fields, initial, *args, **kwargs):
        super(DinamicForm, self).__init__(*args, **kwargs)
        # GENERATE FORMS WITH INITIAL VALUE
        for field in fields:
            field.update({'initial': initial.get(field['name'])})
            self.fields[field['name']] = _scheme_to_form(field)