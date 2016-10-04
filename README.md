# Users management

"Users management" is a system for managing users easily. This system allows dynamically generate forms.

# Requeriments
  - POSTGRESQL 9.4.5
  - Python 2.7.6
    - Django==1.10.1
    - psycopg2==2.6.2

### Installation
```sh
$ git clone https://github.com/jesusce21/users_management.git
```

### Test
```sql
-- Insert in "users_management_scheme"
1;"user_profile";"[{"help": "", "name": "name", "type": "string", "label": "Name", "required": "on", "placeholder": ""}, {"help": "", "name": "gender", "type": "select", "label": "Gender", "option": [["1", "Male"], ["3", "Female"]]}, {"help": "Write about yourself", "name": "description", "type": "long_string", "label": "Description", "placeholder": ""}, {"help": "", "name": "number_of_siblings", "type": "int", "label": "Number of siblings", "required": "on", "placeholder": ""}, {"help": "", "name": "check", "type": "boolean", "label": "I agree to terms"}]"

-- Insert in "users_management_user"
1;"admin";"admin";"{}";1;
2;"user";"user";"{}";2;
```

### View example
![Users management](static/image/example-v2.gif)

### Json structure
Permitted types
```json
["int", "float", "time", "date", "datetime", "long_string", "string", "select"]
```

Option for ["int", "float", "time", "date", "datetime", "long_string", "string"]
```json
{"type":"", "label": "", "name": "", "placeholder":"", "help_text": "", "required": ""}
```

Option for ["select"]
```json
{"type":"", "label": "", "name": "", "help_text": "", "required": "", "option": [[,]]}
```

### Next version
- Frontend: Improve Interface
- Backend:  Improve security (cypher password,...)
