from django.views import View
from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages
from globals.decorators import login_required

class ProfileView (View) : 

    @login_required
    def get(self, request, **kwargs) : 
        return render(request,'profile.html')
    
    @login_required
    def post (self, request, **kwargs) :
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken')
        posted_data = {}
        for key, val in data.items():
            posted_data[key] = val
        
        action = Action(
            url = MAIN_URL + '/certificate/create/',
            data=posted_data,
            headers=kwargs['headers']
        )
        action.post()
        if action.is_valid() :
            response = action.json_data()
            return redirect(f"{MAIN_URL}/{response['output']}")
        else:
            messages.error(request, 'an error accoured')
            return response('profile')