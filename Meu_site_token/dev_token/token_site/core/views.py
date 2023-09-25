from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random

# Create your views here.
def Registration(request):
    form = RegistroForm()
    if request.method == 'POST':
        username = request.POST.get('nome')
        email = request.POST.get('email')
        user = Registro(nome=username, email=email)
        
        domain_name = get_current_site(request).domain
        token = str(random.random()).split('.')[1]
        user.token = token
        
        link = f'http://{domain_name}/verify/{token}'
        
        send_mail(
            'Vericação do Email',
            f'Clique para completar seu cadastro: {link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return HttpResponse('Verifique a caixa de entrada do seu email para confirmar')
    
    return render(request, 'index.html', {'form':form})
        
def verify(request, token):
    try:
        user = Registration.objects.filter(token = token)
        if user:
            user.is_verified = True
        return redirect('index')
    except Exception:
        return render(request,'sucess.html')