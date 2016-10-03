import functools

from django.shortcuts import redirect
from django.utils.decorators import available_attrs


def login_obligatorio(view_func):
    """
    DECORATOR
    """
    def _wrapped_view(request, *args, **kargs):
        if request.session.get('session'):
            return view_func(request, *args, **kargs)
        else:
            return redirect('/')
    return functools.wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)

def admin(view_func):
    """
    Decorador
    """
    def _wrapped_view(request, *args, **kargs):
        if request.session.get('rol'):
            return view_func(request, *args, **kargs)
    return functools.wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)