from django.shortcuts import render
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import appeal.api
import requests



@csrf_exempt
@require_http_methods(['POST'])
def add_appeal(request):
    result = {}
    last_send = request.session.get('last_send')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email', None)
    content = request.POST.get('content', None)
    service = request.POST.get('service', None)


    request.session['last_send'] = datetime.now().strftime(r'%x %X')
    print('last_send ', last_send)
    if last_send:
        last_send = datetime.strptime(last_send, r'%x %X')
        if datetime.now() - last_send < timedelta(seconds=15):
            result = {'error': 'Too many query per minutes!'}
            return JsonResponse(result)
    
   
    appeal_result = getattr(_load_module('appeal'), 'add')(name, phone, email, content, service)
    text = f'Новое обращение от {name} {phone}'

    requests.get(settings.TG_API_URL + text)
    result['result'] = appeal_result.id if appeal_result else 0

    return JsonResponse(result)


def _load_module(module_name: str) -> object:
    """Load module api from string."""
    module_dict = {
        'appeal': appeal.api,
    }

    return module_dict[module_name]