# REDIRECT
ROOT_PATH = '/'

# FORMS IN DATABASE
def_form = dict(user_profile='user_profile')

# STRUCTURE FOR FORM
option_basic = {'type': 'required', 'name': 'required', 'label': 'optional',
                'placeholder': 'optional', 'help_text': 'optional',
                'required': 'optional'}
option_select = {'type': 'required', 'name': 'required', 'label': 'optional',
                 'placeholder': 'optional', 'required': 'optional',
                 'option': 'required'}

basic_scheme = [
    {"name": "type", "type": "select", "label": "Type",
     "option": [
         ["int", "Integer"], ["boolean", "Boolean"], ["select", "Select"],
         ["time", "Time"], ["date", "Date"], ["datetime", "Datetime"],
         ["long_string", "Area"], ["string", "String"]
     ]},
    {"name": "name", "type": "string", "label": "Name",
     "placeholder": "Define your name..."},
    {"name": "label", "type": "string", "label": "Label",
     "placeholder": "Define your label...", "not_required": True},
    {"name": "placeholder", "type": "string", "label": "Placeholder",
     "placeholder": "Define your placeholder...", "not_required": True},
    {"name": "help_text", "type": "string", "label": "Help text",
     "placeholder": "Define your help text...", "not_required": True},
    {"name": "required", "type": "boolean", "label": "Required",
     "not_required": True},
    {"name": "option", "type": "string", "label": "Option",
     "placeholder": "Define your option...", "not_required": True}
]

json_scheme = {
    "int": {"structure": {"field": "IntegerField", "input": "TextInput"},
            "option": option_basic},
    "boolean": {
        "structure": {"field": "BooleanField", "input": "CheckboxInput"},
        "option": option_basic},
    "select": {"structure": {"field": "ChoiceField", "input": "option"},
               "option": option_basic},
    "float": {"structure": {"field": "FloatField", "input": "TextInput"},
              "option": option_basic},
    "time": {"structure": {"field": "TimeField", "input": "TimeInput"},
             "option": option_basic},
    "date": {"structure": {"field": "DateField", "input": "DateInput"},
             "option": option_basic},
    "datetime": {
        "structure": {"field": "DateTimeField", "input": "DateTimeInput"},
        "option": option_basic},
    "long_string": {"structure": {"field": "CharField", "input": "Textarea"},
                    "option": option_basic},
    "string": {"structure": {"field": "CharField", "input": "TextInput"},
               "option": option_basic},
}

# ADMIN AND USERS ROL
ADMIN = 1
USER = 2
