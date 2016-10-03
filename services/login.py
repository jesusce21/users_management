from django.shortcuts import render, redirect
from users_management.configuration.config import ROOT_PATH, def_form, ADMIN, \
    json_scheme, basic_scheme, options_scheme
import simplejson as json
from services.utils import _get_scheme, _check_field_value, \
    _update_attr_dict, _alpha_num
from users_management.forms import UserForm, DinamicForm
from users_management.models import user
from users_management.settings import STATIC_URL
from users_management.views_decorator import login_obligatorio, admin


# TODO: LOGOUT, CIPHER PASSWORD, SIGN IN

def login(request):
    form = UserForm()
    min_param = {"STATIC_URL": STATIC_URL}
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            result = _get_user(request, min_param)
            if result:
                return result

    elif request.session.get('session'):
        result = _get_user(request, min_param, type='session')
        if result:
            return result

    min_param.update({"form": form})
    return render(request, 'home.html', min_param)


@login_obligatorio
def change_data(request):
    min_param = {"STATIC_URL": STATIC_URL}
    qry_input = { "username": request.session.get('username')}
    qry = user.objects.filter(**qry_input)

    if qry:
        fields = _get_scheme(def_form.get("user_profile"))
        form = DinamicForm(fields, qry.get().data)
        if request.method == 'POST':
            form = DinamicForm(fields, request.POST, data=request.POST)
            if (form.is_valid() and qry):
                data_finish = _check_field_value(fields, request.POST)
                _update_attr_dict(qry, data_finish, 'data')
                form = DinamicForm(fields, request.POST)

        data = dict(username=qry_input.get('username'), form=form, **min_param)
        return render(request, 'user_profile.html', data)

    else:
        return redirect(ROOT_PATH)


@login_obligatorio
@admin
def change_scheme(request):
    min_param = {"STATIC_URL": STATIC_URL}
    res_scheme = {}
    if request.method == 'POST':
        # CAPTURE ONLY THE PERMITTED OPTION
        for attr, value in request.POST.items():
            if any(s in attr for s in options_scheme):
                row = attr.split("_", 1)
                val = json.loads(value) if row[1] == 'option' else value
                if row[0] in res_scheme:
                    res_scheme[row[0]].update({row[1]: val})
                else:
                    res_scheme[row[0]] = {row[1]: val}

        # CHECK THE VALUE
        json_to_save = []
        for k, v in res_scheme.items():
            if v.get('type'):
                option = json_scheme.get(v.get('type')).get('option')
                for attr, value in v.items():
                    if option.get(attr) and not value:
                        pass
                        # RETURN ERROR
                json_to_save.append(v)
            else:
                pass
                #RETURN ERROR
        qry = _get_scheme(def_form.get("user_profile"), ret=True)
        _update_attr_dict(qry, json_to_save, 'data', combine=False)

    return redirect(ROOT_PATH)


@login_obligatorio
def logout(request):
    form = UserForm()
    min_param = {"STATIC_URL": STATIC_URL}
    if request.session.get('session'):
        for key in request.session.keys():
            del request.session[key]
    min_param.update({"form": form})
    return redirect(ROOT_PATH)


# ONLY FOR DRY
def _get_user(request, min_param, type='POST'):
    qry_input = {"username": getattr(request, type).get('username')}
    qry = user.objects.filter(**qry_input)
    if type == 'POST':
        qry = qry.filter(password=getattr(request, type).get('password'))
        qry_input["session"] = _alpha_num(30)

    if qry:
        qry_input['rol'] = qry.get().rol
        request.session.update(qry_input)
        request.session.set_expiry(3000)

        fields = _get_scheme(def_form.get("user_profile"))
        data = dict(username=qry_input.get('username'),
                    **min_param)
        if qry.get().rol == ADMIN:
            template = "admin_configuration.html"
            forms = []
            row_id = 'row0'
            count = 0
            for row in fields:
                row['option'] = json.dumps(row.get('option'))
                forms.append(DinamicForm(basic_scheme, row, multi_form=row_id))
                count += 1
                row_id = 'row%s' % count
            data["forms"] = forms
        else:
            template = 'user_profile.html'
            data["form"] = DinamicForm(fields, qry.get().data)

        return render(request, template, data)

    else:
        return False
