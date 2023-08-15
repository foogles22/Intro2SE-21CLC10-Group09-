from django.shortcuts import redirect
from django.http import HttpResponse
def user_is_authenticated(function = None, redirect_url = '/home/'):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator(function)

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)   
            else:
                return HttpResponse("You are not authorized to view this page")
        return _wrapped_view
    return decorator