# REDIRECT
ROOT_PATH='/'

# FORMS IN DATABASE
def_form = dict(user_profile='user_profile')


# STRUCTURE FOR FORM
option_basic = {'type': 'required', 'name': 'required', 'label': 'optional',
                'placeholder': 'optional', 'help_text': 'optional',
                'required': 'optional'}
option_select = {'type': 'required', 'name': 'required', 'label': 'optional',
                 'placeholder': 'optional', 'required': 'optional',
                 'option': 'required'}

json_scheme = {"int": {"structure": {"field": "IntegerField", "input": "TextInput"},
                       "option": option_basic},
             "boolean": {"structure": {"field": "BooleanField", "input": "CheckboxInput"},
                        "option": option_basic},
             "select": {"structure": {"field": "ChoiceField", "input": "option"},
                        "option": option_basic},
             "float": {"structure": {"field": "FloatField", "input": "TextInput"},
                        "option": option_basic},
             "time": {"structure": {"field": "TimeField", "input": "TimeInput"},
                        "option": option_basic},
             "date": {"structure": {"field": "DateField", "input": "DateInput"},
                        "option": option_basic},
             "datetime": {"structure": {"field": "DateTimeField", "input": "DateTimeInput"},
                        "option": option_basic},
             "long_string": {"structure": {"field": "CharField", "input": "Textarea"},
                        "option": option_basic},
             "string": {"structure": {"field": "CharField", "input": "TextInput"},
                        "option": option_basic},
             }

# ADMIN AND USERS ROL
ADMIN = 1
USER = 2