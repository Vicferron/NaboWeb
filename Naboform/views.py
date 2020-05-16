from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Naboform.models import Infonabo
from datetime import datetime
from .forms import Formnabo, FormularioContacto
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def home(request):
    Infonabo.objects.filter(time__lt=datetime.now().time()).delete()
    infonabos=Infonabo.objects.all()
    return render(request, "home.html", {"infonabos":infonabos})

def Naboform(request):
    if request.method=="POST":
        naboform=Formnabo(request.POST)
        if naboform.is_valid():
            infForm=naboform.cleaned_data
            naboform.save()
            return redirect('home')
    else:
        naboform=Formnabo()
    return render(request, "form.html", {"form":naboform})

def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            mensaje=f"{infForm['mensaje']} from:{infForm['email']}"
            send_mail(infForm['asunto'], mensaje, infForm['email'],
            ['victorferron92@gmail.com'])
            return redirect("home")
    else:
        miFormulario=FormularioContacto()
    return render(request, "contacto.html", {"form":miFormulario})