from django import forms
from django.utils.safestring import mark_safe
from users_management.models import scheme
import random


# GET THE JSON_FIELDS
def _get_scheme(user_profile):
    qry1 = scheme.objects.filter(code=user_profile)
    return qry1.get().data if qry1 else {}


# UPDATE ATTRIBUTE TYPE DICT
def _update_attr_dict(qry, data_finish, attr):
    update_user = qry.get()
    getattr(update_user, attr).update(data_finish)
    update_user.save()


# RETURN ONLY VALUES CONTENT IN SCHEME
def _check_field_value(fields, values):
    result = {}
    for field in fields:
        name = field.get('name')
        if name in values.keys():
            result[name] = values.get(name)
    return result


# GENERATE FIELDS FROM INPUT
def _scheme_to_form(field):
    # IF FIELD NOT CONTAINT VALUE, THE TYPE DEFAULT IS STRING
    type_field = field.get("type", "string").lower()

    # STRUCTURE FOR DJANGO FORM
    types = {"int": {"field": "IntegerField", "input": "TextInput"},
             "boolean": {"field": "BooleanField", "input": "CheckboxInput"},
             "select": {"field": "ChoiceField", "input": "option"},
             "float": {"field": "FloatField", "input": "TextInput"},
             "time": {"field": "TimeField", "input": "TimeInput"},
             "date": {"field": "DateField", "input": "DateInput"},
             "datetime": {"field": "DateTimeField", "input": "DateTimeInput"},
             "long_string": {"field": "CharField", "input": "Textarea"},
             "string": {"field": "CharField", "input": "TextInput"},
             }

    type_structure = types.get(type_field, types.get("string"))
    help_text = mark_safe(field.get('help_text')) if field.get('help') else None


    scheme_field = {'label': field.get('label'),
                    'initial': field.get('initial'),
                    'help_text': help_text,
                    'required': False if field.get('not_required') else True}

    if type_field != "select":
        widget = getattr(forms, type_structure.get('input'))(
            attrs={'placeholder': field['placeholder']})
        scheme_field['widget'] = widget
    else:
        scheme_field['choices'] = field.get('option', [])

    return getattr(forms, type_structure.get('field'))(**scheme_field)


def _alpha_num(num):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(num))