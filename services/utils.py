from django import forms
from django.utils.safestring import mark_safe
from users_management.models import scheme
from users_management.configuration.config import json_scheme
import random


# GET THE JSON_FIELDS
def _get_scheme(user_profile, ret=False):
    qry1 = scheme.objects.filter(code=user_profile)
    return qry1 if ret else qry1.get().data if qry1 else {}



# UPDATE ATTRIBUTE TYPE DICT
def _update_attr_dict(qry, data_finish, attr, combine=True):
    update_data = qry.get()
    if combine:
        update_data.combine_data(attr, data_finish)
    else:
        update_data.set_data(attr, data_finish)
    update_data.save()


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

    type_structure = json_scheme.get(type_field, json_scheme.get("string").get("structure")).get("structure")
    help = mark_safe(field.get('help')) if field.get('help') else None


    scheme_field = {'label': field.get('label'),
                    'initial': field.get('initial'),
                    'help_text': help,
                    'required': True if field.get('required') else False}

    if type_field != "select":
        widget = getattr(forms, type_structure.get('input'))(
            attrs={'placeholder': field.get('placeholder')})
        scheme_field['widget'] = widget
    else:
        scheme_field['choices'] = field.get('option', [])

    return getattr(forms, type_structure.get('field'))(**scheme_field)


def _alpha_num(num):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(num))