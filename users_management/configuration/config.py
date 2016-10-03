# REDIRECT
ROOT_PATH = '/'

# FORMS IN DATABASE
def_form = dict(user_profile='user_profile')

# STRUCTURE FOR FORM
options_scheme = ['type', 'name', 'label', 'placeholder', 'help',
                  'required', 'option']

# THE VALUE INDICATES IF REQUIRED
option_basic = {'type': True, 'name': True, 'label': False,
                'placeholder': False, 'help': False,
                'required': False}
option_select = {'type': True, 'name': True, 'label': False,
                 'placeholder': False, 'required': False,
                 'option': True, 'help': False}

json_scheme = {
    "int": {"structure": {"field": "IntegerField", "input": "TextInput"},
            "option": option_basic},
    "boolean": {
        "structure": {"field": "BooleanField", "input": "CheckboxInput"},
        "option": option_basic},
    "select": {"structure": {"field": "ChoiceField", "input": "option"},
               "option": option_select},
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

# BASIC SCHEME TO CHANGE JSON STRUCTURE
basic_scheme = [
    {"name": "type", "type": "select", "label": "Type",
     "option": [
         ["int", "Integer"], ["boolean", "Boolean"], ["select", "Select"],
         ["time", "Time"], ["date", "Date"], ["datetime", "Datetime"],
         ["long_string", "Area"], ["string", "String"]
     ]},
    {"name": "name", "type": "string", "label": "Name",
     "placeholder": "Define your name...", "required": True},
    {"name": "label", "type": "string", "label": "Label",
     "placeholder": "Define your label..."},
    {"name": "placeholder", "type": "string", "label": "Placeholder",
     "placeholder": "Define your placeholder..."},
    {"name": "help", "type": "string", "label": "Help text",
     "placeholder": "Define your help text..."},
    {"name": "required", "type": "boolean", "label": "Required"},
    {"name": "option", "type": "string", "label": "Option",
     "placeholder": "Define your option..."}
]

# ADMIN AND USERS ROL
ADMIN = 1
USER = 2
