from django.views import View
from django.shortcuts import redirect


class LogoutView (View) : 
    def get(self, request, **kwargs) : 
        res = redirect('login')
        res.delete_cookie('user')
        return res
        