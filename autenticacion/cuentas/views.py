from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request,'cuentas/inicio.html')

@login_required
def__
