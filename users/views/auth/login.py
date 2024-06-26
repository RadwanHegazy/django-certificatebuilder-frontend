from django.views import View
from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages


class LoginView (View) : 
    def get(self, request, **kwargs) : 
        return render(request,'login.html')
    
    def post (self, request, **kwargs) : 
        data = {
            'email' : request.POST.get('email', None),
            'password' : request.POST.get('password', None),
        }
        action = Action(
            url=MAIN_URL + '/user/auth/login/',
            data=data
        )
        action.post()
        if action.is_valid() : 
            res = redirect('profile')
            res.set_cookie('user',action.json_data()['token'])
            return res
        else:
            messages.error(request,'invalid email or password')
            return redirect('login')